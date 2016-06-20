from django.conf.urls import url
from .views import (
        register, index, login, logout, consult, personal_info,
        my_lines, contact, history, my_consults, details_consult,
        unpaid_lines, payment_report, register_line, dar_alta,
        )

# URLs que tendra la app misLineas
urlpatterns = [
        url(r'^$', index, name='index_view'),
        url(r'^register/', register, name='register_view'),
        url(r'^login/$', login, name='login_view'),
        url(r'^logout/$', logout, name='logout_view'),
        url(r'^dar-de-alta/$', dar_alta, name='dar_de_alta_view'),
        url(r'^consults/$', consult, name='consults_view'),
        url(r'^consults/personal-info/$', personal_info,
            name='personal_info_view'),
        url(r'^consults/lines/$', my_lines, name='lines_view'),
        url(r'^consults/contact/$', contact, name='contact_view'),
        url(r'^consults/history/$', history, name='history_view'),
        url(r'^consults/unpaid-lines/$', unpaid_lines,
            name='unpaid_lines_view'),
        url(r'^consults/my-consults/$', my_consults,
            name='my_consults_view'),
        url(r'^consults/my-consults/(?P<pk>[0-9]+)/$', details_consult,
            name='detail_consult_view'),
        url(r'^payment-report/(?P<pk>[0-9]+)/$', payment_report,
            name='payment_report_view'),
        url(r'^register-line/$', register_line, name='register_line_view'),
        ]
