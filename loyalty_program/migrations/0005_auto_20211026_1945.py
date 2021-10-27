# Generated by Django 3.1.8 on 2021-10-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_program', '0004_auto_20211026_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountcode',
            name='follower',
        ),
        migrations.AddField(
            model_name='follower',
            name='discount_code_list',
            field=models.ManyToManyField(blank=True, to='loyalty_program.DiscountCode'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='id_user',
            field=models.PositiveIntegerField(default='', editable=False),
        ),
    ]
