# Generated by Django 4.2 on 2023-05-07 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="profile_pic"),
                ),
                ("location", models.CharField(max_length=50)),
                ("about", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[("IT", "IT"), ("Non IT", "Non IT")], max_length=100
                    ),
                ),
                ("added_date", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                ("about", models.TextField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Manager", "manager"),
                            ("Software Developer", "sd"),
                            ("Project Leader", "pl"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]
