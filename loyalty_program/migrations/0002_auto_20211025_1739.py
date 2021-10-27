# Generated by Django 3.1.8 on 2021-10-25 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loyalty_program', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Profile',
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loyalty_program.profile')),
            ],
        ),
    ]
