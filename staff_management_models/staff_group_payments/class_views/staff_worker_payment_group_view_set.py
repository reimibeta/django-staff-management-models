from staff_management_models.staff_group_payments.class_models.staff_worker_payment import StaffWorkerPaymentGroup
from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from staff_management_models.staff_group_payments.class_serializers.staff_worker_payment_group_serializer import \
    StaffWorkerPaymentGroupSerializer


class StaffWorkerPaymentGroupViewSet(viewsets.ModelViewSet):
    queryset = StaffWorkerPaymentGroup.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = StaffWorkerPaymentGroupSerializer
