# Generated by Django 4.1.7 on 2023-03-28 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0002_alter_car_image_alter_car_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_bid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='car.car')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
