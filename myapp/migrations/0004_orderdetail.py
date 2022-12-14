# Generated by Django 4.0 on 2022-08-10 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_products_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('has_paid', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.products')),
            ],
        ),
    ]
