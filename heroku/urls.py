from django.contrib import admin
from django.urls import path
import herokuApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', herokuApp.views.main, name='main'),
    path('new/create', herokuApp.views.create, name='create'),
    path('post/<str:id>', herokuApp.views.detail, name='detail'),
    path('edit/<str:id>', herokuApp.views.edit, name='edit'),
    path('update/<str:id>', herokuApp.views.update, name='update'),
    path('delete/<str:id>', herokuApp.views.delete, name='delete'),
]