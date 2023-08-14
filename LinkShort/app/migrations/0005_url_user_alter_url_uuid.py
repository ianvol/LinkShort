# Generated by Django 4.2.3 on 2023-08-08 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_url_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e49fcbf5-d488-471d-b7b3-c27b050a2bae'), editable=False),
        ),
    ]
