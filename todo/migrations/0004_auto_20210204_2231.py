# Generated by Django 3.0 on 2021-02-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]