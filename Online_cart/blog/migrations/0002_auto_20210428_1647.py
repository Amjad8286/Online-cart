# Generated by Django 3.1.7 on 2021-04-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead0',
            new_name='content_head0',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead1',
            new_name='content_head1',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead2',
            new_name='content_head2',
        ),
    ]
