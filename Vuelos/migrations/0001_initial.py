# Generated by Django 3.2.9 on 2022-11-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
                ('clase', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('desde', models.CharField(max_length=200)),
                ('hasta', models.CharField(max_length=200)),
                ('fechasalida', models.DateField()),
                ('fecharegreso', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
