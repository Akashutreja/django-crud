from django.urls import path
from . import views

urlpatterns = [
    path('userdata/', views.UserDataList.as_view(), name='userdata-list'),
    path('userdata/<int:pk>/', views.UserDataDetail.as_view(), name='userdata-detail'),
]
