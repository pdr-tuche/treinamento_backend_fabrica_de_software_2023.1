from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AnimeViewSet


router = DefaultRouter()

router.register('', AnimeViewSet)

urlpatterns = router.urls
