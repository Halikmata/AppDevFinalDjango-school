# Generated by Django 5.0 on 2023-12-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_guardians_number_of_children_teachers_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_images/'),
        ),
    ]
