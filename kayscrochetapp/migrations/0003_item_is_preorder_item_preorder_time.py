# Generated by Django 5.0rc1 on 2024-03-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kayscrochetapp', '0002_item_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_preorder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='preorder_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
