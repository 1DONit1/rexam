# Generated by Django 2.2.5 on 2019-10-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0003_auto_20191024_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_description',
            field=models.TextField(null=True, verbose_name='Описание экзамена'),
        ),
    ]
