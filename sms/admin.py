from django.contrib import admin
from .models import Cordinator, Student, Club, Stream

admin.site.register(Student)
admin.site.register(Stream)
admin.site.register(Cordinator)
admin.site.register(Club)

