from django.contrib.admin import (
    ModelAdmin,
    register,
)

from ishelf.content.models import (
    Author,
    Book,
)


# region Author

@register(Author)
class AuthorAdmin(ModelAdmin):
    list_filter = ["active"]
    list_display = ["__str__", "active"]
    list_editable = ["active"]


# endregion

# region Book

@register(Book)
class BookAdmin(ModelAdmin):
    list_filter = ["author", "active"]
    list_display = ["__str__", "active"]
    list_editable = ["active"]

# endregion
