from mv_test.models import MVProfile

class MVMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            #get or create a profile for this user.
            try:
                profile = request.user.mv_profile
            except MVProfile.DoesNotExist:
                #use profile in session, or create one
                if 'mv_profile_id' in request.session:
                    #this user has just logged in (or registered)
                    profile = MVProfile.objects.get(id = request.session['mv_profile_id'])
                else:
                    profile = MVProfile.objects.new()
                profile.user = request.user
                profile.user_agent = request.META.get('HTTP_USER_AGENT')
                profile.save()
        else:
            #get or create a profile for this visitor
            if 'mv_profile_id' in request.session:
                profile = MVProfile.objects.get(id = request.session['mv_profile_id'])
            else:
                profile = MVProfile.objects.new()
                profile.user_agent = request.META.get('HTTP_USER_AGENT')
                profile.save()
                
        request.mv_profile = profile
        request.session['mv_profile_id'] = profile.id
            
        return None
        
#eof
