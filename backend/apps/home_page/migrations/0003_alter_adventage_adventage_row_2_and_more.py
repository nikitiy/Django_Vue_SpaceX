# Generated by Django 4.2.5 on 2023-09-17 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_alter_adventage_adventage_row_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventage',
            name='adventage_row_2',
            field=models.CharField(help_text='ТЕКСТ <sраn>текст<span>', max_length=32, verbose_name='Строка 2'),
        ),
        migrations.AlterField(
            model_name='adventage',
            name='adventage_row_3',
            field=models.CharField(max_length=32, verbose_name='Строка 3'),
        ),
    ]
