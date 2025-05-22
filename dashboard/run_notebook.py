import subprocess

# Converte o notebook para script Python
subprocess.run(["jupyter", "nbconvert", "--to", "script", "dashboard_vendas.ipynb"])

# Executa o script convertido
subprocess.run(["python", "dashboard_vendas.py"])
