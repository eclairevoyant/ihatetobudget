# Generated by Django 3.2.8 on 2021-10-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sheets", "0006_expense_repeat_next_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="expenses"
            ),
        ),
    ]
