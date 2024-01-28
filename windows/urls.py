from django.urls import path
from windows.views import home, about, farm, garden, dairy_product, fruit, vegetables

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('farm/', farm, name='farm'),
    path('garden/', garden, name='garden'),
    path('dairy_product/', dairy_product, name='dairy'),
    path('fruit/', fruit, name='fruit'),
    path('vegetables/', vegetables, name='vegetable'),
]

