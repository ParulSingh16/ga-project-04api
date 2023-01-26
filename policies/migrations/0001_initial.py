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
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('increase_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('provider', models.ForeignKey(db_column='provider_id', on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='partners.partner')),
            ],
        ),
    ]
