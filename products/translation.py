from .models import Categories
from modeltranslation.translator import TranslationOptions,register
@register(Categories)
class CategoriesTranslate(TranslationOptions):
    fields = ['name']