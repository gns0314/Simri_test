# Generated by Django 4.2.6 on 2023-10-18 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psytest', '0003_remove_result_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psytest',
            name='writer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
