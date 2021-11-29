from django.urls import path
from . import views


#URLConfiguration
urlpatterns = [
    path('hello/', views.registration_page),
    path('thank_you/', views.thank_you),
    path('show/', views.display_registered_users),
]