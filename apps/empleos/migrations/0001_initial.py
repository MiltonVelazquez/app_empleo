# Generated by Django 4.2.3 on 2023-07-28 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empleos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nombre_empresa', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(blank=True, default='empleos/empleo_def.png', null=True, upload_to='empleos')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleos.categoria')),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]