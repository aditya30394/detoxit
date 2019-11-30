# Generated by Django 3.1 on 2019-11-30 21:24

from django.db import migrations
import random

def create_posts(apps, schema_editor):

    db_alias = schema_editor.connection.alias
    User = apps.get_model("aggiehub", "User")
    Post = apps.get_model("aggiehub", "Post")

    for user in User.objects.all():
        name = user.name
        Post.objects.using(db_alias).bulk_create([
            Post(user=user, text=name + "some random comment has been added 1", score=random.uniform(0.0, 0.5)),
            Post(user=user, text=name + "some random comment has been added 2", score=random.uniform(0.0, 0.5)),
            Post(user=user, text=name + "some random comment has been added 3", score=random.uniform(0.0, 0.5)),
            Post(user=user, text=name + "some random comment has been added 4", score=random.uniform(0.5, 1.0)),
            Post(user=user, text=name + "some random comment has been added 5", score=random.uniform(0.5, 1.0)),
            Post(user=user, text=name + "some random comment has been added 6", score=random.uniform(0.5, 1.0)),
        ])

class Migration(migrations.Migration):

    dependencies = [
        ('aggiehub', '0003_auto_20191130_2019'),
    ]

    operations = [
    	migrations.RunPython(create_posts),
    ]