# Generated by Django 4.0 on 2022-08-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_orderdetail_stripe_payment_intent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='stripe_payment_intent',
            new_name='checkout_session_id',
        ),
    ]
