from django.http import JsonResponse
import requests

def api_status_check(request):
    """
    Verifica em tempo real a saúde de cada uma das 5 APIs públicas de contingência de CNPJ.
    """
    cnpj_teste = "60701190000104" # Itaú (CNPJ válido para teste rápido)

    endpoints = [
        {"nome": "BrasilAPI", "url": f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_teste}"},
        {"nome": "Minha Receita", "url": f"https://minhareceita.org/{cnpj_teste}"},
        {"nome": "CNPJ.ws", "url": f"https://publica.cnpj.ws/cnpj/{cnpj_teste}"},
        {"nome": "ReceitaWS", "url": f"https://www.receitaws.com.br/v1/cnpj/{cnpj_teste}"},
        {"nome": "CNPJa", "url": f"https://api.cnpja.com.br/office/{cnpj_teste}"}
    ]

    status_apis = []
    for ep in endpoints:
        try:
            resp = requests.get(ep["url"], timeout=3)
            # Consideramos funcional se retornar 200 OK ou 429 (rate-limit atingido mas respondendo)
            if resp.status_code in [200, 429]:
                status_apis.append({
                    "nome": ep["nome"],
                    "status": "online" if resp.status_code == 200 else "rate-limit",
                    "code": resp.status_code
                })
            else:
                status_apis.append({
                    "nome": ep["nome"],
                    "status": "offline",
                    "code": resp.status_code
                })
        except Exception:
            status_apis.append({
                "nome": ep["nome"],
                "status": "offline",
                "code": 0
            })

    return JsonResponse({"apis": status_apis})
