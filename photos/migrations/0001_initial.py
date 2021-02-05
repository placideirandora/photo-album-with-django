# Generated by Django 3.1.6 on 2021-02-05 15:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=225, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=225, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category')),
            ],
        ),
    ]