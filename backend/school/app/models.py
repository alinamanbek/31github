from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = (
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('applicant', 'Applicant'),
    )
    role = models.CharField(max_length=10, choices=role_choices)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    subjects_taught = models.ManyToManyField(Subject)

    def __str__(self):
        return self.user_account.user.username

class Student(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_account.user.username

class Applicant(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    # Add other applicant-related fields

    def __str__(self):
        return self.user_account.user.username

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust as needed

    def __str__(self):
        return f"{self.student.user_account.user.username} - {self.subject.subject_name} - {self.grade}"

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Add other models as needed based on your project requirements
