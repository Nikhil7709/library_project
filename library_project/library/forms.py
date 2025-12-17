from django import forms
from library.models import Author, Book

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'email', 'address']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter author email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter address (optional)'}),
        }

    # Custom validation for name
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError('Name should contain only letters and spaces.')
        return name

    # Custom validation for email uniqueness
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Author.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists. Please use a different email.')
        return email


class BookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Book
        fields = ['title', 'published_date', 'author']
