# Generated by Django 4.0.5 on 2022-07-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_comentariocontacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('titulo', models.CharField(max_length=100)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='alumnos',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comentariocontacto',
            options={},
        ),
    ]