# Generated by Django 5.2 on 2025-04-30 13:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('nume', models.CharField(max_length=20)),
                ('magazin', models.CharField(max_length=20, null=True)),
                ('pret', models.FloatField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('ded0c2c1-a786-45c3-ae34-21c1aa71a658'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Produs',
        ),
    ]
