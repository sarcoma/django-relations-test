# Generated by Django 2.2.1 on 2019-05-09 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190509_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='scheduled_mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to='app.ScheduledMail'),
        ),
    ]