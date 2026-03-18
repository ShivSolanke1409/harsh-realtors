from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Enquiry

def home(request):
    properties = Property.objects.all().order_by('-created_at')
    return render(request, 'home.html', {
        'properties': properties
    })


def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})


def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        requirement = request.POST.get('requirement')

        Enquiry.objects.create(
            name=name,
            phone=phone,
            requirement=requirement
        )

        return redirect('home')

    return redirect('home')

def enquiry_view(request):
    return render(request, 'enquiry.html')
