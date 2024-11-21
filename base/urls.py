from django.urls import path
from . import views

urlpatterns = [
    path('rides/', views.RideModelListView.as_view(), name='ride-list'),
    path('ride/create/', views.RideModelCreateView.as_view(), name='ride-create'),
    path('ride/update/<int:pk>/', views.RideModelUpdateView.as_view(), name='ride-update'),
    path('ride/delete/<int:pk>/', views.RideModelDeleteView.as_view(), name='ride-delete'),

    path('users/', views.UserModelListView.as_view(), name='user-create'),
    path('user/create/', views.UserModelCreateView.as_view(), name='user-list'),
    path('user/update/<int:pk>/', views.UserModelUpdateView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', views.UserModelDeleteView.as_view(), name='user-delete'),

    path('createride/<str:start>/<str:destination>/<str:user>/', views.createRide, name='create-ride'),
    path('cancelride/<int:id>/', views.cancelRide, name='cancel-ride'),
    path('getrider/<int:ride_id>/', views.getRider, name='get-rider'),
    path('riderarrived/<int:ride_id>/', views.riderArrived, name='rider-arrived'),
    path('startride/<int:ride_id>/', views.startRide, name='start-ride'),
    path('endride/<int:ride_id>/', views.endRide, name='end-ride'),
    path('rateride/<int:ride_id>/<int:rating>/<str:feed_back>/', views.rateRide, name='rate-ride'),

    path('gethistory/<str:user>/', views.rideHistory, name='ride-history'),
    path('login/<str:password>/', views.login, name='user-login'),
]