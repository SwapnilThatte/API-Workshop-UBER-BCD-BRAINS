# Generated by Django 3.2.9 on 2022-03-29 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0005_alter_ride_current_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='usr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uber.user1'),
        ),
    ]
