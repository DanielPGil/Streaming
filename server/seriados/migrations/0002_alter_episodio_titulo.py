# Generated by Django 4.0.1 on 2022-02-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]