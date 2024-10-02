# Passo de solução:
#   1º Abrir os 6 arquivos em excel
#   2º Para cada arquivo:
#       Verificar se algum valor na coluna "Vendas" naquele arquivo é maior do que R$55.000
#           Se for maior que R$ 55.000 -> Envia um SMS como nome, mês e as vendas do vendedor
#           Se for menor, não fazer nada;

# Aquivos instalados para integração:

# Excel: "pandas" e "openpyxl";
# SMS: "twilio";


import pandas as pd
from twilio.rest import Client

account_sid = 'ACccf16a49e5e2eef196114d255f288972'
auth_token = '36f7e7bbed29a5401b47b8a2c7fcbe64'
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês de {mes} alguém bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')

        message = client.messages.create(
            from_='+12075485901',
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}',
            to='+5515997701411'
        )