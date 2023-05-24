import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'masxmenos.settings')
django.setup()

from catalog.models import Producto, Tienda, Categoria

# Load the CSV file into a DataFrame
df = pd.read_csv('OlimpicaLacteos.csv')
for index, row in df.iterrows():
    p = row['Product Name;Price'].split(';')
    name = p[0].strip()
    price = float(p[1].replace('$','').replace('.','').strip())
    # Create a new instance of producto
    my_model_instance = Producto()
    tienda = Tienda.objects.get(name='Olimpica')
    cat = Categoria.objects.get(name='Lacteos')
    # Set the values from the DataFrame to the model fields
    my_model_instance.name = name
    my_model_instance.price = price
    my_model_instance.store = tienda
    my_model_instance.cat = cat
    
    # Save the model instance to the database
    my_model_instance.save()