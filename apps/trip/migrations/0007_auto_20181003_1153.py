# Generated by Django 2.1.2 on 2018-10-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_remove_reviewresponse_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewresponse',
            name='response',
            field=models.TextField(max_length=200),
        ),
    ]
