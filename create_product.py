import os
import django
import requests
from django.core.files.base import ContentFile
from googleapiclient.discovery import build

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from meteora.models import Product, Category
from datetime import datetime

API_KEY = 'Your API_KEY here' 
CSE_ID  = 'Your CSE_ID here' 

def get_image_url(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(
        q           = query,
        cx          = CSE_ID,
        searchType  = 'image',
        num         = 1 
    ).execute()

    if 'items' in res:
        return res['items'][0]['link']
    else:
        return None

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        image_name = url.split("/")[-1] 
        os.path.join('media_root/products', image_name) 

        image_file = ContentFile(response.content)

        return image_file, image_name
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a image: {e}")
        return None, None

data = [
    ('Acessórios',  'Bolsinha de Ombro Feminina - Couro Sintético', 'Bolsinha de ombro feminina feita em couro sintético de alta qualidade.',                       149.90,     120),
    ('Móveis',      'Cadeira de Escritório Ergonomica',             'Cadeira de escritório com ajuste de altura, apoio lombar e rodas de silicone',                 699.90,     50),
    ('Saúde',       'Termômetro Digital Infravermelho',             'Termômetro digital sem contato, mede temperatura corporal em segundos',                        129.90,     200),
    ('Roupas',      'Camiseta Masculina Nike',                      'Camiseta de algodão com logo Nike, disponível nas cores preta e branca',                       79.90,      150),
    ('Esportes',    'Bola de Futebol Nike Premier',                 'Bola de futebol oficial Nike Premier League, tamanho 5',                                       49.90,      80),
    ('Alimentos',   'Cesta de Frutas Orgânicas',                    'Cesta com frutas orgânicas frescas, incluindo maçãs, bananas, peras e laranjas',               99.90,      60),
    ('Beleza',      'Kit Maquiagem MAC',                            'Kit completo de maquiagem da MAC, incluindo base, batom, sombra e pincéis',                    299.90,     40),
    ('Automóveis',  'Kit de Lavagem de Carro',                      'Kit completo para lavagem de carros com shampoo, esponja e cera',                              179.90,     100),
    ('Brinquedos',  'Boneca Barbie Fashionista',                    'Boneca Barbie com várias opções de roupas e acessórios',                                       89.90,      200),
    ('Ferramentas', 'Parafusadeira Elétrica Makita',                'Parafusadeira elétrica Makita com 2 baterias, ideal para trabalhos manuais e profissionais',   349.90,     70)
]


def create_product():
    for category_name, name_product, description, price, qtd_stock in data:
        
        category = Category.objects.get(name=category_name)
        image_url = get_image_url(name_product)

        if image_url:
            image_file, image_name = download_image(image_url)

            if image_file:
                p = Product.objects.create(
                    name        = name_product,
                    description = description,
                    price       = price,
                    qtd_stock   = qtd_stock,
                    category    = category,
                    make_in     = datetime.now(),
                    update_in   = datetime.now(),
                )
                
                p.image.save(image_name, image_file)
                p.save()

                print(f"Produto '{name_product}' criado e imagem salva com sucesso!")

create_product()
