from django.urls import path
from .views import order_list, order_detail, worker_list, \
    worker_detail, post_list, post_detail, status_list, status_detail

urlpatterns = [
    path('get_orders/', order_list, name="orders-list"),
    path('get_orders/<int:pk>/', order_detail, name="order-detail"),
    path('get_workers/', worker_list, name="workers-list"),
    path('get_workers/<int:pk>/', worker_detail, name="worker-detail"),
    path('get_posts/', post_list, name="posts-list"),
    path('get_posts/<int:pk>/', post_detail, name="post-detail"),
    path('get_statuses/', status_list, name="statuses-list"),
    path('get_statuses/<int:pk>/', status_detail, name="status-detail"),
]
