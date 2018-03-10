# coding=utf8
from django.shortcuts import render
from Manager.models import Products
from User.models import User
from Goods.models import shoppingCart, orderList, orderDetail
from Utils.UserUtil import *
import time


def home_page(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        # return render(request, 'home_page.html', context)
        pass

    if request.method == 'GET':
        all_goods = Products.objects.all()
        context['goods'] = all_goods
        return render(request, 'home_page.html', context)


def goods_detail(request):
    productID = request.GET.get('id')
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
        # return render(request, 'goods_detail.html', context)
    except:
        # return render(request, 'goods_detail.html', context)
        pass

    try:
        product = Products.objects.get(id=productID)
        context['product'] = product
    except:
        pass

    return render(request, 'goods_detail.html', context)


def goods_list(request):
    context = {}
    if "category" in request.GET:
        category = request.GET.get('category')
        goods = Products.objects.filter(productType=category)

    context['goods'] = goods
    context['category'] = category
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return render(request, 'goods_list.html', context)

    return render(request, 'goods_list.html', context)


def cart(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
        try:
            good_list = []
            totalPrice = 0
            all_shopping = shoppingCart.objects.filter(cusID=user.id)
            for each in all_shopping:
                good = Products.objects.get(id=each.productID)
                good_list.append(good)
                totalPrice = totalPrice + good.price * each.quantity
            context['good_list'] = zip(all_shopping, good_list)
            context['totalPrice'] = totalPrice
        except Exception, e:
            print e
        if user.address:
            context['address'] = user.address
        else:
            context['address'] = ''
        # 创建订单
        if request.method == 'POST':
            totalPrice = request.GET.get('totalPrice')
            address = request.POST.get('address')
            if address == '':
                address = user.address
            localtime = time.localtime(time.time())
            formated_time = time.strftime("%Y-%m-%d", localtime)
            state = "未发货"
            print address, totalPrice

            try:
                new_order = orderList(
                    cusID=user.id,
                    totalPrice=totalPrice,
                    orderTime=formated_time,
                    orderState=state,
                    address=address)
                new_order.save()
            except Exception, e:
                print e

            try:
                all_shopping = shoppingCart.objects.filter(cusID=user.id)
                for each in all_shopping:
                    good = Products.objects.get(id=each.productID)
                    # good_list.append(good)
                    new_order_detail = orderDetail(
                        orderID=new_order.id,
                        productID=good.id,
                        quantity=each.quantity,
                        productName=good.name,
                        pic_url=good.picture.url,
                        username=user.name,
                        buyPrice=good.price * each.quantity,
                    )
                    good.Inventory = good.Inventory - each.quantity
                    good.save()
                    new_order_detail.save()
                    each.delete()
                    context['good_list'] = None
                    context['totalPrice'] = 0.0
            except Exception, e:
                print e

            return HttpResponseRedirect('/Goods/order_success')
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page/')

    return render(request, 'cart.html', context)


def remove_from_cart(request):
    shoppingID = request.GET.get('id')
    try:
        shopping = shoppingCart.objects.get(id=shoppingID)
        shopping.delete()
    except Exception, e:
        print e
    return HttpResponseRedirect('cart.html')


def order_success(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
        return render(request, 'order_success.html', context)
    except:
        return render(request, 'order_success.html', context)





# def order_success(request):
#     context = {}
#     try:
#         username, user = test_cookie(request)
#         context['user'] = user
#         return render(request, 'order_success.html', context)
#     except:
#         return render(request, 'order_success.html', context)


def editInfo(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page/')

    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if address == '':
            address = user.address
        if phone == '':
            phone = user.telephone
        if email == '':
            email = user.email
        try:
            user.address = address
            user.telephone = phone
            user.email = email
            user.save()
            context['success'] = '修改成功'
            context['error'] = '修改失败'
        except Exception, e:
            print e


    return render(request, 'editInfo.html', context)


def order(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
        # return render(request, 'order.html', context)
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page/')

    if 'orderID' in request.GET:
        orderID = request.GET.get('orderID')
        order = orderList.objects.get(id=orderID)
        order.orderState = '订单已完成'
        order.save()
        return HttpResponseRedirect('/Goods/order')

    orderLists = orderList.objects.filter(cusID=user.id).exclude(
        orderState='订单已完成')
    orderDetails = []

    for each in orderLists:
        details = orderDetail.objects.filter(orderID=each.id)
        orderDetails.append(details)
    # 获取已完成订单
    closed_orderLists = orderList.objects.filter(
        cusID=user.id, orderState='订单已完成')
    closed_orderDetails = []

    for each in closed_orderLists:
        details = orderDetail.objects.filter(orderID=each.id)
        closed_orderDetails.append(details)

    context['orders_details'] = zip(orderLists, orderDetails)
    context['closed_orders_details'] = zip(closed_orderLists, closed_orderDetails)

    return render(request, 'order.html', context)


def add_to_cart(request):
    context = {}
    try:
        username, user = test_cookie(request)
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page/')

    cusID = request.GET.get('cusID')
    productID = request.GET.get('productID')
    quantity = request.POST.get('goodsNum')
    print quantity, cusID, productID

    try:
        shopping = shoppingCart.objects.get(cusID=cusID, productID=productID)
        shopping.quantity = shopping.quantity + int(quantity)
        shopping.save()
    except Exception, e:
        print e
        try:
            new_shopping = shoppingCart(
                cusID=cusID, productID=productID, quantity=quantity)
            new_shopping.save()
        except:
            pass

    return render(request, 'add_to_cart.html', context)


def cancel_order(request):
    context = {}
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return HttpResponseRedirect('/User/redirect_to_login_page/')

    orderID = request.GET.get('orderID')

    try:
        order = orderList.objects.get(id=orderID)
        orderdetails = orderDetail.objects.filter(orderID=orderID)
        for item in orderdetails:
            product = Products.objects.get(id=item.productID)
            product.Inventory = product.Inventory + item.quantity
            product.save()

        orderdetails.delete()
        order.delete()
    except Exception, e:
        print e

    return HttpResponseRedirect('order.html', context)


def search(request):
    context = {}
    productName = request.POST.get('searchdata')

    products = Products.objects.filter(name__icontains=productName)

    context['products'] = products
    try:
        username, user = test_cookie(request)
        context['user'] = user
    except:
        return render(request, 'search_list.html', context)
    return render(request, 'search_list.html', context)