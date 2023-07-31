from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, login
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth import get_user_model
from django.templatetags.static import static

UserModel = get_user_model()


class RegisterUserView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        request = self.request
        login(request, user)

        return result


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(generic.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_picture = static('images/incognito.png')
        if self.object.profile_picture is not None:
            profile_picture = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        context['profile_picture'] = profile_picture
        context['media'] = self.request.user.media_set.all()

        return context


class EditProfileView(generic.UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = UserModel
    fields = '__all__'
    success_url = 'accounts/profile-details.html'


class DeleteProfileView(generic.DeleteView):
    template_name = 'accounts/delete-profile.html'
    model = UserModel
    success_url = 'common/index.html'


def shopping_cart(request, pk):
    context = {
        'user_pk': pk,
    }
    return render(request, template_name='accounts/shopping-cart.html', context=context)
