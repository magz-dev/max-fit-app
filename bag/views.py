from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Coupon
from products.models import Product
from .forms import FormCoupon




def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()}'
                                  f'{product.name} quantity to'
                                  f'{bag[item_id]["items_by_size"][size]}'))
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your bag'))
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your bag'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name}'
                              f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

@login_required
@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    # View to check code entered against codes in the coupon model
    code = request.POST.get('coupon-code')

    # Checking for blank coupon submissions
    if not code:
        messages.error(request, "You didn't enter a coupon code!")
        return redirect(reverse('view_bag'))

    try:
        coupon = Coupon.objects.get(code=code)
        request.session['coupon_id'] = coupon.id
        messages.success(request, f'Coupon code: { code } applied')
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        messages.warning(request, f'Coupon code: { code } not accepted')
        return redirect('view_bag')
    else:
        return redirect('view_bag')


@login_required
def coupons_manage(request):
    # View to allow admins to see the manage coupons page
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins have permission to manage\
            coupons.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        coupon_form = FormCoupon(request.POST)

        # Check if the coupon form is valid and display appropriate message
        if coupon_form.is_valid():
            form_data = coupon_form.save(commit=False)
            form_data.code = form_data.code.upper()
            form_data.save()
            messages.success(request, 'Coupon added successfully!')
            return redirect('coupons_manage')
        else:
            messages.error(request, 'Unable to add coupon, please check your \
                form information is correct.')
            return redirect('coupons_manage')
    else:
        coupon_form = FormCoupon()

    coupon_form = FormCoupon()
    coupons = Coupon.objects.all()
    context = {
        'coupons': coupons,
        'coupon_form': coupon_form,
    }

    return render(request, 'bag/coupons_manage.html', context)


@login_required
def coupon_delete(request, coupon_id):
    # View to allow admins to delete coupons
    if not request.user.is_superuser:
        messages.error(request, 'Only admins have permission to delete\
            coupons.')
        return redirect(reverse('index'))

    coupon = get_object_or_404(Coupon, pk=coupon_id)
    coupon.delete()
    messages.success(request, 'Coupon deleted successfully!')
    return redirect(reverse('coupons_manage'))


@login_required
def coupon_delete_confirmation(request, coupon_id):
    # Retrieve the coupon
    coupon = get_object_or_404(Coupon, pk=coupon_id)

    if request.method == 'POST':
        # Delete the coupon
        coupon.delete()
        messages.success(request, 'Coupon deleted successfully!')
        return redirect('coupons_manage')

    return render(request, 'bag/coupon_delete_confirmation.html', {'coupon': coupon})
