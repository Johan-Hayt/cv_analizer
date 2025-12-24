from langchain_openai import ChatOpenAI
from prompt.cv_prompts import crear_sistema_prompts
from models.cv_model import AnalisisCv

def crear_evaluador() -> AnalisisCv:
    
    #Instanciar modelo base
    llm_base = ChatOpenAI(
        model="gpt-5-nano",
        temperature=0.2,
    )

    # Modelo con salida estructurada
    llm_structured = llm_base.with_structured_output(AnalisisCv)

    # plantilla prompt
    chat_prompt = crear_sistema_prompts()

    # pipeline del proceso
    return chat_prompt | llm_structured


def evaluador_cv(texto_cv: str, descripcion_puesto: str)->AnalisisCv:
    try:
        # instanciando al evaluador
        evaluador = crear_evaluador()

        # invocando al evaluador
        return evaluador.invoke(
                    {
                        "texto_cv": texto_cv,
                        "descripcion_puesto": descripcion_puesto,
                    }
                )

    except Exception as e:
        return AnalisisCv(
            nombre_candidato="Error en procesamiento.",
            experiencia_anios=0,
            habilidades_tecnicas=["Error al leer el PDF"+str(e)],
            education="",
            experiencia_relevante="",
            fortalezas=[""],
            areas_mejora=[""],
            porcentaje_adecuacion=0,
        )