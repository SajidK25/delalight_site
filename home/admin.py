from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(AboutHome)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(AboutUs)
admin.site.register(Expertise)
admin.site.register(Blog)