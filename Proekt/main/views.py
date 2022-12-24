from django.shortcuts import render, redirect
from pyqiwip2p import QiwiP2P
import random
from .forms import CheckForm
from user_account.models import *
from django.contrib.auth import login, authenticate
from datetime import datetime, timedelta


QIWI_PRIV_KEY="YOUR QIWI API"

let="AaBbCcDdEeFfGg"

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)


def balance(request):
    form = CheckForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'main/balance.html', context)

def balancepay(request):
    error = ''
    form = CheckForm(request.POST)
    amount = form.data.get('amount')
    user = str(request.user)
    comment = user + "_" + amount + "_" + str(random.randint(10000, 99999))
    bill_id=str(random.randint(10000, 99999)) + comment + "_" + str(random.randint(10000, 99999))
    bill = p2p.bill(bill_id=bill_id, amount = amount, lifetime=15, comment=comment)
    CheckPayment(email=user, bill_id=bill_id, comment=comment, amount=amount).save()
    return redirect('balancecheck')

def balancecheck(request):
    user = str(request.user)
    email = CheckPayment.objects.filter(email=user)
    for comment in email:
        comment = comment.comment
    for bill_id in email:
        bill_id = bill_id.bill_id
    for amount in email:
        amount = amount.amount
    try:
        email = email[0]
    except:
        return redirect('home')
    if comment == p2p.check(bill_id).comment:
        status = p2p.check(bill_id).status
        url = p2p.check(bill_id).pay_url
        time = p2p.check(bill_id).expiration
    if status == "PAID":
        email = NewUser.objects.filter(email=user)
        for balance in email:
            balance = balance.balance
        NewUser.objects.filter(balance=balance).update(balance=balance+amount)

    context = {
        'fiel': f"Пополнение баланса на {amount}р.",
        'status': status,
        'url' : url,
        'time': time,
    }
    return render(request, 'main/checkpay.html', context)


def yearpay(request):
    user = str(request.user)
    email = NewUser.objects.filter(email=user)
    for subscribe in email:
        subscribe = subscribe.subscribe
    if subscribe != "PREMIUM":
        comment = user + "_" + "Year" + str(random.randint(10000, 99999))
        bill_id=str(random.randint(10000, 99999)) + comment + "_" + str(random.randint(10000, 99999))
        bill = p2p.bill(bill_id=bill_id, amount = 2400, lifetime=15, comment=comment)
        CheckPayment(email=user, bill_id=bill_id, comment=comment).save()
        return redirect('year')
    else:
        return redirect('home')

def yearcheck(request):
    user = str(request.user)
    email = CheckPayment.objects.filter(email=user)
    for comment in email:
        comment = comment.comment
    for bill_id in email:
        bill_id = bill_id.bill_id
    try:
        email = email[0]
    except:
        return redirect('home')
    if comment == p2p.check(bill_id).comment:
        status = p2p.check(bill_id).status
        url = p2p.check(bill_id).pay_url
        time = p2p.check(bill_id).expiration
    if status == "PAID":
        email = NewUser.objects.filter(email=user)
        for subscribe in email:
            subscribe = subscribe.subscribe
            NewUser.objects.filter(subscribe=subscribe).update(subscribe="PREMIUM")
        for subscribe_date in email:
            subscribe_date = subscribe_date.subscribe_date
        now=datetime.now()
        if subscribe_date>datetime.date(now):
            days = subscribe_date + timedelta(365)
        else:
            days = datetime.now() + timedelta(365)
        NewUser.objects.filter(subscribe_date=subscribe_date).update(subscribe_date=days)

    context = {
        'fiel': "Оплата подписки на 1 год",
        'status': status,
        'url' : url,
        'time': time,
    }
    return render(request, 'main/checkpay.html', context)

def mothpay(request):
    user = str(request.user)
    email = NewUser.objects.filter(email=user)
    for subscribe in email:
        subscribe = subscribe.subscribe
    if subscribe != "BASIC" and subscribe != "PREMIUM":
        comment = user+ "_" + "Moth" + str(random.randint(10000, 99999))
        bill_id=str(random.randint(10000, 99999)) + comment + "_" + str(random.randint(10000, 99999))
        bill = p2p.bill(bill_id=bill_id, amount = 500, lifetime=15, comment=comment)
        CheckPayment(email=user, bill_id=bill_id, comment=comment).save()
        return redirect('moth')
    else:
        return redirect('home')

def mothcheck(request):
    user = str(request.user)
    email = CheckPayment.objects.filter(email=user)
    for comment in email:
        comment = comment.comment
    for bill_id in email:
        bill_id = bill_id.bill_id
    try:
        email = email[0]
    except:
        return redirect('home')
    if comment == p2p.check(bill_id).comment:
        status = p2p.check(bill_id).status
        url = p2p.check(bill_id).pay_url
        time = p2p.check(bill_id).expiration
    if status == "PAID":
        email = NewUser.objects.filter(email=user)
        for subscribe in email:
            subscribe = subscribe.subscribe
            NewUser.objects.filter(subscribe=subscribe).update(subscribe="BASIC")
        for subscribe_date in email:
            subscribe_date = subscribe_date.subscribe_date
        now=datetime.now()
        if subscribe_date>datetime.date(now):
            days = subscribe_date + timedelta(30)
        else:
            days = datetime.now() + timedelta(30)
        NewUser.objects.filter(subscribe_date=subscribe_date).update(subscribe_date=days)


    context = {
        'fiel': "Оплата подписки на 1 месяц",
        'status': status,
        'url' : url,
        'time': time,
    }
    return render(request, 'main/checkpay.html', context)

def reject(request):
    user = str(request.user)
    email = CheckPayment.objects.filter(email=user)
    for comment in email:
        comment = comment.comment
    for bill_id in email:
        bill_id = bill_id.bill_id
    try:
        email = email[0]
    except:
        return redirect('home')
    if comment == p2p.check(bill_id).comment:
        p2p.reject(bill_id)
    return redirect('home')

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def free(request):
    return render(request, 'main/free.html')

def tou(request):
    return render(request, 'main/tou.html')



