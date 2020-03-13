from django.urls import path 
from .views import  mainpage ,test  , login  , signup

urlpatterns = [

 path('mainpage/' , mainpage , name = 'mainpage') ,
 path('test/' , test ) ,
 path('login/' , login , name = 'login') , 
 path('signup/' , signup , name = 'signup'),
 

]

