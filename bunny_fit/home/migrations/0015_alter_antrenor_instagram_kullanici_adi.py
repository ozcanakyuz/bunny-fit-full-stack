# Generated by Django 5.0.1 on 2024-02-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_antrenor_instagram_kullanici_adi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antrenor',
            name='instagram_kullanici_adi',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]