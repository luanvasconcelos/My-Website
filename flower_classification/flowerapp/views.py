from django.shortcuts import render

def home(request):
    data_dict = {
        'title': 'Luan Vasconcelos',
        # 'user_input': Image.Objects.last,
    }
    return render(request, 'flowerapp/home.html', data_dict)

def prediction(request):
    data_dict = {
        'title': 'Flower Prediction',
    }
    return render(request, 'flowerapp/flower_prediction.html', data_dict)
