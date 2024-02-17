from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #! Remove password fields from form
        self.fields.pop('email')
        self.fields.pop('username')
        self.fields.pop('password')

CITY = [
    ('Adana', 'Adana'),
    ('Adıyaman', 'Adıyaman'),
    ('Afyonkarahisar', 'Afyonkarahisar'),
    ('Ağrı', 'Ağrı'),
    ('Amasya', 'Amasya'),
    ('Ankara', 'Ankara'),
    ('Antalya', 'Antalya'),
    ('Artvin', 'Artvin'),
    ('Aydın', 'Aydın'),
    ('Balıkesir', 'Balıkesir'),
    ('Bilecik', 'Bilecik'),
    ('Bingöl', 'Bingöl'),
    ('Bitlis', 'Bitlis'),
    ('Bolu', 'Bolu'),
    ('Burdur', 'Burdur'),
    ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'),
    ('Çankırı', 'Çankırı'),
    ('Çorum', 'Çorum'),
    ('Denizli', 'Denizli'),
    ('Diyarbakır', 'Diyarbakır'),
    ('Edirne', 'Edirne'),
    ('Elazığ', 'Elazığ'),
    ('Erzincan', 'Erzincan'),
    ('Erzurum', 'Erzurum'),
    ('Eskişehir', 'Eskişehir'),
    ('Gaziantep', 'Gaziantep'),
    ('Giresun', 'Giresun'),
    ('Gümüşhane', 'Gümüşhane'),
    ('Hakkari', 'Hakkari'),
    ('Hatay', 'Hatay'),
    ('Isparta', 'Isparta'),
    ('Mersin', 'Mersin'),
    ('İstanbul', 'İstanbul'),
    ('İzmir', 'İzmir'),
    ('Kars', 'Kars'),
    ('Kastamonu', 'Kastamonu'),
    ('Kayseri', 'Kayseri'),
    ('Kırklareli', 'Kırklareli'),
    ('Kırşehir', 'Kırşehir'),
    ('Kocaeli', 'Kocaeli'),
    ('Konya', 'Konya'),
    ('Kütahya', 'Kütahya'),
    ('Malatya', 'Malatya'),
    ('Manisa', 'Manisa'),
    ('Kahramanmaraş', 'Kahramanmaraş'),
    ('Mardin', 'Mardin'),
    ('Muğla', 'Muğla'),
    ('Muş', 'Muş'),
    ('Nevşehir', 'Nevşehir'),
    ('Niğde', 'Niğde'),
    ('Ordu', 'Ordu'),
    ('Rize', 'Rize'),
    ('Sakarya', 'Sakarya'),
    ('Samsun', 'Samsun'),
    ('Siirt', 'Siirt'),
    ('Sinop', 'Sinop'),
    ('Sivas', 'Sivas'),
    ('Tekirdağ', 'Tekirdağ'),
    ('Tokat', 'Tokat'),
    ('Trabzon', 'Trabzon'),
    ('Tunceli', 'Tunceli'),
    ('Şanlıurfa', 'Şanlıurfa'),
    ('Uşak', 'Uşak'),
    ('Van', 'Van'),
    ('Yozgat', 'Yozgat'),
    ('Zonguldak', 'Zonguldak'),
    ('Aksaray', 'Aksaray'),
    ('Bayburt', 'Bayburt'),
    ('Karaman', 'Karaman'),
    ('Kırıkkale', 'Kırıkkale'),
    ('Batman', 'Batman'),
    ('Şırnak', 'Şırnak'),
    ('Bartın', 'Bartın'),
    ('Ardahan', 'Ardahan'),
    ('Iğdır', 'Iğdır'),
    ('Yalova', 'Yalova'),
    ('Karabük', 'Karabük'),
    ('Kilis', 'Kilis'),
    ('Osmaniye', 'Osmaniye'),
    ('Düzce', 'Düzce')
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'image']