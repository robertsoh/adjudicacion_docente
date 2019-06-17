Instalación
===========

- Configuración dentro de Django: `settings/base.py`

* `DB_NAME` nombre de la base de datos
* `DB_USER` usuario de la base de datos
* `DB_HOST` servidor de base de datos
* `DB_PORT` puerto de la base de datos
* `SECRET_KEY` Secret Key de Django

- Cargar data:

```
    python manage.py loaddata loaddata apps/colegios/fixtures/colegios.json
```
