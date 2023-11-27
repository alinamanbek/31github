from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    class_name = models.CharField(max_length=50)

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = (
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('applicant', 'Applicant'),
    )
    role = models.CharField(max_length=10, choices=role_choices)

class Teacher(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    subjects_taught = models.ManyToManyField(Subject)
    # Add other teacher-related fields

class Student(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    # Add other student-related fields

class Applicant(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    # Add other applicant-related fields

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)  # You might want to use a DecimalField for grades

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

# Add other models as needed based on your project requirements
