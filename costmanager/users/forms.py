from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from costs.models import Shop

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nume', 'prenume', 'email', 'username',
                  'bio', 'magazine_favorite', 'poza_profil',
                  'social_github', 'social_linkedin', 'social_twitter',
                  'social_instagram']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

