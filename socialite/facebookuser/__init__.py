from oauth_access.access import OAuthAccess
from socialite.users import create_django_user
from django.contrib.auth.models import User

import facebook

class FacebookBackend:

    supports_object_permissions = False
    supports_anonymous_user = False
    
    def authenticate(self, access, auth_token):
        # Ensure that the tokens are valid for this provider
        # Nasty hack to ensure django.contrib.auth.authenticate() works
        if access.service != "facebook":
            raise TypeError
        # Get the user from facebook
        graph = facebook.GraphAPI(auth_token.token)
        profile = graph.get_object("me")
        # Match it with a django user
        user = self.get_user(facebook_id=profile['id'])
        if user:
            # We have an existing association
            return user
        else:
            # Create a new user
            user = create_django_user(first_name=profile['first_name'],
                                last_name=profile['last_name'])
            # And an association
            access.persist(user=user, token=auth_token,
                        identifier=profile['id'])
            return user
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
