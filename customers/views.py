from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer

# Create your views here.

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request,'customers/customer_list.html',{'customers': customers})


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

@login_required
def customer_create(request):
    """
    View to add new customer.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        vat_id = request.POST.get('vat_id')
        street = request.POST.get('street')
        city = request.POST.get('city')
        country = request.POST.get('country')

        if name and vat_id and street and city and country:
            customer = Customer.objects.create(name=name, vat_id=vat_id, street=street,city=city,country=country)
            return redirect('customer_list')
        return render(request, 'customers/customer_create_form.html', {'error': 'All fields are required.'})

    return render(request, 'customers/customer_create_form.html')

@login_required
def customer_update(request, pk):
    """
    View to update an existing Customer data.
    """
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name', customer.name)
        customer.vat_id = request.POST.get('vat_id', customer.vat_id)
        customer.street = request.POST.get('street', customer.street)
        customer.city = request.POST.get('city', customer.city)
        customer.country = request.POST.get('country', customer.country)
        customer.save()
        return redirect('customer_list')

    return render(request, 'customers/customer_edit_form.html', {'customer': customer})