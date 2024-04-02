from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateTaskAPIView.as_view(), name='get_post_tasks'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTaskAPIView.as_view(), name='get_delete_update_tasks'),
    path('labels', views.ListCreateLabelAPIView.as_view(), name='get_post_labels'),
    path('labels/<int:pk>/', views.RetrieveUpdateDestroyLabelAPIView.as_view(), name='get_delete_update_labels'),
]