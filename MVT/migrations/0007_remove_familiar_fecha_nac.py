# Generated by Django 4.1.3 on 2022-12-06 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MVT", "0006_familiar_fecha_nac"),
    ]

    operations = [
        migrations.RemoveField(model_name="familiar", name="fecha_nac",),
    ]
