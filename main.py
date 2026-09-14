#Etapa 1: Cadastro da Startup e Projetos
startups = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("STARTUP:", startups["nome"], "Segmento:", startups["segmento"])
print("1° Produto:", solucoes_ativas[0])

#Etapa 2: Mapeamento das Bancadas de Trabalho
bancadas = [
    [1,0],
    [0,1]
]

print("Status da BancadaN1:", bancadas[0][0], "\nStatus da BancadaN2:", bancadas[0][1], "\nStatus da BancadaS1:", bancadas[1][0], "\nStatus da BancadaS2:", bancadas[1][1])
print("Classificação de Status: 1 = Ocupado e 0 = Livre")