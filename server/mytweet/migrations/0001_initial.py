# Generated by Django 4.0.4 on 2022-05-19 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=280, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='./image')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_retweet', models.BooleanField(default=False)),
                ('is_reply', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='tweetLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('tweet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mytweet.tweet')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='like',
            field=models.ManyToManyField(related_name='tweetLike', through='mytweet.tweetLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mytweet.tweet'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
