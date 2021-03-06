# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_no', models.PositiveIntegerField()),
                ('line_desc', models.CharField(max_length=100)),
                ('line_comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('line_num1', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('line_num2', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('line_num3', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('line_num4', models.DecimalField(blank=True, decimal_places=7, max_digits=20, null=True)),
                ('line_alpha1', models.CharField(blank=True, max_length=30, null=True)),
                ('line_alpha2', models.CharField(blank=True, max_length=60, null=True)),
                ('line_date1', models.DateField(blank=True, null=True)),
                ('line_date2', models.DateField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('last_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParTable',
            fields=[
                ('table_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('table_desc', models.CharField(max_length=100)),
                ('table_comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('table_num1', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('table_num2', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('table_num3', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('table_num4', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('last_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='parline',
            name='table_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.ParTable'),
        ),
        migrations.AlterUniqueTogether(
            name='parline',
            unique_together=set([('table_no', 'line_no')]),
        ),
    ]
