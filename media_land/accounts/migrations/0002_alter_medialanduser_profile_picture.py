# Generated by Django 4.2.3 on 2023-07-31 15:48

from django.db import migrations, models
import media_land.media.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medialanduser',
            name='profile_picture',
            field=models.ImageField(upload_to='media', validators=[media_land.media.validators.validate_file_size]),
        ),
    ]