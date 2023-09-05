# Generated by Django 4.2.3 on 2023-09-04 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(to='classes.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='images/lessons/', verbose_name='preview'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField(verbose_name='date of payment')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='payment amount')),
                ('type_of_payment', models.CharField(choices=[('Cash', 'Cash'), ('Transfer to account', 'Transfer to account')], max_length=100, verbose_name='type of payment')),
                ('course_paid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.course', verbose_name='course paid')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'ordering': ('user',),
            },
        ),
    ]
