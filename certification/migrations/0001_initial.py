# Generated by Django 5.1.1 on 2024-10-26 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('awarded_date', models.DateTimeField(blank=True, null=True)),
                ('awarded', models.BooleanField(default=False)),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certifications/')),
                ('certificate_html', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='course.course')),
            ],
        ),
    ]
