# Generated by Django 2.2.1 on 2019-05-09 08:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0c96f733-d0d1-4517-84a4-03de71837a90'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('07b071b3-727f-4c33-8901-dc4037552fde'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('faa63154-2060-4600-b813-6543b13d7568'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scheduledmail',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c1eb4bad-ea7d-4739-8afa-16e771f435fa'), primary_key=True, serialize=False),
        ),
    ]
