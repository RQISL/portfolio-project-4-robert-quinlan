from .forms import (ContactForm, UserUpdateForm,
                    BioUpdateForm, ProfileUpdateForm
                    )
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import MenuItem, OrderModel, Profile
from django.contrib import messages

""" This is Home page view """


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


""" This is About page view """


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutus.html')


""" This is Contact page view """


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


"""
This is response 'Thank you' page view,
when the contact page is sending and turn out
the page to 'Thank you'

"""


class Thank_You(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'thank_you.html')


"""
This is order foods page view,
when you select the food as you like
and fill the detail address for delivery
and send off. It will turn out the page
detail order foods and address, that comes
from order confirmation page.

"""


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
            menu_item = MenuItem.objects.get(pk=int(item))
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


"""
This is order confirmation page. As above
follows the order foods seleted and show up
the price in totals

"""


class OrderPayConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'order_pay_confirmation.html', context)


"""
This is Profile page and included CRUD.
When you click to 'Add & Edit' and drop down
the form, you can fill the profile and image upload
after clcik the 'Update'

There is popup screen as 'Warning' because
The user change username and it will effect
in the database changed. It explained to user
to make sure rememeber when the username is changed.

"""


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        b_form = BioUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and b_form.is_valid() and p_form.is_valid():
            u_form.save()
            b_form.save()
            p_form.save()
            messages.success(request, f'{"Your account has been updated!"}')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        b_form = BioUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'b_form': b_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


"""
This is delete button in Profile page.
It will be empty image and profile detail.
You can fill it again through 'Add & Edit'
update again. The username will be remain
same as display on the profile page.

"""


@login_required
def profile_delete(request):
    item = get_object_or_404(Profile, user=request.user)
    if item.user == request.user:
        item.delete()
    return redirect('/')
