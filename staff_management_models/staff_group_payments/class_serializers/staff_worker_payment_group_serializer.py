from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
# from rest_framework_utils.key_related_field import key_related_field
from staff_management_models.staff_group_payments.class_models.staff_worker_payment import StaffWorkerPayment, \
    StaffWorkerPaymentGroup
from staff_management_models.staff_group_payments.class_serializers.staff_worker_payment_serializer import \
    StaffWorkerPaymentSerializer


class StaffWorkerPaymentGroupSerializer(FlexFieldsModelSerializer):
    # staff_phone = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    staff_worker_payment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = StaffWorkerPaymentGroup
        fields = [
            'id',
            'url',
            'pay_date',
            'staff_worker_payment'
        ]
        expandable_fields = {
            # 'staff_phone': (StaffPhoneSerializer, {'many': True}),
            'staff_worker_payment': (StaffWorkerPaymentSerializer, {'many': True})
        }
