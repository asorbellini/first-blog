from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# MODELO DE CATEGORÍAS 
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        verbose_name= 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
# MODELO DE ETIQUETAS  
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        verbose_name= 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']
    
    def __str__(self):
        return self.name

# MODELO DE AUTOR = USUARIO REGISTRADO EN LA APP


# MODELO DE POST 
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts', null=True, blank= True, verbose_name='Imagen')
    image_description = models.TextField(max_length=200, verbose_name='Descripción de imagen', blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='Publicado')

    #Campos con relaciones con otras DB
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoría')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    likes = models.ManyToManyField(User, related_name='blog_post', blank=True , verbose_name='Me gusta')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        verbose_name= 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
############################################################

class About(models.Model):
    description = models.CharField(max_length=350, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')
    class Meta:
        verbose_name= 'Acerca de '
        verbose_name_plural = 'Acerca de nosotros'
        ordering = ['-created']
    def __str__(self):
        return self.description
    
#Modelo de redes sociales 
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key link')
    name = models.CharField(max_length=120, verbose_name='Red social')
    url = models.URLField(max_length=350,verbose_name='Enlace', blank=True, null=True)
    icon = models.CharField(max_length=100, verbose_name='Icono', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')
    class Meta:
        verbose_name= 'Red social '
        verbose_name_plural = 'Redes sociales'
        ordering = ['name']
    def __str__(self):
        return self.name
    