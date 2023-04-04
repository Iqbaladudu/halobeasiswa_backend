from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import CountriesToStudy


class StudyAbroadAdmin(ModelAdmin):
    model = CountriesToStudy
    base_url_path = 'negara-tujuan'  # customise the URL from default to admin/bookadmin
    menu_label = 'Negara Tujuan'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'status',)
    list_filter = ('status',)
    search_fields = ('name', 'status')


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(StudyAbroadAdmin)
