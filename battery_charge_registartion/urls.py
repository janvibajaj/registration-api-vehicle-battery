from django.urls import path
from .views import RegistrationListAPIView,RegistrationDetails

urlpatterns = [
    path('registration-list/',RegistrationListAPIView.as_view()),
    path('detail/<int:id>/',RegistrationDetails.as_view()),
]
