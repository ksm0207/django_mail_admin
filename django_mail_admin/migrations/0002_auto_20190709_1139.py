# Generated by Django 2.2 on 2019-07-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_mail_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailbox',
            name='active',
            field=models.BooleanField(blank=True, default=True, help_text='Check this e-mail inbox for new e-mail messages during polling cycles.  This checkbox does not have an effect upon whether mail is collected here when this mailbox receives mail from a pipe, and does not affect whether e-mail messages can be dispatched from this mailbox. ', verbose_name='Active'),
        ),
    ]
