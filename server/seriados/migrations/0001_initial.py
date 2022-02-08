# Generated by Django 4.0.1 on 2022-01-30 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewEpisodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(choices=[('A', 'Excelente'), ('B', 'Bom'), ('C', 'Ruim')], default='B', max_length=1)),
                ('episodio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriados.episodio')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriados.serie')),
            ],
        ),
        migrations.CreateModel(
            name='Revisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_episodios', models.ManyToManyField(through='seriados.ReviewEpisodio', to='seriados.Episodio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reviewepisodio',
            name='revisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriados.revisor'),
        ),
        migrations.AddField(
            model_name='episodio',
            name='temporada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriados.temporada'),
        ),
    ]
