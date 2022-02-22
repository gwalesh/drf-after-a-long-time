from django.contrib import admin
from .models import Test 
from .models import Question 
from .models import Option 

# Admin Customization 
admin.site.site_header = "Gwalesh's Django App"
admin.site.site_title   = "Gwalesh Django"
admin.site.index_title = "G Django"

# Test
class TestAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Test, TestAdmin)

# Question
class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)

# Option 
class OptionAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Option, OptionAdmin)