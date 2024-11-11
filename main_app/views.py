from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    our_services = ["Bush camps", "Balloon Tours", "Hunting", "Village Visits"]
    prices = 10000
    date = '15-11-2024'
    return render(request, 'services.html', {'services': our_services, 'prices': prices, 'date': date})

# display data in our pages
# loops
# if statement ts
# templating engine language

#filters
#images
#static files

