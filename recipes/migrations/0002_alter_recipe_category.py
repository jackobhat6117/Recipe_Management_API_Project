# Generated by Django 5.1.1 on 2024-09-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Category',
            field=models.CharField(choices=[('Desert', 'Desert'), ('Main Course', 'Main Course'), ('Breakfast', 'Breakfast'), ('vegertrian', 'vegetrian')], max_length=100),
        ),
    ]
