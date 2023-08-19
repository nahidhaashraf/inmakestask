
from django.urls import path
from . import views
urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('branches/', views.branches_view, name='branches'),
    path('login/', views.login_view, name='logging'),
    path('register', views.registration_view, name='registration'),
    path('new_page/', views.new_page_view, name='new_page'),
    path('new_page/application', views.application_form_view, name='application_form'),
    path('branches/credentials/register',views.register,name='register'),
    path('branches/credentials/logout',views.logout,name='logout'),
]