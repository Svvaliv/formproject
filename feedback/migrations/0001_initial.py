# Generated by Django 4.0.5 on 2022-06-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Имя', max_length=20)),
                ('surname', models.CharField(db_column='Фамилия', max_length=20)),
                ('feedback', models.TextField(db_column='Отзыв')),
                ('rating', models.PositiveIntegerField(db_column='Рейтинг')),
            ],
        ),
    ]
