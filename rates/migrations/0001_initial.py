# Generated by Django 4.1.5 on 2023-01-26 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productRate', models.IntegerField()),
                ('insuranceRate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner', to='partners.partner')),
            ],
        ),
    ]
