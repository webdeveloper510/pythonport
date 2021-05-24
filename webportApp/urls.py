from django.urls import path
# from . import views
from webportApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
urlpatterns = [ 
 
     path('', views.profile, name='/'),
     path('form', views.form_page, name='form'),
     # path('profile', views.profile, name='profile'),
     path('profile_user_data', views.profile_list_page, name='profile_user_data'),
     path('table', views.tables_page, name='table'),
     path('typography', views.typosgraphy_page, name='typography'),
     path('user', views.user_page, name='user'),
     path('delete',views.delete_fn,name="delete"),
     path('profile_delete',views.profile_delete_fn,name="profile_delete"),
     path('register',views.register_page,name="register"),
     path('login',views.login_page,name="login"),
     path('logout',views.logout,name="logout"),
     path('check_enable',views.enable_user,name="check_enable"),
     path('check_res',views.response,name="check_res"),
     
]

