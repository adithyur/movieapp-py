# Generated by Django 4.2.8 on 2023-12-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='asd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='yr',
            field=models.IntegerField(default='1234'),
            preserve_default=False,
        ),
    ]
