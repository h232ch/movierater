# Generated by Django 4.2.1 on 2023-07-01 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_pub_date_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
