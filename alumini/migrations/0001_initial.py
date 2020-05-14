# Generated by Django 3.0.5 on 2020-04-29 05:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('collegename', models.TextField()),
                ('department', models.CharField(choices=[('IT', 'Information Technology'), ('CSE', 'Computer science Engineering'), ('ECE', 'Electronic And Communication Engineering'), ('EEE', 'Electrical And Electronic Engineering'), ('MECH', 'Mechanical Engineering')], max_length=200)),
                ('yearofpassing', models.DateField(default=django.utils.timezone.now)),
                ('companyname', models.TextField()),
                ('currentposition', models.TextField()),
                ('areaofdomain', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contactnumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('url', models.URLField()),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('alumini', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumini.Alumini')),
            ],
        ),
    ]
