from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('login/', TemplateView.as_view(template_name="oauth.html"), name="login"),
    path('login2/', TemplateView.as_view(template_name="oauth02_authorize.html"), name="login2"),
]