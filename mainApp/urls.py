from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutus, name='aboutus'),
    path('booking/<int:car_id>/', views.booking, name='booking'),
    path('cars', views.cars, name='cars'),
    path('detail/<int:car_id>/', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('fuel', views.fuel, name='fuel'),
    path('track', views.track, name='track'),
    path('status', views.trackStatus, name='trackStatus'),
    path('shipping', views.shipping, name='shipping'),
    path('success_shipping/<str:customer_name>/<str:phone_number>/<str:email>/', views.success_shipping, name='success_shipping'),
    path('success/<str:car_name>/<str:car_model>/', views.success_page, name='success_page'),
]