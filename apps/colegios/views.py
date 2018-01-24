from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView

from apps.colegios.models import Colegio


class ColegioListView(ListView):
    template_name = 'colegios/list.html'
    model = Colegio
    context_object_name = 'colegios'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            qs = Colegio.objects.filter(Q(codigo_modular=q) | Q(codigo_colegio=q))
        else:
            qs = Colegio.objects.none()
            messages.warning(self.request, 'Ingrese el código a buscar')
        if not qs:
            messages.warning(self.request, 'No se encontraron coincidencias')
        return qs
