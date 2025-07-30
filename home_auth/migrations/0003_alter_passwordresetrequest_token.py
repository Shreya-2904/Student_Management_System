from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ("home_auth", "0002_alter_passwordresetrequest_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordresetrequest",
            name="token",
            field=models.CharField(
                default="AU5n1OZDR4OVYY5cDFHcEajpfo4peUKB",
                editable=False,
                max_length=32,
                unique=True,
            ),
        ),
    ]
