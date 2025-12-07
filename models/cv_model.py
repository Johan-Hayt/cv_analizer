from pydantic import BaseModel, Field

class AnalisisCv(BaseModel):

    nombre_candidato: str = Field(description="Nombre completo del candidato")
    experiencia_anios: int = Field(description="Años de experiencia laboral del candidato")
    habilidades_tecnicas: list[str] = Field(description="Lista de las 5-8 habilidades técnicas más relevantes del candidato")
    education: str = Field(description="Nivel educativo mas alto y especialización principal del candidato")
    experiencia_relevante: str = Field(description="Descripción breve de la experiencia laboral más relevante del candidato")
    fortalezas: list[str] = Field(description="3-5 fortalezas clave del candidato")
    areas_mejora: list[str] = Field(description="2-4 áreas de mejora o desarrollo para el candidato")
    porcentaje_adecuacion: float = Field(description="Porcentaje de adecuación del candidato para el puesto (0-100%)", ge=0, le=100)