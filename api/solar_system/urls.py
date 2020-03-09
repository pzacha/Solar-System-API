from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('solar_system', views.PlanetView)

urlpatterns = [
    path('', include(router.urls))
]

