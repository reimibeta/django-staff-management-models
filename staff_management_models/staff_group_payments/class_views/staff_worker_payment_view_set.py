from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from staff_management_models.staff_group_payments.class_models.staff_worker_payment import StaffWorkerPayment
from staff_management_models.staff_group_payments.class_serializers.staff_worker_payment_serializer import \
    StaffWorkerPaymentSerializer


class StaffWorkerPaymentViewSet(viewsets.ModelViewSet):
    queryset = StaffWorkerPayment.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffWorkerPaymentSerializer
