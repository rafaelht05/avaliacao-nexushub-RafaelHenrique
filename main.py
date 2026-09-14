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

#Etapa 3: Criação da Base de Dados e Elaboração do Prompt de Leitura
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_dados_1 = arquivo.readline()
    linha_dados_2 = arquivo.readline()
    linha_dados_3 = arquivo.readline()
    linha_dados_4 = arquivo.readline()

print("\n" + cabecalho)
print(linha_dados_1)
print(linha_dados_2)
print(linha_dados_3)
print(linha_dados_4)

#Etapa 4: Elaboração do Prompt para Painel e Cálculo Final

nome_startup = startups["nome"]

custo_1 = float(linha_dados_1.strip().split(",")[-1])
custo_2 = float(linha_dados_2.strip().split(",")[-1])
custo_3 = float(linha_dados_3.strip().split(",")[-1])
custo_4 = float(linha_dados_4.strip().split(",")[-1])

total = custo_1 + custo_2 + custo_3 + custo_4

print("\n===== PAINEL FINAL =====")
print("Startup:", nome_startup)
print("Bancada alocada: Bancada N1")
print(f"Total da infraestrutura Cloud: R$ {total:.2f}")