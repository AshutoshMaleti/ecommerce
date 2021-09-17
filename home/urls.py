from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('brands/', views.Brands, name='Brands'),

    path('customers-details/', views.CustomerDetails, name='CustomerDetails'),
    path('get-customers-details/<str:pk>/', views.GetCustomersDetails, name='GetCustomersDetails'),
    path('update-customers-details/<str:pk>/', views.UpdateCustomersDetails, name='UpdateCustomersDetails'),
    path('delete-customers-details/<str:pk>/', views.DeleteCustomer, name='DeleteCustomer'),
    
    path('add-address/<str:pk>/', views.SetAddress, name='SetAddress'),

    path('write-reviews/<str:pk>/', views.WriteReviews, name='WriteReviews'),
    path('read-reviews/<str:pk>/', views.ReadReviews, name='ReadReviews'),
    path('update-reviews/<str:pk>/', views.UpdateReviews, name='UpdateReviews'),
    path('delete-reviews/<str:pk>/', views.DeleteReviews, name='DeleteReviews'),
]