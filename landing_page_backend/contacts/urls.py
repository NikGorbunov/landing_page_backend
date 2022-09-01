from django.urls import path

from contacts.views import ContactAPIView

urlpatterns = [
    path('api/v1/contacts/', ContactAPIView.as_view(), name='contacts'),
]