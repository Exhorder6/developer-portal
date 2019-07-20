# Generated by Django 2.2.3 on 2019-07-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0026_merge_20190704_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='color',
            field=models.CharField(choices=[('pink-40', 'Pink 40%'), ('red-40', 'Red 40%'), ('orange-40', 'Orange 40%'), ('yellow-40', 'Yellow 40%'), ('green-40', 'Green 40%'), ('blue-40', 'Blue 40%'), ('violet-40', 'Violet 40%'), ('purple-40', 'Purple 40%'), ('pink-20', 'Pink 20%'), ('red-20', 'Red 20%'), ('orange-20', 'Orange 20%'), ('yellow-20', 'Yellow 20%'), ('green-20', 'Green 20%'), ('blue-20', 'Blue 20%'), ('violet-20', 'Violet 20%'), ('purple-20', 'Purple 20%')], default='blue-40', max_length=14),
        ),
    ]
