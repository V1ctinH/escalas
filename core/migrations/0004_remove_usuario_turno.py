# Generated by Django 5.1.6 on 2025-03-04 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_escala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='turno',
        ),
    ]
