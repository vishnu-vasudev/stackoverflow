# Generated by Django 4.0.3 on 2022-07-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_question_vote_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.IntegerField(),
        ),
    ]