# Generated by Django 4.1.1 on 2022-10-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andaman& Nicobar Islands', 'Andaman& Nicobar Islands'), ('Goa', 'Goa'), ('Karela', 'Karela'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('West Bengal', 'West Bengal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Haryana', 'Haryana'), ('Punjab', 'Pujab'), ('Manipur', 'Manipur')], max_length=50),
        ),
    ]
