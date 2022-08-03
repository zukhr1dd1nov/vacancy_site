from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryModel, VacancyModel

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class VacancyTranslationOptions(TranslationOptions):
    fields = ('name', 'body')

translator.register(CategoryModel, CategoryTranslationOptions)
translator.register(VacancyModel, VacancyTranslationOptions)