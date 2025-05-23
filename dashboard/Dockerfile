# Base Python
FROM python:3.11-slim

# Instala dependências
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala pacotes Python
RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    sqlalchemy \
    psycopg2-binary \
    notebook

# Define diretório de trabalho
WORKDIR /app

# Copia o notebook
COPY graficos.ipynb .

# Expõe a porta padrão do Jupyter
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]
