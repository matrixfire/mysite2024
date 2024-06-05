from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home page for reobrix.
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('reviews/', views.reviews, name='reviews'),
    path('contacts/', views.contacts, name='contacts'),

    path('search_results/', views.search_results, name='search_results'),
    path('single_program/', views.single_program, name='single_program'),
    
]
