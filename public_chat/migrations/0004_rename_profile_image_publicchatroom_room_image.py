# Generated by Django 4.0.3 on 2022-04-15 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat', '0003_publicchatroom_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicchatroom',
            old_name='profile_image',
            new_name='room_image',
        ),
    ]