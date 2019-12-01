# Generated by Django 3.1 on 2019-11-30 21:39

from django.db import migrations

def create_notifications_survey(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    User = apps.get_model('aggiehub', 'User')
    Post = apps.get_model("aggiehub", "Post")
    Notification = apps.get_model("aggiehub", "Notification")
    Survey = apps.get_model("aggiehub", "Survey")
    notifications = []
    surveys = []
    for user in User.objects.all():
        posts = user.post_set.all()
        all_other_users = User.objects.all().exclude(email__exact = user.email)

        for post in posts:
            if post.score > 0.5:
                notification = Notification(user = user, notif_id = post.id, type = 'Toxic', text = post.text, toxic_words = "shit, die")
                notifications.append(notification)
            
            for other_user in all_other_users:
                survey = Survey(user=other_user, post=post)
                surveys.append(survey)

    Notification.objects.bulk_create(notifications)
    Survey.objects.bulk_create(surveys)         
            

class Migration(migrations.Migration):

    dependencies = [
        ('aggiehub', '0004_auto_20191130_2124'),
    ]

    operations = [
    	migrations.RunPython(create_notifications_survey),
    ]
