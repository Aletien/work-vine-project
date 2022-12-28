from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        item_title = request.POST['item_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        town = request.POST['town']
        city = request.POST['city']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        comments = request.POST.get('comments')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(item_id=item_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already submitted an inquiry on this particular Item, please wait until we get back to you. Thanks!')
                return redirect('/store/'+item_id)

        contact = Contact(item_id=item_id, item_title=item_title,  user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, town=town, city=city, email=email, phone_number=phone_number, comments=comments)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New Item Inquiry',
            'You have a new inquiry for an Item ' + item_title + '. Please login to your admin panel for more info.' ,
            'dummyallan1@gmail.com',
            [admin_email],
            fail_silently=False,

        )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/store/'+item_id)
