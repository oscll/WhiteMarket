from django.contrib import admin
from django.urls import path
from WhiteMarket.apps.images import views
 
urlpatterns = [ 
    path('images/', 
        views.ImageList.as_view(),
        name=views.ImageList.name), 
    path('images/<int:pk>', 
        views.ImageDetail.as_view(),
        name=views.ImageDetail.name), 
]
