# Generated by Django 3.0.3 on 2020-06-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=24, null=True)),
                ('email', models.EmailField(default=None, max_length=24, null=True)),
                ('group', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
