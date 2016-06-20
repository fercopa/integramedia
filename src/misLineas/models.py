import os
from django.db import models
from django.contrib.auth.models import User


class Linea(models.Model):
    ABONO_MINIMO = 90
    ABONO_MEDIO = 150
    ABONO_MAXIMO = 350
    ECONOMICO = 1
    MEDIO = 2
    ALTO = 3
    PLANES = (
            (ECONOMICO, 'Economico $' + str(ABONO_MINIMO)),
            (MEDIO, 'Normal $' + str(ABONO_MEDIO)),
            (ALTO, 'Premium $' + str(ABONO_MAXIMO)),
            )
    usuario = models.ForeignKey(User, blank=True, null=True)
    numero = models.CharField(max_length=20)
    plan = models.IntegerField(choices=PLANES, default=ECONOMICO,
            blank=True, null=True)
    abono = models.DecimalField(max_digits=6, decimal_places=2,
            blank=True, null=True)
    alta = models.BooleanField(default=True)  # Estado de Alta o Baja
    solicitud_de_alta = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    def set_abono(self, plan):
        """
        Setea el campo abono segun el plan.
        """
        d = dict(self.PLANES)
        precio = d[plan].split('$')[1]
        self.abono = float(precio)

    def get_plan_as_string(self):
        """
        Obtiene el nombre del plan.
        """
        ret = ''
        d = dict(self.PLANES)
        if self.plan:
            plan = d[self.plan].split('$')[0]
            ret = plan.strip()
        return ret

    def get_status(self):
        """
        Muestra el campo alta de una forma legible.
        """
        if self.alta:
            return "De alta"
        else:
            return "Debaja"


class Pago(models.Model):
    RAPIPAGO = 1
    PAGO_FACIL = 2
    LINK = 3
    OTROS = 4
    MEDIOS = (
            (0, 'Seleccionar...'),
            (RAPIPAGO, 'Rapipago'),
            (PAGO_FACIL, 'Pago facil'),
            (LINK, 'Link'),
            (OTROS, 'Otros...'),
            )
    linea = models.ForeignKey(Linea)
    fecha_vencimiento = models.DateField()
    fecha_de_pago = models.DateField(blank=True, null=True)
    medio = models.IntegerField(choices=MEDIOS, default=0, blank=True,
            null=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        d = dict(self.MEDIOS)
        return d[self.medio]


class Contacto(models.Model):
    # Asuntos posibles
    PAGO_REALIZADO = 1
    CAMBIO_ABONO = 2
    ACTUALIZAR_DATO = 3
    OTROS = 4
    ASUNTOS = (
            (PAGO_REALIZADO, 'Pago realizado'),
            (CAMBIO_ABONO, 'Cambio de abono'),
            (ACTUALIZAR_DATO, 'Actualizar datos'),
            (OTROS, 'Otros...'),
            )
    # Medio de comunicacion
    SMS = 1
    EMAIL = 2
    MEDIOS = (
            (SMS, 'Via SMS'),
            (EMAIL, 'Via e-mail'),
            )
    usuario = models.ForeignKey(User)
    asunto = models.IntegerField(choices=ASUNTOS, default=PAGO_REALIZADO)
    medio = models.IntegerField(choices=MEDIOS, default=SMS)
    mensaje = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='uploads/documents/%d-%m-%Y',
            blank=True, null=True)
    contestado = models.BooleanField(default=False)

    def __str__(self):
        d = dict(self.ASUNTOS)
        return d[self.asunto]

    def get_medio(self):
        """
        Muestra el campo medio en forma legible.
        """
        d = dict(self.MEDIOS)
        return d[self.medio]

    def get_file_name(self):
        """
        Defuelve el nombre del documento,
        """
        if self.document:
            name = os.path.basename(self.document.name)
            return name
        else:
            return ''
