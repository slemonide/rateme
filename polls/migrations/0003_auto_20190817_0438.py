# Generated by Django 2.2.4 on 2019-08-17 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_auto_20190817_0431'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'rating_card')},
        ),
    ]