# Generated by Django 4.2.3 on 2023-07-05 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
