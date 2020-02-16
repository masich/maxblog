# Generated by Django 2.2.10 on 2020-02-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200214_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(to='posts.PostAuthor'),
        ),
    ]