from django.contrib import admin
from . models import Feedback

admin.site.site_header = "Swipe2Clean Admin's"

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
