import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import MenuItem, Category, OrderModel, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutus.html')


class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')


class Sign_up(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/signup.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = MenuItem.objects.filter(
            category__name__contains='Appetizer')
        fruits = MenuItem.objects.filter(
            category__name__contains='Fruit')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'appetizers': appetizers,
            'fruits': fruits,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'order_foods.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        county = request.POST.get('county')
        eirecode = request.POST.get('eirecode')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            county=county,
            eirecode=eirecode
        )
        order.items.add(*item_ids)

        return redirect('order-confirmation', pk=order.pk)


class OrderPayConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'order_pay_confirmation.html', context)


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')


class PayConfirmationView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name: str = 'order_foods.html'
    context_object_name = 'order_foods'


class DeleteFood(LoginRequiredMixin, DeleteView):
    model = MenuItem
    fields = ['appetizers', 'fruits', 'entres']
    success_url = "/order_foods"
    template_name = 'delete_foods.html'
