# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_category_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='book_files/'),
        ),
    ]
