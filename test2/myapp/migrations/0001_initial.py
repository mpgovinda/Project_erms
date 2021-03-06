# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 07:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University', models.CharField(max_length=100)),
                ('Degree', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_For_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='DegreeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.CharField(default=b'IT', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10)),
                ('HierachyNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exp_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.FloatField(max_length=2.2)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.CharField(max_length=100)),
                ('Duration', models.FloatField(max_length=2.2)),
                ('Notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Extracurricular', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TimeField()),
                ('Date', models.DateField()),
                ('Interviewer_Review', models.TextField(blank=True, null=True)),
                ('HOD_Review', models.TextField(blank=True, null=True)),
                ('HR_Review', models.TextField(blank=True, null=True)),
                ('NoOfPasses', models.PositiveIntegerField()),
                ('NoOfFails', models.PositiveIntegerField()),
                ('NoOfOnHolds', models.PositiveIntegerField()),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
                ('HOD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InterviewType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LogMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('remember', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Message_Recieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecievedDate', models.DateField()),
                ('RecievedTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message_Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SentDate', models.DateField()),
                ('SentTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MsgType', models.IntegerField()),
                ('MsgTopic', models.CharField(max_length=100, null=True)),
                ('MsgCont', models.TextField(blank=True, null=True)),
                ('MsgAcceptance', models.IntegerField()),
                ('Reciever', models.ManyToManyField(related_name='Reciever_User', through='myapp.Message_Recieve', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ManyToManyField(related_name='Sender_User', through='myapp.Message_Send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIC', models.CharField(max_length=12, unique=True)),
                ('FName', models.CharField(max_length=30)),
                ('LName', models.CharField(max_length=30)),
                ('FullName', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Nationality', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(max_length=100)),
                ('AddressLine3', models.CharField(max_length=100)),
                ('AddressLine4', models.CharField(blank=True, max_length=100, null=True)),
                ('ContactNum', models.CharField(max_length=12)),
                ('Email', models.EmailField(max_length=254)),
                ('FacebookProf', models.CharField(blank=True, max_length=100, null=True)),
                ('LinkedInProf', models.CharField(blank=True, max_length=100, null=True)),
                ('PImage', models.ImageField(null=True, upload_to=myapp.models.Person_directory_path)),
                ('Objective', models.TextField()),
                ('CVPDF', models.ImageField(upload_to=myapp.models.Person_directory_path)),
                ('SpecialNotes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person_Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField()),
                ('SpecialNotes', models.TextField(null=True)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Degree_class')),
                ('Degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Degree')),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Interview')),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Interview_viewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('Rate', models.PositiveSmallIntegerField()),
                ('Person_Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person_Interview')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.CV_Status')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post', models.CharField(max_length=100)),
                ('Field', models.CharField(blank=True, max_length=100, null=True)),
                ('NoOfInterviews', models.PositiveIntegerField()),
                ('InterviewType', models.ManyToManyField(to='myapp.InterviewType')),
            ],
        ),
        migrations.CreateModel(
            name='Post_Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QName', models.CharField(max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecializedArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sports', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SubQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QName', models.CharField(max_length=100)),
                ('Result', models.CharField(blank=True, max_length=10, null=True)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('SubResult', models.CharField(max_length=4)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='subQul_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QName', models.CharField(max_length=100)),
                ('SubResult', models.CharField(max_length=10)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('UPhoto', models.ImageField(blank=True, null=True, upload_to=myapp.models.User_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfPublish', models.DateField()),
                ('ClosingDate', models.DateField()),
                ('NoOfIntDone', models.IntegerField()),
                ('NoOfPossitions', models.IntegerField()),
                ('DeptID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HallName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewers',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Users')),
                ('NoOfInts', models.PositiveIntegerField(blank=True, null=True)),
            ],
            bases=('myapp.users',),
        ),
        migrations.AddField(
            model_name='users',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department'),
        ),
        migrations.AddField(
            model_name='users',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='users',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='UserRole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserRole'),
        ),
        migrations.AddField(
            model_name='person',
            name='Degree',
            field=models.ManyToManyField(null=True, through='myapp.Person_Degree', to='myapp.Degree'),
        ),
        migrations.AddField(
            model_name='person',
            name='Department',
            field=models.ManyToManyField(to='myapp.Department'),
        ),
        migrations.AddField(
            model_name='person',
            name='Interview',
            field=models.ManyToManyField(null=True, through='myapp.Person_Interview', to='myapp.Interview'),
        ),
        migrations.AddField(
            model_name='person',
            name='Post',
            field=models.ManyToManyField(to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='message_send',
            name='Messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Messages'),
        ),
        migrations.AddField(
            model_name='message_send',
            name='Sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message_recieve',
            name='Messages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Messages'),
        ),
        migrations.AddField(
            model_name='message_recieve',
            name='Reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='InterviewType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.InterviewType'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Interviewers',
            field=models.ManyToManyField(related_name='User_Interviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='Vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Vacancy'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Venue'),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='ExPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ExPost', to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='exp_post',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='degree_for_post',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeField',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.DegreeField'),
        ),
        migrations.AddField(
            model_name='degree',
            name='DegreeType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.DegreeType'),
        ),
        migrations.AddField(
            model_name='person_interview_viewer',
            name='Interviewers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Interviewers'),
        ),
        migrations.AddField(
            model_name='person_interview',
            name='Interviewers',
            field=models.ManyToManyField(through='myapp.Person_Interview_viewer', to='myapp.Interviewers'),
        ),
        migrations.AddField(
            model_name='interviewers',
            name='Interview',
            field=models.ManyToManyField(to='myapp.Interview'),
        ),
        migrations.AddField(
            model_name='interviewers',
            name='SpecializedArea',
            field=models.ManyToManyField(to='myapp.SpecializedArea'),
        ),
    ]
