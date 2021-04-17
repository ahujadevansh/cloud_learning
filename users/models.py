import os
import datetime

from django.db import models
from django.contrib.auth.models import User

# name & email are in auth_user
class Lecturer(models.Model):
    
    DEFAULT_PROFILE_IMAGE = 'nopic.jpg'

    def profile_pic_path(self, filename):
        if filename != self.DEFAULT_PROFILE_IMAGE:
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'profile_pics/{userid}/{basename}_{randomstring}{ext}'.format(
                userid=self.id, basename=basefilename, randomstring=randomstr, ext=file_extension)
        return self.DEFAULT_PROFILE_IMAGE

    profile_pic = models.ImageField(default=DEFAULT_PROFILE_IMAGE, upload_to=profile_pic_path)
    account = models.ForeignKey(User, models.DO_NOTHING, db_column='account', blank=True, null=True)
    bio = models.CharField(max_length=500, null=True)
    about = models.TextField(null=True)
    achievements = models.TextField(null=True)
    designation = models.CharField(max_length=100, default="Associate Professor")

    class Meta:
        db_table = 'lecturer'
    
    def __str__(self):
        return f'Lecturer {self.account.username}'


# name, email, last_login are in auth_user
class Student(models.Model):
    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=80, blank=True, null=True)
    nationality = models.CharField(max_length=80, blank=True, null=True)
    occupy = models.CharField(max_length=80, blank=True, null=True)
    graduated_university = models.CharField(max_length=80, blank=True, null=True)
    # email = models.CharField(max_length=80, blank=True, null=True)
    account = models.ForeignKey(User, models.DO_NOTHING, db_column='account', blank=True, null=True)
    course = models.ForeignKey('course.Course', models.DO_NOTHING, db_column='course', blank=True, null=True)
    # last_login = models.DateTimeField(blank=True, null=True)
    accumulated_online_time = models.DateTimeField(blank=True, null=True)
    dob = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return f'Student {self.account.username}'


class LecturerRating(models.Model):
    lecturer = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='lecturer', blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='student', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'lecturer_rating'
    
    def __str__(self):
        return f'{self.lecturer} | {self.rating}'
