from decimal import Decimal

from django_datetime.datetime import datetime
from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

# from pcr_models.products.product_accounts.models import ProductAccount
from staff_models.staff_groups.class_models.staff_worker import StaffWorker
# from wallet_models.wallet_models.wallet import Wallet

# from staff_management_models.classes.balances.outlets.balance_outlet import BalanceOutlet
from wallet_models.class_apps.wallets.wallet_outlet import WalletAccountOutlet
from wallet_models.class_models.wallet import Wallet

from staff_management_models.staff_group_payments.class_apps.staff_payment_status_choice import \
    StaffPaymentStatusChoice


class StaffWorkerPaymentGroup(models.Model):
    pay_date = models.DateField(default=datetime.dnow())

    def __str__(self):
        return "{}".format(self.pay_date)


class StaffWorkerPayment(models.Model):
    payment_group = models.ForeignKey(
        StaffWorkerPaymentGroup,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='staff_worker_payment'
    )
    account = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffWorker, on_delete=models.CASCADE)
    # pay_date = models.DateField(default=DateTime.datenow)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    pay_status = models.CharField(
        max_length=60,
        choices=StaffPaymentStatusChoice.choices(),
        default=StaffPaymentStatusChoice.DAILY,
    )

    def __str__(self):
        return "{}".format(self.staff)


@receiver(post_save, sender=StaffWorkerPayment)
def add(sender, instance, created, **kwargs):
    if created:
        # account
        # BalanceOutlet()
        WalletAccountOutlet.outlet_account(
            amount=instance.amount,
            account_pk=instance.account.id
        )


@receiver(pre_save, sender=StaffWorkerPayment)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        old_value = StaffWorkerPayment.objects.get(id=instance.id)
        # account
        if instance.account.id == old_value.account.id:
            WalletAccountOutlet.update_outlet_account(
                new_amount=instance.amount,
                old_amount=old_value.amount,
                account_pk=instance.account.id
            )
        else:
            # refund
            WalletAccountOutlet.refund_outlet_account(old_value.amount, old_value.account.id)
            # outlet
            WalletAccountOutlet.outlet_account(instance.amount, instance.account.id)


@receiver(pre_delete, sender=StaffWorkerPayment)
def delete(sender, instance, using, **kwargs):
    old_value = StaffWorkerPayment.objects.get(id=instance.id)
    WalletAccountOutlet.refund_outlet_account(old_value.amount, old_value.account.id)
