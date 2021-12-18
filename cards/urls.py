from django.urls import path
from .views import CardListView, CardDetailView


urlpatterns = [
    path('', CardListView.as_view(), name='home'),
    path('post/<int:pk>/', CardDetailView.as_view(), name='carddetail'),
]
