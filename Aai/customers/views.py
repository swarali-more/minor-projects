# Customer detail page handles photo, status and blouse uploads
from django.shortcuts import render, redirect
from .models import Customer, Blouse

def home(request):
    return render(request, 'home.html')

def add_customer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')
        received_date = request.POST.get('received_date')
        delivery_date = request.POST.get('delivery_date')

        customer = Customer.objects.create(
            name=name,
            phone=phone,
            photo=photo,
            received_date=received_date,
            delivery_date=delivery_date
        )

        return redirect('customer_detail', id=customer.id)

    return render(request, 'add_customer.html')

def old_customers(request):
    search_query = request.GET.get('search')

    if search_query:
        customers = Customer.objects.filter(name__icontains=search_query)
    else:
        customers = Customer.objects.all()

    return render(request, 'old_customers.html', {
        'customers': customers,
        'search_query': search_query
    })

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == "POST":

        # Save Note
        if request.POST.get('note') is not None:
            customer.note = request.POST.get('note')

        if request.FILES.get('photo'):
            customer.photo = request.FILES.get('photo')
            customer.save()

        # Save Dates
        if request.POST.get('received_date'):
            customer.received_date = request.POST.get('received_date')

        if request.POST.get('delivery_date'):
            customer.delivery_date = request.POST.get('delivery_date')

        # Save Blouse Image
        if request.FILES.get('blouse_image'):
            Blouse.objects.create(
                customer=customer,
                image=request.FILES.get('blouse_image')
            )

        if request.POST.get('status'):
            customer.status = request.POST.get('status')
            customer.save()

        # Final Save
        customer.save()

    return render(request, 'customer_detail.html', {'customer': customer})

def delete_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('old_customers')

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == "POST":
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customer_detail', id=customer.id)

    return render(request, 'edit_customer.html', {'customer': customer})