# Generated by Django 4.1 on 2022-08-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_alter_farmblock_block_id_alter_farmblock_block_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmblock',
            name='block_name',
            field=models.CharField(default='14vdwp4cht', max_length=10),
        ),
    ]
