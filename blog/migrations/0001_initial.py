# Generated by Django 4.1.13 on 2024-11-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]