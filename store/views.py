from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .tasks import send_real_sms_task


def product_list_view(request):
    cache_key = 'all_products_cache'

    products = cache.get(cache_key)
    source = "Redis Cache (Tezkor xotira)"

    if not products:
        qs = Product.objects.all().values('id', 'name', 'price', 'stock')
        products = list(qs)

        cache.set(cache_key, products, timeout=900)
        source = "Database - SQL (Ma'lumotlar bazasi)"

    context = {
        'source': source,
        'count': len(products),
        'products': products
    }

    return render(request, 'store/products.html', context)



def trigger_sms_view(request):
    phone = "+998901234567"
    text = "Assalomu alaykum! Sizning buyurtmangiz muvaffaqiyatli qabul qilindi."

    send_real_sms_task.delay(phone, text)

    return JsonResponse({
        "status": "Success",
        "message": "SMS yuborish navbatga qo'shildi va orqa fonda bajarilmoqda!"
    })
