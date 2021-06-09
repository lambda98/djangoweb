# Generated by Django 2.2 on 2019-07-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_auto_20190710_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('questions', 'Questtions'), ('problems', 'Problems'), ('other', 'Other')], default='questions', max_length=50)),
                ('title', models.CharField(max_length=120)),
                ('detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]