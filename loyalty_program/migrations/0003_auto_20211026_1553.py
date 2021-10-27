# Generated by Django 3.1.8 on 2021-10-26 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_program', '0002_auto_20211025_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_brand', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='store',
        ),
        migrations.AddField(
            model_name='discountcode',
            name='follower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loyalty_program.follower'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loyalty_program.brand'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
