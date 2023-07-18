import requests
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Acesso ao site www.pudim.com.br -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)

def acessoSite(site):
    """Função de acesso a URLs de sites
    :param site: parâmetro tipo string, ali é onde irá colocar a URL do site.
    Caso você consiga acessar o site a função te retornara um print dizendoq ue está acessivel,
    Caso não cosiga será retornado um print negativo. E caso aja um erro ele retornara o erro a você.
    """
    try:
        resp = requests.get(site)
        if resp.status_code == 200:
            print('O site está acessecivel!')
        else:
            print('O site não está acessivel!')
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao acessar o site: {e}')

