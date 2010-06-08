from oauth_access.access import OAuthAccess
from utils.users import create_django_user

import tweepy

class TwitterBackend:
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
        user = self.get_user(screen_name=profile.screen_name)
        if user:
            # We have an existing association
            return user
        else:
            # Create a new user
            # We need to fudge the name in
            if profile.name:
                first_name = profile.name.split()[0]
                try:
                    last_name = profile.name.split()[1]
                except:
                    last_name = None
            else:
                first_name = last_name = None
            user = create_django_user(first_name=first_name,
                                last_name=last_name)
            # And an association
            access.persist(user=user, token=auth_token,
                        identifier=profile.screen_name)
            return user
            
    def get_user(self, screen_name):
        access = OAuthAccess("twitter")
        return access.lookup_user(screen_name)
