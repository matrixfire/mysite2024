from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home page for reobrix.
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('blog-single-post/', views.blog_single_post, name='blog_single_post'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('contacts/', views.contacts, name='contacts'),
    path('join_us/', views.join_us, name='join_us'),
    path('index/', views.index, name='index'),
    path('privacy/', views.privacy, name='privacy'),
    path('search-results/', views.search_results, name='search_results'),
    path('shop/', views.shop, name='shop'),
    path('single-product/', views.single_product, name='single_product'),
    path('subscribe/', views.subscribe, name='subscribe'),
    
]
