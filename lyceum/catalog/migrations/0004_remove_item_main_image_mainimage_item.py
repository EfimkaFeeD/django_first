# Generated by Django 4.2.6 on 2023-11-01 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_item_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='main_image',
        ),
        migrations.AddField(
            model_name='mainimage',
            name='item',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='main_image', to='catalog.item'),
        ),
    ]
