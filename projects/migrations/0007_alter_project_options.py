# Generated by Django 4.0.2 on 2022-02-27 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
