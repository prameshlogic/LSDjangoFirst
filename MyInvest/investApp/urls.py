from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import userViewSet

router = DefaultRouter()
router.register(r'userView', userViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

