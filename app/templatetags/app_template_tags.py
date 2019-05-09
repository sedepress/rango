from django import template
from app.models import Category

register = template.Library()

@register.inclusion_tag('app/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat': cat}