from .models import About, Category, Link, Post

#Procesadores de contexto lo que hacen es utilizar librerias para acceder a los datos

#ABOUT
def ctx_dict_about(request):
    ctx_about = {}
    ctx_about['About'] = About.objects.latest('-created')
    return ctx_about

#CATEGORY
def ctx_dict_category(request):
    ctx_category = {}
    ctx_category['Categories'] = Category.objects.filter(active=True)
    return ctx_category
    

#LINK = REDES SOCIALES 
def ctx_dict_link(request):
    ctx_link = {}
    links = Link.objects.all()
    for link in links:
        ctx_link[link.key] = {'social_media':link.name,'url':link.url, 'icon': link.icon}
    return ctx_link

#ARCHIVOS
def ctx_dict_history(request):
    ctx_history = {}
    ctx_history['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    return ctx_history