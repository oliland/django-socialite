from django.contrib.auth.models import User
import datetime
import base64
import uuid

# Django user functions
def create_django_user(first_name=None, last_name=None, username=None, password=None):
    """
    Allows you to create a django user with a random username
    """
    now = datetime.datetime.now()
    if not username:
        username = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:13]
    user = User(username=username, is_staff=False,
                 is_active=True, is_superuser=False, last_login=now,
                 date_joined=now, first_name=first_name,
                 last_name=last_name)
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
    user.save()
    return user
