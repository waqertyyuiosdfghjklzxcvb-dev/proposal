from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('submit', views.submit_proposal, name='submit_proposal'),
    path('logout/', views.logout_view),
]
