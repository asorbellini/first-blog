from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from .models import Post, Category
from django.contrib.auth.models import User
from .forms import ProfileForm
# Create your views here.

def home(request):
    if request.method == 'GET' and 'items_per_page' in request.GET:
        request.session['items_per_page'] = int(request.GET['items_per_page'])
    else:
        request.session['items_per_page'] = 2

    items_per_page = request.session['items_per_page']
    
    posts_page = Paginator(Post.objects.filter(published=True).order_by('-created'),items_per_page)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)

    return render(request, "core/home.html",{'posts':posts,})

def post(request, post_id):
    try: 
        post = get_object_or_404(Post, id=post_id)
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(request, 'core/detail.html',{'post':post, 'total_likes':total_likes, 'liked':liked})
    except:
        return render(request, 'core/404.html')

def category(request, category_id):
    try: 
        if request.method == 'GET' and 'items_per_page' in request.GET:
            request.session['items_per_page'] = int(request.GET['items_per_page'])
        elif not request.session['items_per_page']:
            request.session['items_per_page'] = 2

        items_per_page = request.session['items_per_page']

        category = get_object_or_404(Category, id=category_id)
        posts_page = Paginator(Post.objects.filter(category_id=category_id, published=True),items_per_page)
        page = request.GET.get('page')
        posts = posts_page.get_page(page)
        
        return render(request, 'core/category.html',{'category':category, 'posts':posts,})
    except:
        return render(request, 'core/404.html')

def author(request, author_id):
    try: 
        if request.method == 'GET' and 'items_per_page' in request.GET:
            request.session['items_per_page'] = int(request.GET['items_per_page'])
        elif not request.session['items_per_page']:
            request.session['items_per_page'] = 2

        items_per_page = request.session['items_per_page']

        author = get_object_or_404(User, id=author_id)
        posts_page = Paginator(get_list_or_404(Post, author_id=author_id, published=True),items_per_page)
        page = request.GET.get('page')
        posts = posts_page.get_page(page)

        return render(request, 'core/author.html',{'author':author, 'posts':posts,})
    except:
        return render(request, 'core/404.html')

def dates(request, month_id, year_id):
    months = {
        1:'Enero',
        2:'Febrero',
        3:'Marzo',
        4:'Abril',
        5:'Mayo',
        6:'Junio',
        7:'Julio',
        8:'Agosto',
        9:'Septiembre',
        10:'Octubre',
        11:'Noviembre',
        12:'Diciembre',
    }
    if month_id > 12 or month_id < 1:
        return render(request, 'core/404.html')
    
    if request.method == 'GET' and 'items_per_page' in request.GET:
        request.session['items_per_page'] = int(request.GET['items_per_page'])
    elif not request.session.get('items_per_page'):
        request.session['items_per_page'] = 2
    
    items_per_page = request.session['items_per_page']

    posts_page = Paginator(Post.objects.filter(published=True,created__month=month_id, created__year=year_id),items_per_page)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)

    return render(request, 'core/dates.html', {'posts':posts, 'month':months[month_id], 'year':year_id,})

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post', args=[str(pk)]))

def register(request):
    if request.method == 'GET':
        try:
            return render(request, 'core/register.html',{
            'form': UserCreationForm
        })
        except:
            return render(request, 'core/404.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'core/register.html',{
            'form': UserCreationForm,
            'error' : 'El usuario ya existe.'
            })

            except ValueError:
                return render(request, 'core/register.html',{
            'form': UserCreationForm,
            'error' : 'Complete los campos solicitados.'
            })

        return render(request, 'core/register.html',{
            'form': UserCreationForm,
            'error' : 'La contraseña no coincide, vuelva a intentarlo.'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'core/signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request,'core/signin.html',{
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos.'
            } )
        else:
            login(request, user)
            return redirect('home')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user        
    posts = Post.objects.all()
    liked_posts = []
    for post in posts:
        if post.likes.filter(id=request.user.id).exists():
            liked_posts.append(post)
       
    editing = request.GET.get('edit') == '1'
    success = False

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            success = True
            return redirect('profile')
        else:
            success = 'Existe un error en los datos ingresados, por favor vuelva a intentarlo'
    else:
        form = ProfileForm
        
    return render(request, 'core/profile.html',{
                    'user':user,
                    'liked_posts':liked_posts,
                    'form':form,
                    'editing':editing,
                    'success': success,
                })

