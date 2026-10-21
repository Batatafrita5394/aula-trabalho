print('=' * 50)
print(' NETSENTINEL - CADASTRO DE ATIVOS DE REDE ')
print('=' * 50)

nome_host = input("Digite o nome do Host (Hostname): ")
endereco_ip = input("Digite o Endereço IP do host (ex: 192.168.1.10):")
endereco_mac = input("Digite o Endereço MAC (ex: 00:1B:44:11:3A:B7):")
sistema_operacional = input("Digite o Sistema Operacional (ex: Linux, Windows):")
porta = int(input("Digite a porta: "))

#=======================================================
#criticalidade

porta_critica = int(input("Digite a principal porta aberta a monitorar (Ex: 22, 80):"))
cn = int(input("Nível de criticidade do Ativo (1-Baixo a 5-Crítico):"))

#=======================================================
#ping

tempo_resposta_ping = float(input('Tempo médio de Ping (ex : 100 ms): '))
score_cvss = float(input('Score CVSS (ex : 0.0 - 10.0): '))

#=======================================================
#firewall

firewall_ativo_input = input('Firewall ativo? (s/n): ').strip().lower()
firewall_ativo = firewall_ativo_input == 's'

#=======================================================
status_ativo_input = input('Host em operação? (s/n): ').strip().lower()
status_ativo = status_ativo_input == 's'

#=======================================================
#desafios de segurança
banda_mbps = float(input("Consumo de banda (Mbps): "))
if porta == 23:
    print("ALERTA: A porta 23 (Telnet) é insegura!")
print(f"Tempo de Ping: {ping:.2f} ms")
#=======================================================
#pontuação

pontuacao = 0

if cvss >= 8.0:
    pontuacao += 5
if not firewall_active:
    pontuacao += 3
if port == 22:
    pontuacao += 2
if port == 3389:
    pontuacao += 3
if cn >= 3:
    pontuacao += cn


if porta == 23:
    print(f'Alerta : acesso de porta telnet {porta} detectada!!')
elif porta == 3389:
    print('Aleta : Risco alto porta 3389 com host')
elif porta == 22:
    print("Risco medio")
else:
    print('Tudo lindo')

if porta == 23 and cvss >= 9:
    print(f'Altamente Critíco acesso a porta 23 e cvss maior que 8')
elif porta == 3389 and cvss >=7:
    print('Aleta alto : Risco alto porta 3389 com host e cvss maior que 7')

print('=' * 50)
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

alerta_seguranca = (score_cvss >= 7.0) or (not firewall_ativo)


if alerta_seguranca:
    print('ATENÇÃO: Alto risco!')
else:
    print('STATUS: Dentro da conformidade.')
