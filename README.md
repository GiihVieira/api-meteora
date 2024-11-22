# API Meteora

A **API Meteora** é um projeto desenvolvido para fornecer serviços RESTful com funcionalidades relacionadas à gestão de dados e integração com ferramentas externas. Construída com o framework Django e Django REST Framework, ela oferece endpoints flexíveis para operações CRUD e suporte à autenticação e documentação interativa.

## 🛠 Tecnologias e Funcionalidades

O projeto utiliza as seguintes tecnologias:

- **Python** e **Django** para o backend.
- **Django REST Framework** para construção da API.
- **drf-yasg** para documentação interativa dos endpoints.
- Bibliotecas adicionais para integração com APIs do Google, manipulação de dados e validações (como `validate-docbr` e `google-auth`).

- Gestão de Produtos: Operações CRUD para produtos, com informações como nome, descrição, preço, estoque e categoria.
- Validações: Suporte a validações específicas, como CPF/CNPJ, utilizando bibliotecas como validate-docbr.
- Documentação Interativa: Endpoints documentados via Swagger ou Redoc para facilitar o uso da API.
- Autenticação: Integração com serviços externos, como APIs do Google, para autenticação e validação.
- Expansibilidade: Ideal para e-commerce, gestão de inventário ou integração com plataformas externas.

## 📋 Requisitos

Certifique-se de ter o Python instalado e, em seguida, instale as dependências listadas no arquivo `requeriments.txt`:

```bash
pip install -r requeriments.txt
```

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/GiihVieira/api-meteora.git
```

2. Acesse o diretório do projeto:

```bash
cd api-meteora
```

3. Configure as variáveis de ambiente e execute as migrações do banco de dados:

```bash
python manage.py migrate
```

4. Inicie o servidor local:

```bash
python manage.py runserver
```

Agora a API estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📖 Documentação

Acesse a documentação interativa da API no endpoint `/swagger/` ou `/redoc/` para explorar as rotas e realizar testes.

## 🤝 Contribuição

Contribuições são bem-vindas! Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações: `git checkout -b minha-feature`.
3. Envie suas alterações: `git push origin minha-feature`.
4. Abra um Pull Request.

---
