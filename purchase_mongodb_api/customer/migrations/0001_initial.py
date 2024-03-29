# Generated by Django 3.2.6 on 2021-08-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('location', models.CharField(choices=[('IND', 'India -- Default'), ('SG', 'Singapore')], default='IND', max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'db_table': 'customer',
            },
        ),
    ]
