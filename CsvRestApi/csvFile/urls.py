from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewList.as_view(), name='viewlist'),
    #path('<int:pk>/', views.ViewList.get_csv, name='viewdetail')
]
