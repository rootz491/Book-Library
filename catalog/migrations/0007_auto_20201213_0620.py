# Generated by Django 3.1.3 on 2020-12-13 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201211_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_edit_book', "edit book's data"))},
        ),
    ]
