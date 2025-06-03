from enum import Enum

class TipoImportacao(str, Enum):
    vinhos_mesa = "vinhos-mesa"
    espumantes = "espumantes"
    uvas_frescas = "uvas-frescas"
    uvas_passas = "uvas-passas"
    suco_de_uva = "suco-de-uva"

class TipoExportacao(str, Enum):
    vinhos_mesa = "vinhos-mesa"
    espumantes = "espumantes"
    uvas_frescas = "uvas-frescas"
    suco_de_uva = "suco-de-uva"

class TipoProcessamento(str, Enum):
    viniferas = "viniferas"
    americanas_hibridas = "americanas-e-hibridas"
    uvas_mesa = "uvas-de-mesa"
    sem_classificacao = "sem-classificacao"
