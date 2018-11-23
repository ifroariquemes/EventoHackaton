from django.urls import path
from .views import login, event_view, event, accreditation, user, user_edit, organization_edit, frequency, event_edit, organizations
urlpatterns = [
    path('login/', login),
    path('event_view/', event_view),
    path('event/', event),
    path('accreditation/', accreditation),
    path('user/', user),
    path('user_edit/', user_edit),
    path('organization_edit/',organization_edit),
    path('frequency/', frequency),
    path('event_edit/', event_edit),
    path('organizations/', organizations),
]