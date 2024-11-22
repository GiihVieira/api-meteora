import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from meteora.models import Category

data = [
    ('Acessórios',  'Uma variedade de itens para complementar seu estilo, como bolsas, mochilas, carteiras, cintos, óculos de sol, relógios e bijuterias.'), 
    ('Móveis',      'Móveis para casa e escritório, incluindo sofás, cadeiras, mesas, estantes e outros itens de decoração e funcionalidade'),
    ('Saúde',       'Produtos voltados para o cuidado pessoal e saúde, incluindo itens como termômetros, vitaminas, e suplementos'), 
    ('Roupas',      'Vestimentas de diferentes estilos, incluindo camisetas, vestidos, calças, e acessórios de moda para todas as idades'),  
    ('Esportes',    'Equipamentos e acessórios para prática de esportes, como bolas, raquetes, tênis e outros produtos esportivos'),  
    ('Alimentos',   'Alimentos e bebidas, desde itens frescos até alimentos processados, com foco em qualidade e praticidade'), 
    ('Beleza',      'Produtos de cuidados pessoais e cosméticos, como maquiagens, cremes, perfumes e outros itens de beleza e bem-estar'),  
    ('Automóveis',  'Acessórios e peças para veículos, incluindo kits de lavagem, pneus, óleos, e itens de manutenção de carros e motos'), 
    ('Brinquedos',  'Brinquedos e jogos para crianças de todas as idades, incluindo bonecas, jogos de tabuleiro, brinquedos educativos e mais'),
    ('Ferramentas', 'Ferramentas manuais e elétricas para uso profissional ou doméstico, incluindo parafusadeiras, martelos, e kits de reparo') 
]

def criar_cursos():
    for name, description in data:
        make_in     = datetime.datetime.now()
        update_in   = datetime.datetime.now()
        Category.objects.create(
            name        = name, 
            description = description, 
            make_in     = make_in, 
            update_in   = update_in
        )

criar_cursos()