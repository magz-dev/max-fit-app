from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page """

    return render (request, 'bag/shopping_bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity # update item quantity
    else:
        bag[item_id] = quantity # add item quantity

    request.session['bag'] = bag # overrides variable with an updated version
    print(request.session['bag'])
    return redirect(redirect_url)
    