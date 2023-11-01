# Generated by Django 4.2.6 on 2023-11-01 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_item_main_image_mainimage_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='item',
            field=models.ForeignKey(help_text='Товар к которому добавить картинку', on_delete=django.db.models.deletion.CASCADE, related_name='image', to='catalog.item', verbose_name='товар'),
        ),
    ]
