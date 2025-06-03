# API Postech Tech Challenge 1 - Dados Embrapa

## Descrição

Esta API em FastAPI realiza scraping de dados do site da Embrapa. Ela disponibiliza dados sobre produção, comercialização, processamento, importação e exportação, com filtros por ano e categorias específicas.

A API possui autenticação via JWT para controle de acesso e utiliza cache para otimizar consultas e evitar sobrecarga no site da Embrapa, além de possuir fallback em casos de falha no scrape.

## Funcionalidades

- **Dados**: Produção, comercialização, processamento, importação/exportação.  
- **Filtros**: Por ano e categoria (quando aplicável).  
- **Segurança**: Autenticação JWT (roteamento protegido).  
- **Performance**: Cache de consultas (evita scraping repetitivo).  
- **Resiliência**: Fallback com dados locais se o site da Embrapa estiver offline. 
- **Documentação**: Documentação automática via Swagger UI.

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/denner25data/postech_tc1.git
cd postech_tc1
```

2. Instale o Poetry (caso ainda não tenha):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Instale as dependências e crie o ambiente virtual:

```bash
poetry install
```

## Uso

1. Defina as credenciais no arquivo `config.py`:  
```python 
ADMIN_USERNAME = "seu_usuario"  
ADMIN_PASSWORD = "sua_senha"  
```

2. Rode a aplicação:

```bash
poetry run uvicorn postech_tc1.main:app --reload
```

3. Acesse a API e a documentação em: 

```bash
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

4. Gere o token JWT com um POST em `/auth/token` enviando o formulário com `username` e `password` (formato `application/x-www-form-urlencoded`). Credenciais configuradas no arquivo `config.py` (`ADMIN_USERNAME` e `ADMIN_PASSWORD`). Exemplo:

```bash
curl --location 'http://127.0.0.1:8000/auth/token' \
    --form 'username=seu_usuario' \
    --form 'password=sua_senha'
```

5. Use o token nas requisições autenticadas, incluindo o header:

```bash
Authorization: Bearer <seu_token>
```

6. Exemplo para obter dados de produção:

```bash
curl -X GET "http://127.0.0.1:8000/producao?ano=2023" -H "Authorization: Bearer <seu_token>"

```

## Tecnologias

Este projeto foi desenvolvido utilizando as seguintes bibliotecas e frameworks:

- **FastAPI** — framework web moderno e rápido para construir APIs com Python.
- **Uvicorn** — servidor ASGI leve para executar a aplicação FastAPI.
- **python-jose[cryptography]** — biblioteca para manipulação de JWT e criptografia.
- **python-multipart**  — suporte para parsing de dados multipart/form-data (upload de arquivos, formulários).
- **httpx** — cliente HTTP assíncrono para realizar requisições web.
- **beautifulsoup4** — parser HTML para extrair dados da página web.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- **Nome:** Denner Rodrigues Campelo
- **E-mail:** dennerrc95@hotmail.com
- **LinkedIn:** [linkedin.com/in/dennerrc95](https://linkedin.com/in/dennerrc95)

Fique à vontade para abrir issues no repositório ou enviar pull requests.
