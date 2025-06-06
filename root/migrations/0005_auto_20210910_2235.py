# Generated by Django 3.2.7 on 2021-09-10 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0004_auto_20210906_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxSpin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spin', models.IntegerField(verbose_name='عدد اللفات')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.box', verbose_name='الصندوق')),
            ],
            options={
                'verbose_name': 'BoxSpin',
                'verbose_name_plural': 'BoxSpins',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50, verbose_name='الرسالة')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxes_spin', models.ManyToManyField(through='root.BoxSpin', to='root.Box', verbose_name='لفات الصناديق')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اللاعب')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_numbers', models.IntegerField(verbose_name='عدد مرات الفوز')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.box', verbose_name='الصندوق')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.player', verbose_name='اللاعب')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.product', verbose_name='الجائزة')),
            ],
            options={
                'verbose_name': 'Prize',
                'verbose_name_plural': 'Prizes',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='prizes',
            field=models.ManyToManyField(through='root.Prize', to='root.Product', verbose_name='الجوائز'),
        ),
        migrations.AddField(
            model_name='boxspin',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.player', verbose_name='اللاعب'),
        ),
    ]
