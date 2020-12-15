# Generated by Django 3.0.9 on 2020-12-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('catagory', models.CharField(choices=[('A', 'Food'), ('B', 'Clothing'), ('C', 'Housing'), ('D', 'Education'), ('E', 'Entertainment'), ('F', 'Other')], max_length=8)),
                ('projected', models.PositiveIntegerField(default=0)),
                ('actual', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
