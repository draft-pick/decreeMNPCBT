# Generated by Django 4.1.3 on 2022-11-16 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("decree", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="decrees",
            options={
                "ordering": ["-pub_date"],
                "verbose_name": "Приказ",
                "verbose_name_plural": "Приказы",
            },
        ),
        migrations.AddField(
            model_name="decrees",
            name="number",
            field=models.IntegerField(default=1, verbose_name="Номер"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="decrees",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="decree_type",
                to="decree.type",
                verbose_name="Тип документа",
            ),
        ),
    ]
