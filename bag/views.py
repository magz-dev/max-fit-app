from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page """

    return render (request, 'bag/shopping_bag.html')

