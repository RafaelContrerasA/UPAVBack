# Generated by Django 5.0.4 on 2024-04-16 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('pagina_fb', models.URLField()),
                ('status', models.CharField(max_length=10)),
                ('siglas', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accion', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('time', models.DateTimeField()),
                ('text', models.CharField(max_length=200)),
                ('me_gusta', models.IntegerField()),
                ('me_encanta', models.IntegerField()),
                ('me_divierte', models.IntegerField()),
                ('me_asombra', models.IntegerField()),
                ('me_entristece', models.IntegerField()),
                ('me_enoja', models.IntegerField()),
                ('me_importa', models.IntegerField()),
                ('id_dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('extracted_text', models.CharField(max_length=50)),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='dependencia',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.tipo'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('video_thumbnail', models.CharField(max_length=100)),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.publicacion')),
            ],
        ),
    ]
