# Generated by Django 3.1 on 2022-12-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='product',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]