# Generated by Django 5.0.4 on 2024-05-06 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_comment_parent_coment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent_coment',
            new_name='parent_comment',
        ),
    ]
