from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('enquire/', views.submit_enquiry, name='submit_enquiry'),
    path('enquiry/', views.enquiry_view, name='enquiry'),

]
