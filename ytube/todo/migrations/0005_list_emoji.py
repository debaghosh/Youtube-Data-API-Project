# Generated by Django 3.1.2 on 2021-04-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210422_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='emoji',
            field=models.CharField(choices=[('studies', '🎓'), ('tech', '👩\u200d💻'), ('hallyu', '🇰🇷'), ('funny', '🤣'), ('entertainment', '📺'), ('booktube', '📚')], default=False, max_length=20),
        ),
    ]
