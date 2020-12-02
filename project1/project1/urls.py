"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget import views as budget_view
from core import views as core_view
from tasks import views as tasks_view
from log import views as log_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.core, name='core'),
    path('tasks/', tasks_view.tasks, name='tasks'),
    path('budget/', budget_view.budget, name='budget'),
    path('join/', log_view.join, name='join'),
    path('login/', log_view.user_login, name='login'),
    path('logout/', log_view.user_logout, name='logout'),
    path('add_tasks/', tasks_view.add_tasks, name='add_tasks'),
    path('edit_tasks/', tasks_view.edit_tasks, name='edit_tasks'),
]
