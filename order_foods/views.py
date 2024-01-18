from .forms import ItemForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import MenuItem, OrderModel, ProfileView
from django.contrib import messages


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutus.html')


class Contact(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            form.save()
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('thank_you')

            else:
                print(form.errors)
                print(form.non_field_errors())


class Thank_You(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'thank_you.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')


class Sign_up(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/signup.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        starters = MenuItem.objects.filter(
            category__name__contains='Starter')
        soups = MenuItem.objects.filter(
            category__name__contains='Soup')
        mains = MenuItem.objects.filter(category__name__contains='Main')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'starters': starters,
            'soups': soups,
            'mains': mains,
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


class Profile_View(View):
    @login_required
    def get(self, request, *args, **kwargs):
        profile_view = ProfileView.objects.all()

        context = {'profile_view': profile_view
                   }

        return render(request, 'profile.html', context)


class Profile_Update(View):
    @login_required
    def get(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ProfileView, user=request.user, id=item_id)
        if request.method == 'POST':
            form = ItemForm(request.POST, instance=item)
            form = form.save()
        form = ItemForm(instance=item)
        context = {
            'form': form
        }
        messages.success(request, f'Your account has been updated!')
        return render(request, 'profile_update.html', context)

    def post(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ProfileView, id=item_id)
        if request.method == 'POST':
            form = ItemForm(request.POST or None,
                            request.FILES or None, instance=item)
            form.save()
        else:
            item = ProfileView()

        return redirect('profile')


class Profile_Create(View):
    @login_required
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ItemForm(request.POST)
            form.save()
        form = ItemForm()
        context = {
            'form': form
        }
        return render(request, 'profile_add.html', context)

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST, request.FILES)
        if request.method == 'POST':

            if form.is_valid():
                form.save()

            return redirect('profile')


class Profile_Delete(View):
    def get(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(ProfileView, user=request.user, id=item_id)
        item.delete()
        return redirect('profile')
