from django.urls import path
from rest_framework import routers

from . import views
from .views import PositionList, PositionDetail, EmployeeList, EmployeeDetail, OrderList, OrderDetail, OrderByStatusList

router = routers.SimpleRouter()

router.register(r'app', views.PositionList)


urlpatterns = [
    path('', PositionList.as_view(), name='position-list'),
    path('positions/<int:pk>/', PositionDetail.as_view(), name='position-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('orders/status/<str:status>/', OrderByStatusList.as_view(), name='order-by-status'),
]
