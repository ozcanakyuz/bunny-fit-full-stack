# Generated by Django 5.0.1 on 2024-02-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_fiyatlar_odeme_sekli'),
    ]

    operations = [
        migrations.AddField(
            model_name='antrenor',
            name='instagram',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]