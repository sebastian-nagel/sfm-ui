# Generated by Django 2.0.7 on 2018-07-12 17:10

import django.contrib.auth.validators
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0020_auto_20180608_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalcollection',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcollectionset',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcredential',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalseed',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='If blank, will continue until stopped.', null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='harvest_type',
            field=models.CharField(choices=[('twitter_user_timeline', 'Twitter user timeline'), ('twitter_search', 'Twitter search'), ('twitter_filter', 'Twitter filter'), ('twitter_sample', 'Twitter sample'), ('tumblr_blog_posts', 'Tumblr blog posts'), ('flickr_user', 'Flickr user'), ('weibo_timeline', 'Weibo timeline')], max_length=255),
        ),
        migrations.AlterField(
            model_name='collection',
            name='link',
            field=models.CharField(blank=True, max_length=512, verbose_name='Public link'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Collection name'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='schedule_minutes',
            field=models.PositiveIntegerField(choices=[(1, 'One time harvest'), (30, 'Every 30 minutes'), (60, 'Every hour'), (240, 'Every 4 hours'), (720, 'Every 12 hours'), (1440, 'Every day'), (10080, 'Every week'), (40320, 'Every 4 weeks'), (5, 'Every 5 minutes')], default=10080, null=True, verbose_name='schedule'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='visibility',
            field=models.CharField(choices=[('default', 'Group only'), ('local', 'All other users')], default='default', help_text='Who else can view and export from this collection. Select "All other users" to share with all Social Feed Manager users.', max_length=255),
        ),
        migrations.AlterField(
            model_name='collectionset',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Collection set name'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Credential name'),
        ),
        migrations.AlterField(
            model_name='credential',
            name='platform',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('flickr', 'Flickr'), ('weibo', 'Weibo'), ('tumblr', 'Tumblr')], help_text='Platform name', max_length=255),
        ),
        migrations.AlterField(
            model_name='export',
            name='errors',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='export',
            name='export_format',
            field=models.CharField(choices=[('xlsx', 'Excel (XLSX)'), ('csv', 'Comma separated values (CSV)'), ('tsv', 'Tab separated values (TSV)'), ('json_full', 'Full JSON'), ('json', 'JSON of limited fields'), ('dehydrate', 'Text file of identifiers (dehydrate)')], default='xlsx', max_length=10),
        ),
        migrations.AlterField(
            model_name='export',
            name='export_segment_size',
            field=models.BigIntegerField(blank=True, choices=[(100000, '100,000'), (250000, '250,000'), (500000, '500,000'), (100000, '1,000,000'), (None, 'Single file'), (100, '100')], default=250000, null=True),
        ),
        migrations.AlterField(
            model_name='export',
            name='infos',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='export',
            name='status',
            field=models.CharField(choices=[('not requested', 'Not requested'), ('requested', 'Requested'), ('running', 'Running'), ('completed success', 'Success'), ('completed failure', 'Failure')], default='not requested', max_length=20),
        ),
        migrations.AlterField(
            model_name='export',
            name='warnings',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='errors',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='infos',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='status',
            field=models.CharField(choices=[('requested', 'Requested'), ('completed success', 'Success'), ('completed failure', 'Completed with errors'), ('running', 'Running'), ('stop requested', 'Stop requested'), ('stopping', 'Stopping'), ('voided', 'Voided'), ('skipped', 'Skipped'), ('paused', 'Paused')], default='requested', max_length=20),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='token_updates',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='uids',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='warnings',
            field=jsonfield.fields.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='If blank, will continue until stopped.', null=True),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='harvest_type',
            field=models.CharField(choices=[('twitter_user_timeline', 'Twitter user timeline'), ('twitter_search', 'Twitter search'), ('twitter_filter', 'Twitter filter'), ('twitter_sample', 'Twitter sample'), ('tumblr_blog_posts', 'Tumblr blog posts'), ('flickr_user', 'Flickr user'), ('weibo_timeline', 'Weibo timeline')], max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='link',
            field=models.CharField(blank=True, max_length=512, verbose_name='Public link'),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Collection name'),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='schedule_minutes',
            field=models.PositiveIntegerField(choices=[(1, 'One time harvest'), (30, 'Every 30 minutes'), (60, 'Every hour'), (240, 'Every 4 hours'), (720, 'Every 12 hours'), (1440, 'Every day'), (10080, 'Every week'), (40320, 'Every 4 weeks'), (5, 'Every 5 minutes')], default=10080, null=True, verbose_name='schedule'),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='visibility',
            field=models.CharField(choices=[('default', 'Group only'), ('local', 'All other users')], default='default', help_text='Who else can view and export from this collection. Select "All other users" to share with all Social Feed Manager users.', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicalcollectionset',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Collection set name'),
        ),
        migrations.AlterField(
            model_name='historicalcredential',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Credential name'),
        ),
        migrations.AlterField(
            model_name='historicalcredential',
            name='platform',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('flickr', 'Flickr'), ('weibo', 'Weibo'), ('tumblr', 'Tumblr')], help_text='Platform name', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('none', 'None')], default='daily', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='local_id',
            field=models.CharField(blank=True, default='', help_text='Local identifier', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
