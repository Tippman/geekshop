from django import forms
from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import Category, Product


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['avatar'].required = False


class CategoryAdminCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminCreationForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = 5
        self.fields['title'].widget.attrs['class'] = 'form-control py-4'
        self.fields['description'].widget.attrs['class'] = 'form-control py-4'


class ProductAdminCreationForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'short_description', 'price', 'quantity', 'image', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductAdminCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['title'].widget.attrs['placeholder'] = 'Введите название товара'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите описание товара'
        self.fields['short_description'].widget.attrs['placeholder'] = 'Введите краткое описание товара'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену товара'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество товара на складе'
        self.fields['image'].required = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['class'] = ''
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
