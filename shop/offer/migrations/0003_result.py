# Generated by Django 4.2.1 on 2023-06-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_alter_discount_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
