from django import template


register = template.Library()

@register.filter(name='pages')
def pages(list_data,page_size):
    page = []
    i = []
    for data in list_data:
        page.append(data)
        i = i+1
        if i==page_size:
            yield page
            i = 0
            page = []
    

    yield page