from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from staff_models.staffs.class_models.staff import Staff
from staff_models.staffs.class_serializers.staff_address_serializers import StaffAddressSerializer
from staff_models.staffs.class_serializers.staff_phone_serializers import StaffPhoneSerializer

from staff_management_models.staff_group_payments.class_models.staff_worker_payment import StaffWorkerPayment


class StaffWorkerPaymentSerializer(FlexFieldsModelSerializer):
    # staff_phone = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # payment_group = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = StaffWorkerPayment
        fields = [
            'id',
            'url',
            'account',
            'payment_group',
            'staff',
            'amount',
            'pay_status'
        ]
        expandable_fields = {
            # 'staff_phone': (StaffPhoneSerializer, {'many': True}),
            # 'payment_group': StaffWorkerPaymentGroupSerializer
        }
