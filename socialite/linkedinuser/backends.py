from oauth_access.access import OAuthAccess
from socialite.users import create_django_user

from linkedin import linkedin

class LinkedInBackend:
    def authenticate(self, access, auth_token):
        # Ensure that the tokens are valid for this provider
        # Nasty hack to ensure django.contrib.auth.authenticate() works
        if access.service != "linkedin":
            raise TypeError
        # Get the user from Linkedin
        api = linkedin.LinkedIn(access.key, access.secret, "")
        api.access_token, api.access_token_secret = auth_token.key, auth_token.secret
        profile = api.GetProfile(None,None,'id','first-name','last-name')
        # Match it with a django user
        user = self.get_user(linkedin_id=profile.id)
        if user:
            # We have an existing association
            return user
        else:
            user = create_django_user(first_name=profile.first_name,
                                last_name=profile.last_name)
            # And an association
            access.persist(user=user, token=auth_token,
                        identifier=profile.id)
            return user
            
    def get_user(self, linkedin_id):
        access = OAuthAccess("linkedin")
        return access.lookup_user(linkedin_id)
