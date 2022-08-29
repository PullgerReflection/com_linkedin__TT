# Generated by Django 4.0.6 on 2022-08-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_linkedin__TT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkpeople',
            old_name='loaded',
            new_name='executed',
        ),
        migrations.AddField(
            model_name='linkpeople',
            name='discription',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='linkpeople',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]