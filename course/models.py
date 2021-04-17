import datetime
import os

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from users.models import Lecturer

class Faculty(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    faculty_describtion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'faculty'

    def __str__(self):
        return f'Faculty {self.name}'


class Course(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    course_describtion = models.TextField(blank=True, null=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty', blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'course'
    
    def __str__(self):
        return f'Course {self.id} | Name: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'Category {self.name}'

class Subject(models.Model):

    DEFAULT_PROFILE_IMAGE = 'nopic.jpg'

    def subject_pic_path(self, filename):
        if filename != self.DEFAULT_PROFILE_IMAGE:
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'subject_pics/{lecturer_id}/{basename}_{randomstring}{ext}'.format(
                lecturer_id=self.lecturer_id, basename=basefilename, randomstring=randomstr, ext=file_extension)
        return self.DEFAULT_PROFILE_IMAGE
    
    name = models.CharField(max_length=80, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    thumb = models.CharField(max_length=100, blank=True, null=True)
    pic = models.ImageField(default=DEFAULT_PROFILE_IMAGE, upload_to=subject_pic_path)

    pic = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    lecturer_id = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    requirements = models.TextField()
    duration = models.IntegerField()

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return f'Subject {self.id} | Name: {self.name}'


class SubjectRating(models.Model):
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='subject', blank=True, null=True)
    student = models.ForeignKey('users.Student', models.DO_NOTHING, db_column='student', blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    commence = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'subject_rating'

    def __str__(self):
        return f'Subject: {self.subject.name} | Student {self.student.account.username} | Rating: {self.rating}'


class Enrollment(models.Model):
    subject = models.ForeignKey('Subject', models.DO_NOTHING, db_column='subject')
    student = models.ForeignKey('users.Student', models.DO_NOTHING, db_column='student')
    status = models.IntegerField(blank=True, null=True)
    # lesson = models.ForeignKey('Lesson', models.DO_NOTHING, db_column='lesson', blank=True, null=True)

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return f'Student {self.student.account.username} | Subject: {self.subject.name}'