from . import views
from django.urls import path

app_name = 'demo_app'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('product/<int:product_id>',views.single_product,name='single_product'),
    path('add',views.add_product,name='add_product')
]