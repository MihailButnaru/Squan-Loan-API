# Generated by Django 2.2.5 on 2019-09-10 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190910_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
    ]
