from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse
from django.apps import apps

UserProfile = apps.get_model('login', 'UserProfile')

# Create your views here.


def index(request):
    try:
        selected_choice = request.POST['Tutor']
    except Exception as e:
        # Redisplay the question voting form.
        print(e)
        return render(request, 'login/is_tutor.html', {
            'error_message': "Empty text fields",
        })
    else:
        if selected_choice == "True":
            return HttpResponse("Tutor")
        else:
            user_list = UserProfile.objects.all()
            output = ', '.join([q.user.username for q in user_list])
            return HttpResponse(output)


# Gets online users
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

