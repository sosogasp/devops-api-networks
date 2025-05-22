# Imagem base
FROM python:3.11-slim

# Instala dependências do sistema e do Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala bibliotecas Python diretamente
RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    sqlalchemy \
    psycopg2-binary \
    nbconvert

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY dashboard_vendas.ipynb .
COPY run_notebook.py .

# Comando para rodar o notebook convertido em script
CMD ["python", "run_notebook.py"]
