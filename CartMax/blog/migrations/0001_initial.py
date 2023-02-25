# Generated by Django 4.0.2 on 2022-04-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogposts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Head0', models.CharField(default='', max_length=500)),
                ('Chead0', models.CharField(default='', max_length=5000)),
                ('Head1', models.CharField(default='', max_length=500)),
                ('Chead1', models.CharField(default='', max_length=5000)),
                ('Head2', models.CharField(default='', max_length=500)),
                ('Chead2', models.CharField(default='', max_length=5000)),
                ('Pub_date', models.DateField()),
                ('Thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]