# Generated by Django 3.2.5 on 2021-12-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0002_alter_meme_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
