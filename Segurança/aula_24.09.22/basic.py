from http.client import HTTPException
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

#Depends = vai depender de uma outra função que vai ser chamada antes
app = FastAPI()
seguranca = HTTPBasic()


def confere_credencial(credencial: HTTPBasicCredentials = Depends(seguranca)):
      usuario = 'felipe'
      senha = 'luizacode'
      
      credencial_usuario = credencial.username
      credencial_senha = credencial.password
      
      
      if usuario == credencial_usuario:
            if senha == credencial_senha:
                  return usuario
            
      raise HTTPException( \
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Usuario ou Senha incorretos', 
            headers={'WWW-Authenticate': 'Basic'})
            

@app.get("/auth/basic")
def basic(credenciais: str = Depends(confere_credencial)):
      return 'Usuário' + usuario