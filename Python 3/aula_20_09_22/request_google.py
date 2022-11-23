# Crie um script que o site da Google e retornar se o mesmo está acessível

from logging import exception
import re
from unittest import result
import requests

try: 
    requests.get("https://www.google.com.br/")
    result.raise_for_status()
    print("Google acessado")
except requests.exceptions as error:
    print(f"Não foi possivel acessar o Google. erro {error}")