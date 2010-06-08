"""
Enter your API keys and secrets in here.

The quickest way to access them is:
access = OAuthAccess("provider")
access.key
access.secret
"""

OAUTH_ACCESS_SETTINGS = {
'twitter': {
    'keys': {
        'KEY': '#',
        'SECRET': '#',
    },
    'endpoints': {
        'request_token': 'https://twitter.com/oauth/request_token',
        'access_token': 'https://twitter.com/oauth/access_token',
        # Use this url to allow users to 'sign in' with Twitter"
        'authorize': 'https://twitter.com/oauth/authenticate',
        # Use this url if to display a "Connect application dialogue"
        # 'authorize': 'https://twitter.com/oauth/authorize',
        'callback': 'utils.views.success'
    },
},

'facebook': {
    'keys': {
        'KEY': '#',
        'SECRET': '#',
    },
    'endpoints': {
        'request_token': 'https://graph.facebook.com/oauth/request_token',
        'access_token': 'https://graph.facebook.com/oauth/access_token',
        'authorize': 'https://graph.facebook.com/oauth/authorize',
        'callback': 'utils.views.success'
    },
},

'linkedin': {
    'keys': {
        'KEY': '#',
        'SECRET': '#',
    },
    'endpoints': {
        'request_token': 'https://api.linkedin.com/uas/oauth/requestToken',
        'access_token': 'https://api.linkedin.com/uas/oauth/accessToken',
        'authorize': 'https://api.linkedin.com/uas/oauth/authorize',
        'callback': 'utils.views.success'
    },
}

}
