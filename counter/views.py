from django.shortcuts import render

# API KEY :
#Uk5Vidz/KOqn4xo7mpeMwQ==o9sqdc40eRiy5bkk

# Create your views here.
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'Uk5Vidz/KOqn4xo7mpeMwQ==o9sqdc40eRiy5bkk'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops! No data found"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})