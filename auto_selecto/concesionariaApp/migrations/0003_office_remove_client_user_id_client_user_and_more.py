# Generated by Django 4.2.1 on 2023-06-05 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concesionariaApp', '0002_client_created_at_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('telephone', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_id',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='concesionariaApp.user'),
        ),
        migrations.CreateModel(
            name='OfficeManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=10)),
                ('cedula', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('office', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='concesionariaApp.office')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='concesionariaApp.user')),
            ],
        ),
    ]
