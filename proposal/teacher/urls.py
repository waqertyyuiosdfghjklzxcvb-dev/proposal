from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login, name='teacher_login'),
    path('dashboard', views.dashboard, name='teacher_dashboard'),
    path('review/<int:proposal_id>', views.review_proposal, name='review_proposal'),
    path('logout', views.logout, name='teacher_logout'),
]
