# Generated by Django 4.2.1 on 2023-06-26 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concesionariaApp', '0005_companyposition'),
        ('users', '0006_rename_company_position_staffmember_company_position_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmember',
            name='company_position_id',
        ),
        migrations.AddField(
            model_name='staffmember',
            name='company_position',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='concesionariaApp.companyposition'),
            preserve_default=False,
        ),
    ]
