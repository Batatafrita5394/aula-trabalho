# =======================================================
# NETSENTINEL - CADASTRO E ANÁLISE DE ATIVOS DE REDE
# =======================================================

print('=' * 50)
print(' NETSENTINEL - CADASTRO DE ATIVOS DE REDE ')
print('=' * 50)

# Coleta de informações básicas do Host
nome_host = input("Digite o nome do Host (Hostname): ")
endereco_ip = input("Digite o Endereço IP do host (ex: 192.168.1.10): ")
endereco_mac = input("Digite o Endereço MAC (ex: 00:1B:44:11:3A:B7): ")
sistema_operacional = input("Digite o Sistema Operacional (ex: Linux, Windows): ")
porta = int(input("Digite a porta: "))

# =======================================================
# Criticidade e Monitoramento
# =======================================================

porta_critica = int(input("Digite a principal porta aberta a monitorar (Ex: 22, 80): "))
nivel_criticidade = int(input("Nível de criticidade do Ativo (1-Baixo a 5-Crítico): "))

# =======================================================
# Métricas de Rede e Vulnerabilidade
# =======================================================

tempo_resposta_ping = float(input("Tempo médio de Ping (ex: 100 ms): "))
score_cvss = float(input("Score CVSS (ex: 0.0 - 10.0): "))

# =======================================================
# Status e Segurança
# =======================================================

firewall_ativo_input = input("Firewall ativo? (s/n): ").strip().lower()
firewall_ativo = firewall_ativo_input == 's'

status_ativo_input = input("Host em operação? (s/n): ").strip().lower()
status_ativo = status_ativo_input == 's'

banda_mbps = float(input("Consumo de banda (Mbps): "))

# Verificação inicial da porta e ping
if porta == 23:
    print("ALERTA: A porta 23 (Telnet) é insegura!")
print(f"Tempo de Ping: {tempo_resposta_ping:.2f} ms")

# =======================================================
# Cálculo da Pontuação de Risco
# =======================================================

pontuacao = 0

if score_cvss >= 8.0:
    pontuacao += 5
if not firewall_ativo:
    pontuacao += 3
if porta == 22:
    pontuacao += 2
if porta == 3389:
    pontuacao += 3
if nivel_criticidade >= 3:
    pontuacao += nivel_criticidade

# =======================================================
# Base de Dados / Dicionários de Hosts
# =======================================================

hosts = {
    'WEB01': 'Online',
    'DB01': 'Online',
    'FW01': 'Offline',
}

criti = {
    'WEB01': 'Criticidade Alta',
    'DB01': 'Criticidade Crítica',
    'FW01': 'Dentro dos padrões',
}

cvss_hosts = {
    'WEB01': 6.4,
    'DB01': 8.2,
    'FW01': 4.5,
}

# Análise de risco por porta e score CVSS
if porta == 23:
    print(f'Alerta: acesso de porta telnet {porta} detectada!!')
elif porta == 3389:
    print('Alerta: Risco alto porta 3389 com host')
elif porta == 22:
    print("Risco medio")
else:
    print('Tudo lindo')

if porta == 23 and score_cvss >= 9:
    print('Altamente Crítico: acesso a porta 23 e cvss maior que 8')
elif porta == 3389 and score_cvss >= 7:
    print('Alerta alto: Risco alto porta 3389 com host e cvss maior que 7')

# =======================================================
# Inventário de Equipamentos
# =======================================================

inventario = [
    {
        "hostname": "WEB01",
        "IP": "192.168.1.10",
        "status": "ONLINE",
        "sistema": "OS",
        "criticidade": "ALTA",
    },
    {
        "hostname": "DB01",
        "IP": "192.168.1.20",
        "sistema": "Linux",
        "criticidade": "ALTA",
        "status": "ONLINE",
    },
    {
        "hostname": "FW01",
        "IP": "192.168.1.1",
        "status": "ONLINE",
        "sistema": "Windows",
        "criticidade": "ALTA",
    },
    {
        "hostname": "RTR01",
        "IP": "192.168.1.254",
        "status": "OFFLINE",
        "sistema": "Linux",
        "criticidade": "ALTA",
    },
]

print(f"Total de itens no inventário antes da adição: {len(inventario)}")

print("\n--- Adicionar novo ativo ao inventário ---")
inventario.append({
    "hostname": input("Digite o hostname: "),
    "IP": input("Digite o IP: "),
    "status": input("Digite o status: "),
    "sistema": input("Digite o sistema: "),
    "criticidade": input("Digite a criticidade: "),
})

# =======================================================
# Relatório Final do Ativo Cadastrado
# =======================================================

print('\n' + '=' * 50)
print('CADASTRO DE ATIVOS DE REDE')
print('=' * 50)

print(f'Hostname: {nome_host} (Tipo: {type(nome_host).__name__})')
print(f'Endereço IP: {endereco_ip} (Tipo: {type(endereco_ip).__name__})')
print(f'Endereço MAC: {endereco_mac} (Tipo: {type(endereco_mac).__name__})')
print(f'Sistema Operacional: {sistema_operacional} (Tipo: {type(sistema_operacional).__name__})')
print(f'Porta Crítica: {porta_critica} (Tipo: {type(porta_critica).__name__})')
print(f'Nível de Criticidade: {nivel_criticidade} (Tipo: {type(nivel_criticidade).__name__})')
print(f'Tempo Médio de Ping: {tempo_resposta_ping} ms (Tipo: {type(tempo_resposta_ping).__name__})')
print(f'Score CVSS: {score_cvss} (Tipo: {type(score_cvss).__name__})')
print(f'Firewall Ativo: {firewall_ativo} (Tipo: {type(firewall_ativo).__name__})')
print(f'Host em Operação: {status_ativo} (Tipo: {type(status_ativo).__name__})')
print(f'Consumo de Banda: {banda_mbps} Mbps (Tipo: {type(banda_mbps).__name__})')
print(f'Pontuação de Risco: {pontuacao} (Tipo: {type(pontuacao).__name__})')
print(f'Porta: {porta} (Tipo: {type(porta).__name__})')

print('\n' + '-' * 50)
print('STATUS DOS HOSTS MONITORADOS:')
for cri in criti:
    print(f'Host verificado: {cri} - {criti[cri]} - Status: {hosts[cri]} - CVSS: {cvss_hosts[cri]}')

print('\n' + '-' * 50)
print('INVENTÁRIO COMPLETO:')
for ativo in inventario:
    print(f"{ativo['hostname']} === {ativo}")

# Avaliação final de conformidade
alerta_seguranca = (score_cvss >= 7.0) or (not firewall_ativo)

print('\n' + '-' * 50)
if alerta_seguranca:
    print('ATENÇÃO: Alto risco!')
else:
    print('STATUS: Dentro da conformidade.')
