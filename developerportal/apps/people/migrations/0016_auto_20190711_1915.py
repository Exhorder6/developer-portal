# Generated by Django 2.2.3 on 2019-07-11 19:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('mozimages', '0001_initial'),
        ('people', '0015_auto_20190709_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='intro',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='intro_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='person',
            name='card_description',
            field=models.TextField(blank=True, default='', max_length=140, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='person',
            name='card_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mozimages.MozImage', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='person',
            name='card_title',
            field=models.CharField(blank=True, default='', max_length=140, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_mozillian',
            field=models.BooleanField(default=True, verbose_name='Is Mozillian'),
        ),
        migrations.CreateModel(
            name='PersonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='people.Person')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people_persontag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='keywords',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='people.PersonTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
