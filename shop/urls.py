from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('json/', views.product_list_json, name='product_list_json'),
    path('json/category/<slug:category_slug>/', views.product_list_json, name='product_list_json_by_category'),
    path('json/collection/<slug:collection_slug>/', views.product_list_json, name='product_list_json_by_collection'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('collection/<slug:collection_slug>/', views.product_list, name='product_list_by_collection'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

