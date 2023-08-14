# Generated by Django 4.2.3 on 2023-08-09 00:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_url_user_alter_url_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('513086af-3d46-4315-bd36-9e94ce885728'), editable=False),
        ),
    ]