from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from . models import Category, Product
from cart.forms import CartAddProductForm
from . recommender import Recommender

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                    translations__language_code = language,
                                    translations__slug=category_slug)
        products = products.filter(category=category)
    
    # Apply pagination
    paginator = Paginator(products, 6)  # Show 6 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'shop/product/list.html', {'category': category,
                                                    'categories': categories, 
                                                    'products':products})

def product_detail(request,id,slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,id=id,translations__language_code = language,
                                translations__slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = Product.objects.order_by('-created')[:4]
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'recommended_products': recommended_products
                                                        })

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created')[:8]
    return render(request, 'shop/home.html', {'categories': categories, 'products': products})

