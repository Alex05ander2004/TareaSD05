import requests

clientes = ['HolaCliente1', 'HolaCliente2', 'HolaCliente3']

for payload in clientes:
    r = requests.get(f'http://127.0.0.1:5000/rpc_call/{payload}')
    print(f"Respuesta para {payload}: {r.text}")
