from django.contrib import admin
from .models import Test, Questions, SubmitedAnswer

admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(SubmitedAnswer)

