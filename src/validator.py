import pandas as pd
from pydantic import BaseModel, Field, ValidationError, validator
from typing import List, Optional, Tuple
from datetime import date

class AdData(BaseModel):
    Organizador: int
    Ano_Mes: str
    Dia_da_Semana: str
    Tipo_Dia: str
    Objetivo: str
    Date: date
    AdSet_name: str
    Amount_spent: float = Field(ge=0)
    Link_clicks: Optional[int] = None
    Impressions: Optional[int] = None
    Conversions: Optional[int] = None
    Segmentação: str
    Tipo_de_Anúncio: str
    Fase: str

    @validator("Ano_Mes")
    def validate_ano_mes(cls, value):
        if " | " not in value:
            raise ValueError("Ano_Mes deve conter ' | ' separando ano e mês (ex: '2024 | Março')")
        return value

    @validator("Tipo_Dia")
    def validate_tipo_dia(cls, value):
        if value not in {"Dia útil", "Final de Semana", "Feriado"}:
            raise ValueError("Tipo_Dia deve ser 'Dia útil', 'Final de semana' ou 'Feriado'")
        return value


def validate_dataframe(df: pd.DataFrame) -> Tuple[List[AdData], List[Tuple[int, dict, str]]]:
    """
    Valida um DataFrame linha a linha usando o modelo Pydantic `AdData`.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo os dados a serem validados.

    Returns
    -------
    Tuple[List[AdData], List[Tuple[int, dict, str]]]
        Uma tupla com a lista de registros válidos e a lista de erros contendo:
        (índice, linha original como dict, mensagem de erro).
    """
    valid_data = []
    errors = []

    for i, row in df.iterrows():
        # Converte todos os NaN para None
        record = {k: (None if pd.isna(v) else v) for k, v in row.items()}
        try:
            validated = AdData(**record)
            valid_data.append(validated)
        except ValidationError as e:
            errors.append((i, record, str(e)))

    return valid_data, errors