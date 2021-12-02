from django.urls import path
from . import views


# URLConfiguration
urlpatterns = [
    path('hello/', views.registration_page),
    path('thank_you/', views.thank_you),
    path('show/', views.display_registered_users),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),
    path('update_user/<int:id>/', views.update_user, name="update_user")
]
