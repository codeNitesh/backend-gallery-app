from django.urls import path
from . import views

urlpatterns = [
	path('', views.imageList, name="images-list"),
	path('show/<str:pk>/', views.imageDetail, name="task-detail"),
	path('new/', views.imageCreate, name="task-create"),

	path('<str:pk>/edit/', views.imageUpdate, name="task-update"),
	path('delete/<str:pk>/', views.imageDelete, name="task-delete"),
]
