EMBRAPA_OPT = {
    "producao": "opt_02",
    "processamento": "opt_03",
    "comercializacao": "opt_04",
    "importacao": "opt_05",
    "exportacao": "opt_06",
}

EMBRAPA_SUBOPT = {
    "processamento": {
        "viniferas": "subopt_01",
        "americanas-e-hibridas": "subopt_02",
        "uvas-de-mesa": "subopt_03",
        "sem-classificacao": "subopt_04",
    },
    "importacao": {
        "vinhos-mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas-frescas": "subopt_03",
        "uvas-passas": "subopt_04",
        "suco-de-uva": "subopt_05",
    },
    "exportacao": {
        "vinhos-mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas-frescas": "subopt_03",
        "suco-de-uva": "subopt_04",
    },
    # producao e comercializacao não têm subopcao
}

def get_opt_url(tipo: str) -> str:
    return EMBRAPA_OPT.get(tipo)

def get_subopt_url(tipo: str, categoria: str) -> str | None:
    return EMBRAPA_SUBOPT.get(tipo, {}).get(categoria)
