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
    
    
    def send_sms_notification(self, message):
        # Your Twilio Account SID and Auth Token
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        twilio_phone_number = 'your_twilio_phone_number'

        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Student's phone number (replace with your actual logic to get the phone number)
        student_phone_number = 'student_phone_number'

        # Send SMS
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=student_phone_number
        )

        return message.sid


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
from django.db import models

class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject.subject_name} - {self.lesson_date} - {self.lesson_time}"



from django.db import models

class Schedule(models.Model):
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week_choices = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    day_of_week = models.CharField(max_length=10, choices=day_of_week_choices)
    lesson_time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.class_assigned.class_name} - {self.subject.subject_name} - {self.teacher.user_account.user.username} - {self.day_of_week} - {self.lesson_time}"
from django.db import models
from django.contrib.auth.models import User

class Director(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    # Add other director-related fields

    def __str__(self):
        return self.user_account.user.username
# models.py

from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    subjects_taught = models.ManyToManyField(Subject)
    # Add other fields specific to teachers

    def __str__(self):
        return self.user_account.user.username

class TeacherModule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.teacher.user_account.user.username} - {self.module_name}"
from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    due_date = models.DateField()
    description = models.TextField()
    # You can add more fields based on your requirements, such as file uploads, etc.

    def __str__(self):
        return f"{self.subject.subject_name} - {self.due_date} - {self.teacher.user_account.user.username}"
from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    # Add other parent-related fields

    def __str__(self):
        return self.user_account.user.username
from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    due_date = models.DateField()
    description = models.TextField()
    # Additional fields for homework
    additional_notes = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    # You can add more fields based on your requirements, such as file uploads, etc.

    def __str__(self):
        return f"{self.subject.subject_name} - {self.due_date} - {self.teacher.user_account.user.username}"
from django.db import models
from django.contrib.auth.models import User

class AbsentList(models.Model):
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    absent_students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.class_assigned.class_name} - {self.subject.subject_name} - {self.date}"
from django.db import models
from django.contrib.auth.models import User

class FinishedHomework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    completion_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user_account.user.username} - {self.homework.subject.subject_name} - {self.completion_date} - Approved: {self.is_approved}"
from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    max_marks = models.PositiveIntegerField()
    # You can add more fields based on your requirements

    def __str__(self):
        return f"{self.subject.subject_name} Exam - {self.date}"

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    obtained_marks = models.PositiveIntegerField()
    # You can add more fields based on your requirements

    def __str__(self):
        return f"{self.student.user_account.user.username} - {self.exam.subject.subject_name} Exam - Marks: {self.obtained_marks}"
from django.db import models
from django.contrib.auth.models import User

class Methodology(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='methodologies/', blank=True, null=True)

    def __str__(self):
        return f"{self.subject.subject_name} - {self.teacher.user_account.user.username} - {self.title}"
# serializers.py
from rest_framework import serializers
from .models import Subject, Class

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
