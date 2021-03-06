# Generated by Django 3.0 on 2020-04-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('postTitle', models.CharField(max_length=255)),
                ('postContent', models.TextField()),
                ('postAuthor', models.CharField(max_length=100)),
                ('postLanguage', models.CharField(choices=[('HI', 'Hindi'), ('MA', 'Marathi')], default='MA', max_length=2)),
                ('postType', models.CharField(choices=[('PG', 'Poems & Gazals'), ('ST', 'Short Stories')], default='PG', max_length=2)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
