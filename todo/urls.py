from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('completeit/<str:todo_id>', views.completeit, name = 'completeit'),
    path('del_todo/<str:todo_id>', views.del_todo, name = 'deletetodo'),
    path('appraisal/', views.appraisal, name = 'appraisal'),
    path('plan/', views.plan, name = 'plans'),
    path('loginpage/', views.longinpage, name = 'loginpage'),
    path('logoutpage/', views.logoutpage, name = 'logoutpage'),
    path('registerpage/', views.registerpage, name = 'registerpage'),
    path('userprofile/', views.userprofile, name = 'userprofile'),
    path('signout/', views.signout, name = 'signout'),
]