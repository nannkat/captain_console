# Generated by Django 3.0.6 on 2020-05-13 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consoleimage',
            old_name='candy',
            new_name='console',
        ),
    ]
