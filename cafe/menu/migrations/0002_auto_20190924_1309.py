# Generated by Django 2.2.3 on 2019-09-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burger',
            old_name='price',
            new_name='offer_price',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='burger',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/Burger'),
        ),
        migrations.AddField(
            model_name='burger',
            name='original_price',
            field=models.IntegerField(default=0),
        ),
    ]
