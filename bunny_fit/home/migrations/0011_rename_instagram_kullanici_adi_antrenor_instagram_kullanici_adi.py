# Generated by Django 5.0.1 on 2024-02-17 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_instagram_antrenor_instagram_kullanici_adi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antrenor',
            old_name='instagram_Kullanici_Adi',
            new_name='instagram_kullanici_adi',
        ),
    ]
