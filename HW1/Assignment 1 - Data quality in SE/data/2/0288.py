__author__ = 'Che'
from django.contrib import admin
from screenwriter.models import Slug, Action, Dialogue, Character, Screenplay, ScreenplayElements, Parentheses, ScreenplayElementType

class SlugAdmin(admin.ModelAdmin):
            fields = ['slug']
            list_display = ('slug',)


class ActionAdmin(admin.ModelAdmin):
    pass
class DialogueAdmin(admin.ModelAdmin):
    pass
class CharacterAdmin(admin.ModelAdmin):
    pass
class ScreenplayAdmin(admin.ModelAdmin):
    pass
class ScreenplayElementsAdmin(admin.ModelAdmin):
    pass
class ParenthesesAdmin(admin.ModelAdmin):
    pass
class ScreenplayElementTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slug, SlugAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Screenplay, ScreenplayAdmin)
admin.site.register(ScreenplayElements, ScreenplayElementsAdmin)
admin.site.register(Parentheses, ParenthesesAdmin)
admin.site.register(ScreenplayElementType, ScreenplayElementTypeAdmin)
