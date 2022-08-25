# Generated by Django 3.2.7 on 2021-09-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0010_auto_20210910_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='boxes_spin',
            field=models.ManyToManyField(blank=True, through='root.BoxSpin', to='root.Box', verbose_name='لفات الصناديق'),
        ),
        migrations.AlterField(
            model_name='player',
            name='prizes',
            field=models.ManyToManyField(blank=True, through='root.Prize', to='root.Product', verbose_name='الجوائز'),
        ),
    ]
