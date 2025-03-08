from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib import messages
from django.db.models import Avg

from .forms import ProductCreateForm, ProductUpdateForm
from .models import Product, Rating, RatingAnswer


def index_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'main/index.html', {'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    product_update_form = ProductUpdateForm(instance=product)
    product_comments = Rating.objects.filter(product=product)

    rating_avg = product_comments.aggregate(Avg('count'))['count__avg']

    similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)

    return render(
        request=request,
        template_name='main/product_detail.html',
        context={
            'product': product,
            'similar_products': similar_products,
            'product_update_form': product_update_form,
            'product_comments': product_comments,
            'rating_avg': rating_avg
        })


def product_create_view(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product_object = form.save(commit=False)
            product_object.user = request.user
            product_object.save()

            messages.success(request, 'Успешно создано!')
            return redirect('index')

    form = ProductCreateForm()
    return render(request, 'main/product_create.html', {'form': form})

def product_update_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user != product.user:
        raise Http404

    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлен!')
        else:
            messages.error(request, 'Ошибка при обновлении продукта.')
    return redirect('product_detail', product_id=product.id)

def rating_create_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if  not request.user.is_authenticated:
        messages.error(request, 'Только авторизованные!')
        return redirect('product_detaile', product_id)

    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        count = int(request.POST.get('count', ''))
        rating = Rating(
            user=request.user,
            product=product,
            count=count,
            comment=comment
        )
        rating.save()
        messages.success(request, 'отзыв успешно отправлен!')
        return redirect('product_detail', product_id)

def rating_answer_create_view(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    if rating.product.user != request.user:
        messages.error(request, 'Нет доступа!')
        return redirect('product_detail', rating.product_id)
    if request.method == 'POST':
        comment = request.POST.get('comment', '')

        rating_answer = RatingAnswer(
            user=request.user,
            rating=rating,
            comment=comment
        )

        rating_answer.save()

        messages.success(request, 'Успешно отправлено!')
        return redirect('product_detail', rating.product_id)



















