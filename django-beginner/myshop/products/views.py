from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    user = "tom"
    products = 4
    return render(
        request,
        "products/home.html",
        {
            "name": user,
            "product_num": products,
        }
    )

def signup(request):
    return render(
        request,
        "products/signup.html",
    )

def product_cat(request, product):
    product_list = ["suit", "dress", "shirt", "shoes"]
    if product in product_list:
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse(f"Sorry, we don't have {product} in our category.")