# Generated by Django 5.0.4 on 2024-05-06 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_coment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_comment', to='places.comment'),
        ),
    ]
