# Projeto Dashboard de Vendas com Containers Docker

Este projeto tem como objetivo criar um ambiente com múltiplos containers Docker para um dashboard de vendas, utilizando:

- **PostgreSQL** para banco de dados;
- **Container `pegar-dados`** para manipulação/preparação dos dados;
- **Container `dashboard`** para visualização interativa via Jupyter Notebook.

---

## Requisitos

- Docker instalado e rodando no seu computador (Windows).
- A rede Docker `network-dashboard` criada (pode ser criada automaticamente pelo script `.bat`).

---

## Passo a passo para executar o projeto

### 1. Criar a rede Docker (caso não exista)

```bash
docker network inspect network-dashboard >nul 2>&1 || docker network create network-dashboard
