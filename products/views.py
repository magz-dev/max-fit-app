from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, UserProfile, Review 
from .forms import ProductForm, ReviewForm


# Create your views here.

def all_products(request):
    """ 
    View to show all products, including sorting and search queries 
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Handling sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handling category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handling search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    View to show individual product details 
    """
    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    reviews = product.reviews.all().order_by('-created_at')
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ 
    Add a product to the store 
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Edit a product in the store 
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ 
    Delete a product from the store 
    """
    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name 
    product.delete()
    messages.success(request, f'{product_name} deleted')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        product = get_object_or_404(Product, pk=product_id)
        if form.is_valid():
            review = form.save(commit=False)
            profile = UserProfile.objects.get(user=request.user)
            review.profile = profile
            review.product = product
            review.save()
            messages.success(request, 'Review Added Successfully')
        else:
            messages.error(request, 'Failed to add your review. Please check the form.')

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_review(request, product_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def edit_review(request, product_id, review_id):
    """
    View to edit review
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated your review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update your review! Please try again.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'You are editing your review!')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product_id': product_id
    }
    return render(request, template, context)
