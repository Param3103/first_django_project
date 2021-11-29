from django.urls import path
from . import views


#URLConfiguration
urlpatterns = [
    path('hello/', views.form_view),
    path('thank_you/', views.thank_you)
]