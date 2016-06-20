from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import (
        login as login_user, authenticate, logout as logout_user
        )
from django.contrib.auth.decorators import login_required
from .forms import (
        RegisterForm, LoginForm, ContactForm, HistoryForm, Linea,
        PaymentReportForm, RegisterLineForm, MyLinesForm, DarAltaForm,
        )
from .models import Pago, Contacto


def index(request):
    """
    Vista encargada de la pagina de inicio.
    """
    return render(request, 'index.html')

def register(request):
    """
    Vista encargada del registro de un usuario al sistema MisLineas.
    """
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        messages.success(request, 'Registro exitoso')
        return HttpResponseRedirect('/mislineas/')
    context = {
            'form':form,
            }
    return render(request, 'register.html', context)

def login(request):
    """
    Vista encargada de identificacion al sistema.
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login_user(request, user)
                return HttpResponseRedirect('/mislineas/')
    context = {
            'form':form
            }
    return render(request, 'login.html', context)

@login_required
def logout(request):
    """
    Vista encargada de cerrar sesion del usuario y redirigirlo a la raiz
    """
    logout_user(request)
    messages.info(request, 'Nos vemos pronto.')
    return HttpResponseRedirect('/mislineas/')

@login_required
def dar_alta(request):
    """
    Vista encargada de dar de alta a una linea.
    """
    form = DarAltaForm(request.user, request.POST or None)
    if form.is_valid():
        linea_id = form.cleaned_data['linea']
        linea = Linea.objects.get(id=linea_id)
        linea.solicitud_de_alta = True
        linea.save()
        messages.success(request, 'Solicitud enviada')
        return HttpResponseRedirect('/mislineas/')
    context = {'form':form}
    return render(request, 'dar_alta.html', context)

@login_required
def consult(request):
    """
    Vista encargada de elegir un template para las consultas.
    """
    return render(request, 'consult.html')

@login_required
def personal_info(request):
    """
    Vista encargada de mostrar la informacion personal del usuario.
    """
    user = request.user
    lineas = Linea.objects.filter(usuario=user)
    cantidad_lineas = len(lineas)
    context = {
            'user':user,
            'lineas':lineas,
            'cantidad_lineas':cantidad_lineas
            }
    return render(request, 'personal_info.html', context)

@login_required
def my_lines(request):
    """
    Vista encargada de mostrar las lineas de un usuario.
    """
    form = MyLinesForm(request.user, request.POST or None)
    context = dict()
    if form.is_valid():
        line_id = form.cleaned_data['linea']
        linea = Linea.objects.get(id=line_id)
        context['linea'] = linea
    context['form'] = form
    return render(request, 'my_lines.html', context)

@login_required
def contact(request):
    """
    Vista encargada de contactar a un representante.
    """
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        contacto = form.save(commit=False)
        contacto.usuario = request.user
        contacto.save()
        messages.success(request, "Mensaje enviado.")
    form = ContactForm()
    context = {
            'form':form,
            }
    return render(request, 'contact.html', context)

@login_required
def history(request):
    """
    Vista encargada de ver el historial de pago.
    """
    form = HistoryForm(request.user, request.POST or None)
    context = dict()
    if form.is_valid():
        current_line = Linea.objects.get(id=form.cleaned_data['lineas'])
        pagos = Pago.objects.filter(linea=current_line)
        context['pagos'] = pagos
    context['form'] = form
    return render(request, 'history.html', context)

@login_required
def my_consults(request):
    """
    Vista encargada de mostrar las consultas realizadas por el usuario.
    """
    user = request.user
    consultas = Contacto.objects.filter(usuario=user)
    context = {'consultas':consultas}
    return render(request, 'consults_info.html', context)

@login_required
def details_consult(request, pk):
    """
    Vista encargada de mostrar los detalles de una consulta dada.
    Argumento: id de la consulta
    """
    context = dict()
    try:
        contacto = Contacto.objects.get(id=pk)
        context['contacto'] = contacto
    except:
        return HttpResponseRedirect(request,'/mislineas/')
    return render(request, 'detail_consult.html', context)

@login_required
def unpaid_lines(request):
    """
    Vista encargada de mostrar las lineas que no estan pagadas,
    """
    form = HistoryForm(request.user, request.POST or None)
    lineas = ''
    context = dict()
    if form.is_valid():
        current_line = Linea.objects.get(id=form.cleaned_data['lineas'])
        pagos = Pago.objects.filter(linea=current_line)
        context['pagos'] = [pago for pago in pagos
                if pago.fecha_de_pago is None]
    context['form'] = form
    context['lineas'] = lineas
    return render(request, 'unpaid_lines.html', context)

@login_required
def payment_report(request, pk):
    """
    Vista encargada de reportar un pago.
    Argumento: id del Pago.
    """
    form = PaymentReportForm(request.POST or None)
    try:
        pago = Pago.objects.get(id=pk)
        if pago.medio != 0:
            return HttpResponseRedirect('/mislineas/')
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            medio = form.cleaned_data['medio']
            pago.fecha_de_pago = fecha
            pago.medio = medio
            pago.save()
            messages.success(request, 'Informe enviado')
            return HttpResponseRedirect('/mislineas/')
    except Pago.DoesNotExist:
        return HttpResponseRedirect('/mislineas/')
    context = { 'form':form, }
    return render(request, 'payment_report.html', context)

@login_required
def register_line(request):
    """
    Vista encargada de registrar una linea.
    """
    form = RegisterLineForm(request.POST or None)
    if form.is_valid():
        numero = form.cleaned_data['numero']
        plan = form.cleaned_data['plan']
        linea = Linea.objects.get(numero=numero)
        linea.usuario = request.user
        linea.plan = plan
        linea.set_abono(plan)
        linea.save()
        messages.success(request, 'Se ha registrado correctamente')
        return HttpResponseRedirect('/mislineas/lines/')
    context = {'form':form}
    return render(request, 'register_line.html', context)
