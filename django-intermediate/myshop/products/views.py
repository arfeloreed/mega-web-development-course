from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# render homepage
def index(request):
    # query the database to get all the products
    # product_list = Product.objects.all()
    # limiting the number of rendered objects
    product_list = Product.objects.all().order_by("-id")[:4]
    # pass the products to the template context
    context = {
        "products": product_list,
    }
    # render the template and return the response
    return render(
        request,
        "products/home.html",
        context=context,
    )

# render signup page
def signup(request):
    return render(
        request,
        "products/signup.html",
    )


# def product_cat(request, product):
#     product_list = ["suit", "dress", "shirt", "shoes"]
#     if product in product_list:
#         return HttpResponse(f"Here is the list of our {product}.")
#     else:
#         return HttpResponse(f"Sorry, we don't have {product} in our category.")