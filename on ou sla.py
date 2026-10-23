hosts = {
    'WEB01':'Online',
    'DB01':'Online',
    'FW01':'Offline',
    }
criti = {
    'WEB01':'Criticidade Alta',
    'DB01':'Criticidade Crítica',
    'FW01':'Dentro dos padrões',
    }

cvss = {
    'WEB01': 6.4,
    'DB01': 8.2,
    'FW01': 4.5,
    }

for cri in criti:
  print(f'Host verificada : {cri} - {criti[cri]} - Status : {hosts[cri]} - CVSS : {cvss[cri]}')
