from django.forms import ModelForm
from django import forms
from . models import Todo,Category,Profile,Appraisal,Plan
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields= '__all__'
        exclude = ['user']
        widgets = {
            'myCategory':forms.TextInput(
                attrs={'type':'text','id':'myInput','placeholder':'Categories....'}
            )}

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields= '__all__'
        exclude = ['user', 'completed_status']
        widgets = {
            'title':forms.TextInput(
                attrs={'type':'text','id':'myInput','placeholder':'Title....'}
            ),
            'category':forms.Select(
                attrs={'name':'category','id':'id_category'}
            ),
            'description':forms.Textarea(
                attrs={'type':'description','required id':'id_desciption','placeholder':'Description...', 'cols':'30', 'rows':'5'}
            ),
            'decision': forms.Select(
                attrs={'name':'decision','id':'id_decision'}
            )
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
        
        }
    
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields= ['first_name', 'last_name',]
       # exclude = ['password1']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'
        exclude = ('user',)

class AppraisalForm(ModelForm):
    class Meta:
        model = Appraisal
        fields= '__all__'
        #exclude = ['rate']
        widgets = {
             'experience':forms.Textarea(
                attrs={'type':'text','id':'id_experience','placeholder':'....', 'col':'100', 'row':'10'}
            ),
             'thoughts':forms.Textarea(
                 attrs={'type':'text','id':'id_thoughts','placeholder':'....','col':'100', 'row':'10'}
            ),
             'rate':forms.Select(
                 attrs={'name':'Rate'}
            )
            }

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields= '__all__'
        exclude = ['user']
        widgets = {
              'your_plans':forms.Textarea(
                attrs={'type':'text','placeholder':'....', 'col':'100', 'row':'10'}
            ),
             'alternatives':forms.Textarea(
                 attrs={'type':'text','placeholder':'....','col':'100', 'row':'10'}
            ),
            }