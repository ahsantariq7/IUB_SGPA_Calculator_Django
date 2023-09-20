# Generated by Django 4.2.5 on 2023-09-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_1', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_2', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_3', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_4', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_5', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_6', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_7', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_8', models.IntegerField(blank=True, default=0, null=True)),
                ('semester_9', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='semester_info',
            options={'verbose_name': 'Semester_Info', 'verbose_name_plural': "Semester_Info's"},
        ),
        migrations.AddField(
            model_name='semester_info',
            name='email',
            field=models.EmailField(default='ahsantariq0724@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='semester_info',
            name='name',
            field=models.CharField(default='mame', max_length=80),
        ),
        migrations.AddField(
            model_name='semester_info',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='semester_info',
            name='roll_no',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='semester_info',
            name='semester',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=1),
        ),
    ]