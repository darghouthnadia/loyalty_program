# Generated by Django 3.1.8 on 2021-10-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_program', '0003_auto_20211026_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='id_user',
            field=models.PositiveIntegerField(default='0000000', editable=False),
        ),
    ]
