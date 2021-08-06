from allauth.account.views import ConfirmEmailView
from django.conf.urls import url
from django.urls import include, path
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    url(r'^registration/', include('rest_auth.registration.urls')),
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
