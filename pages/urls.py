from django.urls import path
from .views import AboutPageView, HomePageView, LoginPageView, SignUpPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/',SignUpPageView.as_view(), name='signup'),

]
