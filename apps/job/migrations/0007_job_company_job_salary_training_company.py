# Generated by Django 4.1.9 on 2023-07-27 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_employerdetail_address_employerdetail_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.employerdetail'),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.employerdetail'),
        ),
    ]
