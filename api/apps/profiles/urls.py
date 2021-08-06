from allauth.account.views import ConfirmEmailView
from django.urls import include, path
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('', include('rest_auth.urls')),
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    path('registration/', include('rest_auth.registration.urls')),
    path(
        'account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path(
        'password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
]
