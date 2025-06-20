import requests
from django.shortcuts import render

def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        
        return render(request, 'converter/result.html', {
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': round(converted_amount, 2)
        })
    
    return render(request, 'converter/convert.html')