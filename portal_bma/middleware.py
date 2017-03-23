from django.contrib.auth.models import User



class UserMiddleware(object):

    def process_request(self, request):
        user_obj = User.objects.get(username=request.user.username)
        print "---------->",user_obj.date_joined
        print type(user_obj.date_joined)