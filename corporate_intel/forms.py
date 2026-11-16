from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'corporate_intel/login.html'
    redirect_authenticated_user = True
