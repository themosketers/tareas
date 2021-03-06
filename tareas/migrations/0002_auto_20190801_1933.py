# Generated by Django 2.2.2 on 2019-08-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadosolicitud',
            fields=[
                ('id_essol', models.AutoField(db_column='Id_esSol', primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'estadosolicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadotarea',
            fields=[
                ('id_e', models.AutoField(db_column='Id_e', primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'estadotarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_n', models.AutoField(db_column='Id_n', primary_key=True, serialize=False)),
                ('nivel', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'nivel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id_prioridad', models.AutoField(db_column='Id_prioridad', primary_key=True, serialize=False)),
                ('prioridad', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'prioridad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id_s', models.AutoField(db_column='Id_s', primary_key=True, serialize=False)),
                ('sector', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'sector',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_sol', models.AutoField(db_column='Id_sol', primary_key=True, serialize=False)),
                ('solicitud', models.CharField(blank=True, max_length=30, null=True)),
                ('tiempoi', models.DateTimeField(blank=True, db_column='tiempoI', null=True)),
                ('tiempof', models.DateTimeField(blank=True, db_column='tiempoF', null=True)),
            ],
            options={
                'db_table': 'solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subtarea',
            fields=[
                ('id_sub', models.AutoField(db_column='Id_sub', primary_key=True, serialize=False)),
                ('starea', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'subtarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subtarea2',
            fields=[
                ('id_sub2', models.AutoField(db_column='Id_sub2', primary_key=True, serialize=False)),
                ('starea2', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'subtarea2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id_ta', models.AutoField(db_column='Id_ta', primary_key=True, serialize=False)),
                ('tarea', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('id_tie', models.AutoField(db_column='Id_tie', primary_key=True, serialize=False)),
                ('tiempoi', models.DateTimeField(blank=True, db_column='tiempoI', null=True)),
                ('tiempof', models.DateTimeField(blank=True, db_column='tiempoF', null=True)),
            ],
            options={
                'db_table': 'tiempo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_us', models.AutoField(db_column='Id_us', primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=10, null=True)),
                ('contraseña', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Tabla_test',
        ),
    ]
