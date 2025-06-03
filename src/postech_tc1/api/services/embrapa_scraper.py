import httpx
from bs4 import BeautifulSoup
from postech_tc1.api.utils.options import get_opt_url, get_subopt_url
from postech_tc1.api.utils.embrapa_cache import save, load

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

async def fetch_embrapa(
    opt: str,
    ano: int,
    subopt: str | None = None,
    force: bool = False
) -> list[dict]:
    
    if not force:
        cached = load(opt, ano, subopt)
        if cached:
            return cached

    dataset = get_opt_url(opt)
    if not dataset:
        raise ValueError(f"Dataset inválido: {opt}")

    params = {
        "ano": ano,
        "dataset": dataset
    }
    if subopt:
        tipo = get_subopt_url(opt, subopt)
        if not tipo:
            raise ValueError(f"Tipo inválido para {opt}")
        params["tipo"] = tipo

    url = f"{BASE_URL}?ano={params['ano']}&opcao={params['dataset']}"
    if "tipo" in params:
        url += f"&subopcao={params['tipo']}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        if cached:
            return cached
        raise RuntimeError(f"Erro ao acessar Embrapa e sem dados em cache: {str(e)}")


    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    if not table:
        raise ValueError("Dados não encontrados na página")

    rows = table.find_all("tr")
    data = []
    group = None

    for row in rows:
        cols = row.find_all("td")
        if not cols:
            continue

        item = cols[0].get_text(strip=True)
        valor = cols[1].get_text(strip=True)

        if opt in ('importacao', 'exportacao'):
            valor2 = cols[2].get_text(strip=True)
            data.append({
                "item": item,
                "valor": valor,
                "valor2": valor2,
            })
        else:
            td_class = cols[0].get("class", [])
            if "tb_item" in td_class:
                group = item
            elif "tb_subitem" in td_class:
                data.append({
                    "grupo": group,
                    "item": item,
                    "valor": valor,
                })

    save(opt, ano, subopt, data)

    return data
