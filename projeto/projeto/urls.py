"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from visu import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('admin/', admin.site.urls),
    path('visu/', views.visu, name = 'visu'),    
    path('<str:model_name>/', views.list_view, name='list2'),
    path('<str:model_name>/create/', views.create_view, name='create'),
    path('<str:model_name>/<int:pk>/', views.detail_view, name='detail'),
    path('<str:model_name>/<int:pk>/update/', views.update_view, name='update'),
    path('<str:model_name>/<int:pk>/delete/', views.delete_view, name='delete'),

]
