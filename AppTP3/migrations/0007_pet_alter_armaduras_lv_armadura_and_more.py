# Generated by Django 5.0.2 on 2024-03-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTP3', '0006_armaduras_delete_curso_delete_estudiantes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('raza', models.CharField(max_length=60)),
                ('nivel', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='armaduras',
            name='lv_armadura',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='build',
            name='Total_daño',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='personajes',
            name='averno',
            field=models.IntegerField(default=1),
        ),
    ]