Segue o README atualizado e melhor estruturado com base no conteúdo fornecido:

---

# API Meteora

A **API Meteora** é uma solução RESTful desenvolvida para gestão de dados e integração com ferramentas externas. Construída com **Django** e **Django REST Framework**, oferece operações CRUD, autenticação, documentação interativa e validações avançadas.

---

## 🛠 Tecnologias e Funcionalidades

### Tecnologias Utilizadas:
- **Python** e **Django**: Backend robusto e escalável.
- **Django REST Framework**: Criação e gestão de APIs RESTful.
- **drf-yasg**: Documentação interativa (Swagger/Redoc).
- Bibliotecas adicionais:
  - **google-auth**: Integração com APIs do Google.

### Principais Funcionalidades:
- **Gestão de Produtos**:
  - CRUD completo para produtos (nome, descrição, preço, estoque e categoria).
- **Documentação Interativa**:
  - Acesse os endpoints via `/swagger/` ou `/redoc/`.
- **Autenticação**:
  - Integração com APIs externas, como Google, para login e validação.
- **Expansibilidade**:
  - Ideal para projetos de e-commerce ou gestão de inventários.

---

## 📋 Requisitos

Antes de começar, garanta que o Python está instalado. Em seguida, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/GiihVieira/api-meteora.git
   ```

2. **Acesse o diretório do projeto**:
   ```bash
   cd api-meteora
   ```

3. **Configure as variáveis de ambiente** e execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor local**:
   ```bash
   python manage.py runserver
   ```

5. A API estará disponível em:
   - **Local**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Documentação**: `/swagger/` ou `/redoc/`.

---

## 📖 Documentação

Explore as rotas e teste as funcionalidades diretamente na documentação interativa:
- **Swagger**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo:

1. **Faça um fork do repositório**.
2. **Crie uma branch para suas alterações**:
   ```bash
   git checkout -b minha-feature
   ```
3. **Envie suas alterações**:
   ```bash
   git push origin minha-feature
   ```
4. **Abra um Pull Request**.

---

## 👤 Autor

Desenvolvido por [Giovane Vieira](https://github.com/GiihVieira), estudante de **Análise e Desenvolvimento de Sistemas** na Fatec Sorocaba.

---
