# Generated by Django 3.2.5 on 2021-08-05 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0017_alter_changelog_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruleset',
            old_name='github_link',
            new_name='source',
        ),
    ]
