from django.shortcuts import get_object_or_404, redirect, render
from .models import *
import random
# Create your views here.


def index(request):
    cars = list(Cars.objects.all())  # Convert queryset to a list
    random.shuffle(cars)  # Shuffle the list randomly
    cars = cars[:10]  # Take the first 20 cars
    slides = Slides.objects.all()
    services = Services.objects.all()
    staff = Staff.objects.all()
    testimonials = Testimonials.objects.all()
    context = {
        'cars': cars,
        'slides': slides,
        'services': services,
        'staff': staff,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)

def aboutus(request):
    testimonials = Testimonials.objects.all()
    context = {
    'testimonials':testimonials,

    }
    return render(request, 'about.html',context)
def success_page(request, car_name=None, car_model=None):
    return render(request, 'success.html', {'car_name': car_name, 'car_model': car_model})

def booking(request, car_id):
    car1 = get_object_or_404(Cars, id=car_id)
    context = {
        'car1':car1
    }
    if request.method == 'POST':
        customer_name = request.POST.get('names')
        phone_number = request.POST.get('phonenumber')
        pickup_date = request.POST.get('pickup_date')  
        return_date = request.POST.get('return_date')
        
        # Get the car object based on the car_id
        car = get_object_or_404(Cars, id=car_id)

        booking = Booking.objects.create(
            car=car,
            customer_name=customer_name,
            phone_number=phone_number,
            pickup_date=pickup_date,
            return_date=return_date,
        )
        booking.save()

        # Redirect to success page and pass the car name as a parameter
        return redirect('success_page', car_name=car.name, car_model=car.model)
    return render(request, 'booking.html',context)
def cars(request):
    cars = Cars.objects.all
    context = {
        'cars':cars
    }
    return render(request, 'car.html',context)

def detail(request,car_id):
    car = get_object_or_404(Cars, id=car_id)
    cars_images = car.carimages_set.all()

    current_car = Cars.objects.get(pk=car_id)

    similar_cars = Cars.objects.filter(enginetype=current_car.enginetype).exclude(pk=current_car.id)[:20]

    context = {
        'car':car,
        'similar_cars':similar_cars,
        'cars_images':cars_images,  
    }
    return render(request, 'detail.html',context)

def contact(request):
    context = {

    }
    return render(request, 'contact.html',context)
def service(request):
    context = {

    }
    return render(request, 'contact.html',context)
def fuel(request):
    testimonials = Testimonials.objects.all()
    context = {
    'testimonials':testimonials,

    }
    return render(request, 'fuel.html',context)
def track(request):
    context = {

    }
    return render(request, 'track.html',context)

def trackStatus(request):
    context = {

    }
    return render(request, 'track-status.html',context)

def shipping(request):
    if request.method == 'POST':
        customer_name = request.POST.get('names')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')  
        location = request.POST.get('location')
        destination = request.POST.get('destination')
        cargo = request.POST.get('cargo')
        
        shipping = Cargo.objects.create(
            customer_name=customer_name,
            phone_number=phone_number,
            email=email,
            location=location,
            destination=destination,
            cargo=cargo,
        )
        shipping.save()

        # Redirect to success page and pass the car name as a parameter
        return redirect('success_shipping',customer_name=customer_name,phone_number=phone_number,email=email,)

    context = {

    }
    return render(request, 'shipping.html',context)

def success_shipping(request,customer_name, phone_number, email,):
    context = {
    'customer_name': customer_name,
    'phone_number': phone_number,
    'email': email,
    }
    return render(request, 'success_shipping.html', context)
