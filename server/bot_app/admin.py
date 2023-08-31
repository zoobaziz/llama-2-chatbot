from django.contrib import admin

# Register your models here.
from .models import TEC_USER as user
from .models import TEC_USER_QUERIES as queries
from .models import TEC_USER_SESSION_WITH_HOSTNAME as sessions


admin.site.register(user)
admin.site.register(queries)
admin.site.register(sessions)