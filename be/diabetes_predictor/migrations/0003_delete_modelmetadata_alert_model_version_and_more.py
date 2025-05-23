# Generated by Django 4.2.10 on 2025-04-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes_predictor', '0002_patient_admission_date_patient_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ModelMetadata',
        ),
        migrations.AddField(
            model_name='alert',
            name='model_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='admission_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
