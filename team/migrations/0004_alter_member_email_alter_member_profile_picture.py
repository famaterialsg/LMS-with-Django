# Generated by Django 5.1.1 on 2024-10-31 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_member_email_member_profile_picture_member_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
