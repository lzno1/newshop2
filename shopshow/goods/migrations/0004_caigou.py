# Generated by Django 3.1.3 on 2022-11-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20221120_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaiGou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('goods', models.CharField(blank=True, max_length=20, null=True)),
                ('upMoney', models.CharField(blank=True, max_length=20, null=True)),
                ('PI', models.CharField(blank=True, max_length=20, null=True)),
                ('com', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('num', models.CharField(blank=True, max_length=20, null=True)),
                ('money', models.CharField(blank=True, max_length=20, null=True)),
                ('otherMoney', models.CharField(blank=True, max_length=20, null=True)),
                ('allMoney', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
