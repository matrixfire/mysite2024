# shop/context_processors.py

from .models import Category

def categories(request):
    # Retrieves all categories from the database
    categories = Category.objects.all()
    # Returns a dictionary containing the categories to be added to the context
    return {'categories': categories}
