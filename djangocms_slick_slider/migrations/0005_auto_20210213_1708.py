# Generated by Django 3.1.6 on 2021-02-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_slick_slider', '0004_auto_20191202_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slicksliderimage',
            options={'ordering': ['position'], 'verbose_name': 'slider image', 'verbose_name_plural': 'slider images'},
        ),
        migrations.AddField(
            model_name='slicksliderimage',
            name='position',
            field=models.IntegerField(default=100, verbose_name='position'),
        ),
    ]