# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db import models
from User.models import User, Manager
from Manager.models import Products
from Goods.models import shoppingCart, orderList, orderDetail
from Utils.UserUtil import *
import time


# Create your views here.
def goods_manager(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        return HttpResponseRedirect('/User/redirect_to_manager_login_page/')

    if request.method == 'GET':
        if request.GET.get('id'):
            try:
                productID = request.GET.get('id')
                product = Products.objects.get(id=productID)
                product.delete()
                shopping = shoppingCart.objects.filter(productID=productID)
                shopping.delete()
            except Exception, e:
                print e
                context['error'] = e
            return HttpResponseRedirect(
                '/Manager/redirect_to_goods_manager_page/')
        else:
            all_goods = Products.objects.all()
            context['goods'] = all_goods
            return render(request, 'goods_manager.html', context)

    if request.method == 'POST':
        if request.POST.has_key('add'):
            name = request.POST.get('name')
            productType = request.POST.get('productType')
            expTime = request.POST.get('expTime')
            info = request.POST.get('info')
            price = request.POST.get('price')
            Inventory = request.POST.get('Inventory')
            picture = request.FILES['picture']
            produceTime = request.POST.get('produceTime')

            if expTime == '':
                expTime = 0

            localtime = time.localtime(time.time())
            formated_time = time.strftime("%Y-%m-%d", localtime)

            try:
                new_product = Products(
                    name=name,
                    productType=productType,
                    expTime=expTime,
                    produceTime=produceTime,
                    price=price,
                    picture=picture,
                    Inventory=Inventory,
                    saleTime=formated_time,
                    info=info)
                new_product.save()
                context['success'] = '添加商品成功'
            except Exception, e:
                print e
                context['error'] = '添加商品失败'

            return HttpResponseRedirect('/Manager/redirect_to_goods_manager_page/', context)

        # if request.POST.has_key('update'):
        #     name = request.POST.get('name')
        #     productType = request.POST.get('productType')
        #     expTime = request.POST.get('expTime')
        #     info = request.POST.get('info')
        #     price = request.POST.get('price')
        #     Inventory = request.POST.get('Inventory')
        #     picture = request.FILES['picture']
        #     produceTime = request.POST.get('produceTime')
        #     product = Products.objects.get(names=name, productType=productType)
        #     if address == '':
        #         address = user.address
        #     if phone == '':
        #         phone = user.telephone
        #     if email == '':
        #         email = user.email
        #     try:

        #         product.delete()
        #     except Exception, e:
        #         print e
        #         context['error'] = e
        #     render(request, 'goods_manager.html', context)


def orders_manage(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        # return render(request, 'orders_manage.html', context)
        return HttpResponseRedirect('/User/redirect_to_manager_login_page/')

    if 'orderID' in request.GET:
        orderID = request.GET.get('orderID')
        order = orderList.objects.get(id=orderID)
        order.orderState = '待确认收货'
        order.save()
        return HttpResponseRedirect('/Manager/orders_manage')

    orderLists = orderList.objects.all()
    orderDetails = []

    for each in orderLists:
        details = orderDetail.objects.filter(orderID=each.id)
        orderDetails.append(details)

    context['orders_details'] = zip(orderLists, orderDetails)

    return render(request, 'orders_manage.html', context)


def manager_info(request):
    context = {}
    try:
        username, manager = manager_test_cookie(request)
        context['manager'] = manager
    except:
        # return render(request, 'orders_manage.html', context)
        return HttpResponseRedirect('/User/redirect_to_manager_login_page/')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == '' or password2 == '':
            context['error'] = '必填项不能为空'
            return render(request, 'manager_info.html', context=context)
        if not password1 == password2:
            context['error'] = '两次输入密码不一致'
            return render(request, 'manager_info.html', context=context)

        try:
            manager.password = password1
            manager.save()
            context['success'] = '修改成功'
            context['error'] = '修改失败'
        except Exception, e:
            print e

    return render(request, 'manager_info.html', context)