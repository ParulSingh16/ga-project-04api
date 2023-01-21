# Generated by Django 4.1.5 on 2023-01-20 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('policies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insured_product', models.CharField(max_length=100)),
                ('insured_product_price', models.PositiveIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policy_name', to='policies.policy')),
            ],
        ),
    ]
