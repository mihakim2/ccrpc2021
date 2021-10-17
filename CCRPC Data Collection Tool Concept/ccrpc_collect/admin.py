from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as ccrpc_models


admin.site.register(ccrpc_models.DataPointSpot, LeafletGeoAdmin)
