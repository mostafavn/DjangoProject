from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# @login_required
def en(request):
    post_list = models.Post.objects.order_by('-pub_date')[:2]
    product_list = models.Product.objects.order_by('-name')

    context = {
    'latest_post_list':post_list,
    'latest_product_list':product_list}

    return render(request, 'en/en.html', context)
