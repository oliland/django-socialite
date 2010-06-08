from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth import authenticate, login

def success(request, access, auth_token):

    """
    IMPORTANT!
    This is provided for your reference only.
    You should be writing your own callback views. 8D
    """
    
    user = authenticate(access=access, auth_token=auth_token)
    login(request, user)
        
    return render_to_response('socialauth_success.html', {
    }, context_instance=RequestContext(request))
