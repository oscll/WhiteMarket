from django.contrib import admin
from django.urls import path
from WhiteMarket.apps.products import views
 
urlpatterns = [ 
    path('products/', views.ProductList.as_view(), name=views.ProductList.name),

    path('products/like/<int:pk>', views.ProductLike.as_view(), name=views.ProductLike.name),

    path('products/liked/', views.ProductLiked.as_view()),

    path('products/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.name),

    path('categories/', views.ProductCategoryList.as_view(), name=views.ProductCategoryList.name),

    path('categories/<int:pk>', views.ProductCategoryDetail.as_view(), name=views.ProductCategoryDetail.name),
] 