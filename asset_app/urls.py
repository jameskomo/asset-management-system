from django.urls import path
from django.conf.urls import url
from .views import (
    AssetsListView,
    AssetsDetailView,
    AssetsCreateView,
    AssetsUpdateView,
    AssetsDeleteView,
)
from . import views

urlpatterns = [
    path('', AssetsListView.as_view(), name='assets_app_home'),
    path('assets/<int:pk>/', AssetsDetailView.as_view(), name='assets-detail'),
    path('assets/new/', AssetsCreateView.as_view(), name='assets-create'),
    path('assets/<int:pk>/update/', AssetsUpdateView.as_view(), name='assets-update'),
    path('assets/<int:pk>/delete/', AssetsDeleteView.as_view(), name='assets-delete'),
    path('about/', views.about, name='asset_app-about'),
    url(r'^searchassets/$', views.assetssearch, name='assetssearch'),
]
