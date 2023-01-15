from django.contrib import admin

# Register your models here.
from calorieTracker.myapp.models import Food, Consume

admin.site.register(Food)
admin.site.register(Consume)