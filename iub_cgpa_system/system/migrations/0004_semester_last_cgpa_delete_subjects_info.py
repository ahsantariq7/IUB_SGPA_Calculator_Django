# Generated by Django 4.2.5 on 2023-09-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_students_subjects_marks_alter_subjects_info_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_Last_CGPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_semester_cgpa', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Semester_Subjects_Info',
                'verbose_name_plural': "Semester_Subjects_Info's",
            },
        ),
        migrations.DeleteModel(
            name='Subjects_Info',
        ),
    ]
