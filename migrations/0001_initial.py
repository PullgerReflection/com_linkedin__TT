# Generated by Django 4.0.6 on 2022-07-31 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('com_linkedin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkPeople',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('handler', models.CharField(max_length=100)),
                ('sended', models.BooleanField(default=False)),
                ('loaded', models.BooleanField(default=False)),
                ('people', models.ForeignKey(db_column='uuid_people', on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.people', verbose_name='uuid_people')),
            ],
        ),
    ]