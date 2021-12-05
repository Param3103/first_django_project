from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# URLConfiguration
urlpatterns = [
    path('hello/', views.registration_page),
    path('thank_you/', views.thank_you),
    path('show/', views.display_registered_users),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),
    path('update_user/<int:id>/', views.update_user, name="update_user"),
    path('file_upload/', views.file_upload),
    path('test_cookie/', views.test_cookie),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)