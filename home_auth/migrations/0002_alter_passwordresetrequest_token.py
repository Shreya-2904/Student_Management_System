from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ("home_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordresetrequest",
            name="token",
            field=models.CharField(
                default="At3lTeUF9mCQsJbiqaPbdXyd6Aisl2Vd",
                editable=False,
                max_length=32,
                unique=True,
            ),
        ),
    ]
