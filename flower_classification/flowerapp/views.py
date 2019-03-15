from django.shortcuts import render

def home(request):
    return render(request, 'flowerapp/home.html', {'title': 'Luan Vasconcelos'})

def prediction(request):
    return render(request, 'flowerapp/flower_prediction.html', {'title': 'Flower Prediction'})
