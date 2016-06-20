import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Contacto, Linea, Pago


class RegisterForm(forms.ModelForm):
    """
    formulario para el registro de un usuario.
    """
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User  # Uso el modelo User para crear este formulario
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
                'password': forms.PasswordInput(),
                }

    def clean_confirm_password(self):
        """
        Verifica que las contrasenas coincidan.
        """
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                    "Las contrasenas no coinciden")
        return self.cleaned_data


class LoginForm(forms.Form):
    """
    Formulario para el inicio de sesion.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class DarAltaForm(forms.Form):
    """
    Formulario para dar de alta a una linea.
    Argumento: usuario.
    """
    linea = forms.ChoiceField(choices=())

    def __init__(self, user, *args, **kwargs):
        super(DarAltaForm, self).__init__(*args, **kwargs)
        lines = Linea.objects.filter(usuario=user, alta=False,
                solicitud_de_alta=False)
        LINES = [(line.id, line.numero) for line in lines]
        self.fields['linea'] = forms.ChoiceField(choices=LINES)


class ContactForm(forms.ModelForm):
    """
    Formulario para contactar con un representante.
    """
    class Meta:
        model = Contacto
        fields = ['asunto', 'medio', 'mensaje', 'document']

    def clean(self):
        return self.cleaned_data


class HistoryForm(forms.Form):
    """
    Formulario para ver el historial de una linea.
    Argumento: usuario
    """
    lineas = forms.ChoiceField(choices=())

    def __init__(self, user, *args, **kwargs):
        super(HistoryForm, self).__init__(*args, **kwargs)
        lines = Linea.objects.filter(usuario=user)
        LINES = [(line.id, line.numero) for line in lines]
        self.fields['lineas'] = forms.ChoiceField(choices=LINES)


class PaymentReportForm(forms.Form):
    """
    Formulario para el reporte de un pago.
    """
    fecha = forms.DateField()
    medio = forms.ChoiceField(choices=Pago.MEDIOS)

    def clean_fecha(self):
        """
        Verifica que la fecha ingresada no sea mayor a hoy
        """
        hoy = datetime.date.today()
        fecha = self.cleaned_data['fecha']
        if fecha > hoy:
            raise forms.ValidationError("La fecha es mayor a hoy")
        return fecha

    def clean_medio(self):
        """
        Verifica que se haya seleccionado un medio de pago.
        """
        medio = self.cleaned_data['medio']
        if int(medio) == 0:
            raise forms.ValidationError("Seleccione un medio de pago")
        return medio


class RegisterLineForm(forms.ModelForm):
    """
    Formulario para el registro de una linea.
    """
    class Meta:
        model = Linea
        fields = ['numero', 'plan']

    def clean_numero(self):
        """
        Verifica que el numero exista en la base de datos.
        """
        numero = self.cleaned_data['numero']
        try:
            Linea.objects.get(numero=numero)
        except Linea.DoesNotExist:
            raise forms.ValidationError(
                    "El numero no existe en nuestra base de datos")
        return numero


class MyLinesForm(forms.Form):
    """
    Formulario para ver lineas de un usuario.
    Argumento: usuario.
    """
    linea = forms.ChoiceField(choices=())

    def __init__(self, user, *args, **kwargs):
        super(MyLinesForm, self).__init__(*args, **kwargs)
        lineas = Linea.objects.filter(usuario=user)
        LINEAS = [(line.id, line.numero) for line in lineas]
        self.fields['linea'] = forms.ChoiceField(choices=LINEAS)
