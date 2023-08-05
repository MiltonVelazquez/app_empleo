from .models import Usuarios
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

class RegistrarUsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','apellido','dni','fecha_nacimiento','username','password1','password2','email','imagen']
        #error_message para meter errores personalisados en los formularios {'nombre':
        # 'required':'Este campo es requerido'}
        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            return user