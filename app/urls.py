from tkinter import N
from django.urls import path,include
from . import views
app_name = "app"


urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name ="new"),
    path('create/', views.create, name='create'),
    path('detail/<int:review_pk>', views.detail, name='detail'),
    path('edit/<int:review_pk>', views.edit, name='edit'),
    path('update/<int:review_pk>', views.update, name='update'),
    path('delete/<int:review_pk>', views.delete, name='delete'),
]