from django.urls import path
from .views import *

urlpatterns = [
    path('product-type/', ProductTypeView.as_view({'get':'list','post':'create'})),
    path('product-type/<int:pk>/', ProductTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    
    path('product/', ProductApiView.as_view(),name='product'),
    path('product/<int:pk>/', ProductDetailsApiView.as_view()),
    path('login/', login),
    path('register/',register)
    
] 