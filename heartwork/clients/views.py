from django.shortcuts import redirect
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.shortcuts import render
from .forms import RegistrationForm, LogInForm
from .models import Client, ClientManager
from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.mail import send_mail


class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    model = Client

    # fields = ['email', 'password','first_name']
    # success_url = '/products'

    # def form_valid(self, form):
    # obj = form.save(commit=False)
    #     obj.set_password(Client.objects.make_random_password())
    #     obj.save()
    #     return redirect('accounts:register-password')

    def post(self, request, *args, **kwargs):
        # http://stackoverflow.com/questions/30610831/form-fields-are-not-shown-in-django-templates-only-submit-button
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            # form.set_password(form.data['[password'])
            email = form.data.get('email')
            password = form.data.get('password')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            client = Client.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            # TODO is this the correct way?
            # client.save(commit=False)
            client.is_active = True
            client.save()
            print(email, password)
            send_mail("Registration url", "please visit", 'heartwork@heartwrok.tk', [email])

            return render(request, "success.html", {'email': client.email})

        else:

            print("UNBOUND FORM", form.errors.as_data())
            args = {}
            # args['form'] = form
            return render(request, 'register.html', {'form': form})
        


class LoginView(FormView):

    template_name = 'login.html'
    # model = Client
    form_class = LogInForm
    success_url = '/products/'

    # @never_cache
    def dispatch(self, request, *args, **kwargs):
        print("running dispatch")
        email = request.POST.get('username')
        password = request.POST.get('password')
        client = authenticate(email=email, password=password)
        if client is not None:
            print 'CLIENT EXISTS'
            login(request, client)
        else:
            "CANNOT FIND CLIENT", email
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print("Running form_valid")
        return super(LoginView, self).form_valid(form)


class ProfileDetailView(DetailView):
    model = Client
    http_method_names = ['get', ]

    def get(self, request, uuid, *args, **kwargs):
        print '---------------', request.user.email, args, kwargs
        print request.user.is_authenticated()
        uuid = None
        try:
            uuid = Client.objects.get(email=request.user.email).profile.profile_url

            return render_to_response('client_profile.html', {uuid: uuid}, context_instance=RequestContext(request))
        except:
            pass

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print("Login required   ")
        print('-----------------', request)
        return super(ProfileDetailView, self).dispatch(request, *args, **kwargs)
