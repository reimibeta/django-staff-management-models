from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers

from staff_management_models.staff_group_payments import views

router = routers.DefaultRouter()
router.register('staff-payment-worker-group', views.StaffWorkerPaymentGroupViewSet)
router.register('staff-payment-worker', views.StaffWorkerPaymentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
