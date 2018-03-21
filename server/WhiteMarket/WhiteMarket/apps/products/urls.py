from django.contrib import admin
from django.urls import path
from WhiteMarket.apps.products import views 
 
urlpatterns = [ 
    path('products/', views.product_list), 
] 