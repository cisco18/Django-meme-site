# Generated by Django 3.2.5 on 2021-12-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]