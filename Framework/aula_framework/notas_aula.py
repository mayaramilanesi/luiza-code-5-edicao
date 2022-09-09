'''
API - Conjunto de normas que possibilita a comunicação entre plataformas através de uma série de padrões e protocolos

REST - Conjunto de restrições para aplicações WEB

API REST - Conjunto de restrições e normas para comunicação entre sistemas HTTP(s)/Web


UTILIZADO PARA COMUNICAÇÃO:
- Métodos(GET, POST)
- Caminhos: "api/produtos".
- Parâmetros


FRAMEWORKS
- Bibliotecas para desenvolvimento rápido para Web (API Rest)
      Django, Flask, Fast API
      
      
PORTAS TCP

- Um servidor pode ter vários serviços rodando nele
- O endereço do servidor é composto por IP + Porta
- Porta está associada a um serviço rodando no servidor
- localhost = 127.0.0.1
- Exemplo: 127.0.0.1:8000 (pra ele mesmo, próprio servidor, própria máquina)
Ip: Endereço de um prédio
Porta: número do apartamento
Porta identifica um serviço rodando no servidor identificado pelo IP


BIBLIOTECAS USADAS PELO FASTAPI

- uvicorn (ASGI (Asynchronous Server Gateway Interface))
- Utiliza Pydantic (Serialização)


MÉTODOS HTTP

GET
- Solicita a representação de um recurso específico. Requisições utilizando o método GET devem retornar apenas dados.

HEAD
- Os métodos HEAD solicitam uma resposta de uma forma idêntica ao método GET, porém sem conter o corpo da resposta

POST
- O método POST é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma
  mudança no estado do recurso ou efeitos colaterais no servidor
  
PUT
- O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição

DELETE
- O método DELETE remove um recurso específico

OPTIONS
- O método OPTIONS é usado para descrever as opções de comunicação com o recurso de destino
'''

#TESTE FASTAPI

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}