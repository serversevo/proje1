from django.urls import path

from . import views as uviews # 2 tane views olduğundan sadece isim verdim
from home import views

urlpatterns = [

    path('', views.index, name='index'),
    #path('content/<int:id>/<slug:slug>/', views.content_detail, name='content_detail'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),#verileri alır,product_detail sayfasına gönderir
    #path('addcomment/<int:id>/', pviews.addcomment, name='addcomment'),#form kontrolü


]