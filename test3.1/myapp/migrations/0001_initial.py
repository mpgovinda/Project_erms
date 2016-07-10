# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-03 09:34
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
                ('Field', models.CharField(max_length=100)),
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
                ('AltPost', models.CharField(blank=True, max_length=100, null=True)),
                ('Field', models.CharField(max_length=100)),
                ('Duration', models.FloatField(max_length=2.2)),
                ('YearStart', models.IntegerField()),
                ('YearEnd', models.IntegerField()),
                ('Company', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Extracurricular', models.CharField(max_length=100)),
                ('Description', models.TextField()),
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
                ('NoOfPasses', models.PositiveIntegerField(blank=True, null=True)),
                ('NoOfFails', models.PositiveIntegerField(blank=True, null=True)),
                ('NoOfOnHolds', models.PositiveIntegerField(blank=True, null=True)),
                ('InterviewNo', models.IntegerField()),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
                ('HOD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interview_Interviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Interview')),
                ('Interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MsgType', models.IntegerField()),
                ('MsgCont', models.TextField(blank=True, null=True)),
                ('MsgAcceptance', models.IntegerField()),
                ('SentDate', models.DateField()),
                ('SentTime', models.TimeField()),
                ('RecievedDate', models.DateField(null=True)),
                ('RecievedTime', models.TimeField(null=True)),
                ('Recieve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Msg_Reciever', to=settings.AUTH_USER_MODEL)),
                ('Send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIC', models.CharField(max_length=12, unique=True)),
                ('FName', models.CharField(max_length=30)),
                ('LName', models.CharField(max_length=30)),
                ('FullName', models.CharField(max_length=100)),
                ('DOB', models.DateField(null=True)),
                ('DateRecieved', models.DateField()),
                ('Nationality', models.CharField(max_length=20)),
                ('AddressLine1', models.CharField(max_length=100)),
                ('AddressLine2', models.CharField(max_length=100)),
                ('AddressLine3', models.CharField(max_length=100)),
                ('ContactNum', models.CharField(max_length=12)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('FacebookProf', models.CharField(blank=True, max_length=100, null=True)),
                ('LinkedInProf', models.CharField(blank=True, max_length=100, null=True)),
                ('PImage', models.FileField(blank=True, null=True, upload_to=myapp.models.Person_directory_path)),
                ('Interests', models.TextField(blank=True, null=True)),
                ('Objective', models.TextField(blank=True, null=True)),
                ('CVImage', models.FileField(blank=True, null=True, upload_to=myapp.models.Person_directory_path)),
                ('PersonalHighlight', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YearStart', models.IntegerField()),
                ('YearEnd', models.IntegerField()),
                ('SpecialNotes', models.TextField(null=True)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Degree_class')),
                ('Degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Degree')),
                ('Personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Interview')),
                ('Personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Interview_viewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('Rate', models.PositiveSmallIntegerField()),
                ('Interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Personal_Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal_Interview')),
                ('Status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.CV_Status')),
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
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialAchievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading_1', models.CharField(max_length=100)),
                ('Heading_2', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecializedArea', models.CharField(max_length=100)),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sports', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='SubQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QName', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=150)),
                ('Result', models.CharField(blank=True, max_length=10, null=True)),
                ('SubResult', models.CharField(max_length=4)),
                ('QType', models.IntegerField()),
                ('SpecialNotes', models.TextField(blank=True, null=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal')),
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
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
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
                ('UPhoto', models.FileField(blank=True, null=True, upload_to=myapp.models.User_directory_path)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Department')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('UserRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserRole')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfPublish', models.DateField()),
                ('ClosingDate', models.DateField()),
                ('NoOfIntDone', models.IntegerField(default=0)),
                ('NoOfPossitions', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('Post_Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post_Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HallName', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='personal',
            name='DeptPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post_Dept'),
        ),
        migrations.AddField(
            model_name='personal',
            name='RecuritedPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
        migrations.AddField(
            model_name='interview',
            name='InterviewType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.InterviewType'),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal'),
        ),
        migrations.AddField(
            model_name='experience',
            name='Personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Personal'),
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
            model_name='degree',
            name='University',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.University'),
        ),
    ]
