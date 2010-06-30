from oauth_access.access import OAuthAccess
from socialite.users import create_django_user
from django.contrib.auth.models import User

import tweepy

class TwitterBackend:

    supports_object_permissions = False
    supports_anonymous_user = True

    def authenticate(self, access, auth_token):
        # Ensure that the tokens are valid for this provider
        # Nasty hack to ensure django.contrib.auth.authenticate() works
        if access.service != "twitter":
            raise TypeError
        # Get the user from Twitter
        auth = tweepy.OAuthHandler(access.key, access.secret)
        auth.set_access_token(auth_token.key, auth_token.secret)
        api = tweepy.API(auth)
        profile = api.me()
        # Match it with a django user
        user = access.lookup_user(identifier=profile.id)
        if not user:
            # Create a new user
            # We need to fudge the name in
            if profile.name:
                first_name = profile.name.split()[0]
                try:
                    last_name = profile.name.split()[1]
                except:
                    last_name = ""
            else:
                first_name = last_name = ""
            user = create_django_user(first_name=first_name,
                                last_name=last_name)
        # Persist the association
        access.persist(user=user, token=auth_token,
                        identifier=profile.id)
        return user
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
