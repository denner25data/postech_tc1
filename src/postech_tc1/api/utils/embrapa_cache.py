import json
import os
import time
from typing import Optional

BASE_CACHE_DIR = "embrapa_cache"
DEFAULT_TTL = 60 * 60 * 24  # 24h

def _build_cache_path(opt: str, ano: int, subopt: Optional[str]) -> str:
    filename = f"{opt}_{ano}"
    if subopt:
        filename += f"_{subopt}"
    return os.path.join(BASE_CACHE_DIR, f"{filename}.json")

def is_cache_expired(path: str, ttl: int) -> bool:
    if not os.path.exists(path):
        return True
    modified_time = os.path.getmtime(path)
    return (time.time() - modified_time) > ttl

def save(opt: str, ano: int, subopt: Optional[str], data: list[dict]) -> None:
    os.makedirs(BASE_CACHE_DIR, exist_ok=True)
    path = _build_cache_path(opt, ano, subopt)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load(opt: str, ano: int, subopt: Optional[str], ttl: int = DEFAULT_TTL) -> Optional[list[dict]]:
    path = _build_cache_path(opt, ano, subopt)
    if not os.path.exists(path) or is_cache_expired(path, ttl):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
