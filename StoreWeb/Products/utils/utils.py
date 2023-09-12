# api_data/utils.py
import requests
from ..models import Category
#from .models import Product

def fetch_and_save_data():
    api_url_prod = "https://api.escuelajs.co/api/v1/products"
    api_url_cate = "https://api.escuelajs.co/api/v1/categories"
    response = requests.get(api_url_prod)
    response2 = requests.get(api_url_cate)
    
    if response.status_code == 200:
        api_data_cate = response2.json()
        for item in api_data_cate:
            Category.objects.create(
                name=item['name'],
                created=item['creationAt'],
                updated=item['updatedAt'],
            )
    else:
        print("Failed to fetch data from the API")
        
fetch_and_save_data()
    
