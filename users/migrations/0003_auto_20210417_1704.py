# Generated by Django 2.2.3 on 2021-04-17 11:34

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210417_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturerrating',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='nopic.jpg', upload_to=users.models.Student.profile_pic_path),
        ),
    ]