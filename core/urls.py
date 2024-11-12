
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:post_id>', views.post, name="post"),
    path('category/<int:category_id>', views.category, name="category"),
    path('author/<int:author_id>', views.author, name="author"),
    path('dates/<int:month_id>/<int:year_id>', views.dates, name="dates"),
    #Likes de un post
    path('like/<int:pk>', views.like_view, name='like_post'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logout/',views.signout, name='logout'),
    path('profile/', views.profile, name='profile'),
]