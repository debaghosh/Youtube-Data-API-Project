# Generated by Django 3.1.2 on 2021-04-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_list_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='link',
            field=models.URLField(default=False, max_length=1000),
        ),
    ]
