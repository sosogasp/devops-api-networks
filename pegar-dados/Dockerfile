FROM python:3.11-slim
RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

COPY pegar-dados.py .
COPY Lojas.csv .
COPY Produtos.csv .
COPY Clima.csv .
COPY Chocolate.csv .
COPY Vendas.csv .

RUN pip install pandas sqlalchemy psycopg2-binary

CMD ["python", "pegar-dados.py"]
