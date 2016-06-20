from django.contrib import admin
from .models import Linea, Pago, Contacto


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacto
    list_filter = ['contestado']
    list_display = ('asunto', 'medio', 'contestado')


class PagoAdmin(admin.ModelAdmin):
    class Meta:
        model = Pago
    list_display = ('linea', 'fecha_vencimiento', 'fecha_de_pago', 'medio',
            'verificado')
    list_filter = ['verificado']


class LineaAdmin(admin.ModelAdmin):
    class Meta:
        model = Linea
    list_display = ('usuario', 'numero', 'plan', 'abono',
            'solicitud_de_alta', 'alta')
    list_filter = ['alta', 'usuario']


admin.site.register(Linea, LineaAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Contacto, ContactAdmin)
