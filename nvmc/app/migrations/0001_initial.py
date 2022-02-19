# Generated by Django 4.0.2 on 2022-02-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nvmc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radios', models.CharField(max_length=30, verbose_name='選択')),
                ('facility', models.CharField(max_length=30, verbose_name='設備')),
                ('facNo', models.CharField(max_length=10, verbose_name='号機No')),
                ('lot_id', models.CharField(max_length=20, verbose_name='ロットID')),
                ('eqname', models.CharField(max_length=20, verbose_name='装置名')),
                ('brname', models.CharField(max_length=20, verbose_name='品種名')),
                ('description', models.TextField(blank=True, verbose_name='故障現象')),
            ],
        ),
    ]