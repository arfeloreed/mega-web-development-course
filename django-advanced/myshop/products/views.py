from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib import messages
from .models import Product, Feedback
from .forms import FeedbackForm


# Create your views here.
# render homepage
def index(request):
    # query the database to get all the products
    product_list = Product.objects.all()[:4]
    # limiting the number of rendered objects
    # product_list = Product.objects.all().order_by("-id")[:4]
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

# render specific page about a product
def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug=product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(product = product)
    context = {
        "product": product,
        "form": form,
        "reviews": reviews,
    }

    # set variable and render if method == post
    if request.method == "POST":
        form_req = FeedbackForm(request.POST)
        context["form"] = form_req
        if form_req.is_valid():
            feedback = Feedback(
                name = form_req.cleaned_data["name"],
                rating = form_req.cleaned_data["rating"],
                product = product,
                text = form_req.cleaned_data["feedback"],
            )
            feedback.save()
            messages.success(request, "Your form was submitted successfully.")
        
        return render(
            request,
            "products/product.html",
            context=context,
        )

    return render(
        request,
        "products/product.html",
        context=context,
    )


# def product_cat(request, product):
#     product_list = ["suit", "dress", "shirt", "shoes"]
#     if product in product_list:
#         return HttpResponse(f"Here is the list of our {product}.")
#     else:
#         return HttpResponse(f"Sorry, we don't have {product} in our category.")