from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Consulta(BaseModel):
    pregunta: str

@app.get("/")
def read_root():
    return {"mensaje": "API de consultas funcionando"}

@app.post("/consultar")
def hacer_consulta(consulta: Consulta):
    pregunta = consulta.pregunta
    # Aquí podrías conectar con tu LLM o base de datos
    respuesta = f"Procesando tu pregunta: '{pregunta}'"
    return {"respuesta": respuesta}
