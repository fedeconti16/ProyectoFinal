# Generated by Django 4.2.2 on 2023-06-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autosEnStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('km', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='clientesCompradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('autoComprado', models.CharField(max_length=40)),
                ('montoOperacionComp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='clientesVendedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('autoVendido', models.CharField(max_length=40)),
                ('montoOperacionVent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='empleadosVendedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('operacionesConcretadas', models.IntegerField()),
                ('montoVendido', models.IntegerField()),
            ],
        ),
    ]
