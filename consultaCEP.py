import requests
# Função para validar o formato do CEP
def validar_cep(cep):
    return len(cep) == 8 and cep.isdigit()

# Função para consultar o CEP
def consultar_cep(cep, formato):
    # Verifica se o formato do CEP é válido
    if not validar_cep(cep):
        return {"error": "CEP inválido"}

    # Monta a URL de consulta
    url = f"https://viacep.com.br/ws/{cep}/{formato}/"

    # Faz a requisição ao serviço ViaCEP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Retorna os dados no formato desejado
        return response.json()
    elif response.status_code == 400:
        # Retorna erro quando o CEP não é encontrado
        return {"error": "CEP não encontrado"}
    else:
        # Retorna erro genérico em outros casos
        return {"error": "Erro ao processar a requisição"}

# Exemplo de uso:
cep = input("Digite o cep que deseja bucar: ")
formato = "json"
resultado = consultar_cep(cep, formato)
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
