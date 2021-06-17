# Generated by Django 3.1.7 on 2021-06-02 03:13

from django_datetime.datetime import datetime
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import staff_management_models.staff_group_payments.class_apps.staff_payment_status_choice


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff_groups', '0001_initial'),
        ('wallet_models', '0004_delete_walletadjust'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffWorkerPaymentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default=datetime.dnow())),
            ],
        ),
        migrations.CreateModel(
            name='StaffWorkerPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('pay_status', models.CharField(choices=[('DAILY', 'daily'), ('MONTHLY', 'monthly'), ('YEARLY', 'yearly'), ('OPTIONAL', 'optional')], default=staff_management_models.staff_group_payments.class_apps.staff_payment_status_choice.StaffPaymentStatusChoice['DAILY'], max_length=60)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_models.wallet')),
                ('payment_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff_group_payments.staffworkerpaymentgroup')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff_groups.staffworker')),
            ],
        ),
    ]
