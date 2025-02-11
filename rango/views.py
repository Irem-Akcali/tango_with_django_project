from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rango.models import Category, Page 

def index(request):
    # Retrieving top 5 most liked categories
    category_list = Category.objects.order_by('-likes')[:5]

    # Retrieving top 5 most viewed pages
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages': page_list
    }
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

# ✅ ADD THIS FUNCTION!
def show_category(request, category_name_slug):
    """View function to display a category and its related pages."""
    context_dict = {}

    try:
        # Fetch category object based on slug
        category = Category.objects.get(slug=category_name_slug)

        # Fetch all pages related to this category
        pages = Page.objects.filter(category=category)

        # Add to context dictionary
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        # If category doesn't exist, set context values to None
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)