import os
import csv

# caminho pasta de logs
pasta_logs = "/Users/amandananni/Documents/analisador-de-logs/logs"


#contador tipos de mensagens no total
resumo_total = {
    "INFO" : 0,
    "WARNING" : 0,
    "ERROR": 0
}

#lista para armazenar dados para csv
dados_csv = []

# percorrer os arquivos na pasta logs
for arquivo in os.listdir(pasta_logs):
    if arquivo.endswith(".log"):
        caminho_arquivo = os.path.join(pasta_logs, arquivo)
        resumo_arquivo = {"INFO": 0, "WARNING": 0, "ERROR": 0}

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                for tipo in resumo_arquivo.keys():
                    if tipo in linha:
                        resumo_arquivo [tipo] += 1
                        resumo_total[tipo] += 1

        # adicionar resumo do arquivo à lista para csv
        dados_csv.append({
            "Arquivo": arquivo,
            "INFO": resumo_arquivo ["INFO"],
            "WARNING": resumo_arquivo["WARNING"],
            "ERROR": resumo_arquivo["ERROR"]
        })

        # mostrar resumo do arquivo no terminal
        print(f"\nResumo do arquivo {arquivo}:")
        for tipo, quantidade in resumo_arquivo.items ():
            print(f"{tipo}: {quantidade}")

# mostrar resumo total no terminal
print("\nResumo total de todos os logs:")
for tipo, quantidade in resumo_total.items():
    print(f"{tipo}: {quantidade}")

# adicionar linha de total para csv
dados_csv.append({
    "Arquivo": "TOTAL",
    "INFO": resumo_total["INFO"],
    "WARNING": resumo_total["WARNING"],
    "ERROR": resumo_total["ERROR"]
})

#Gerar CSV
arquivo_csv = "relatorio_logs.csv"
with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
    campos = ["Arquivo", "INFO", "WARNING", "ERROR"]
    writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')  # <- aqui
    writer.writeheader()
    for linha in dados_csv:
        writer.writerow(linha)

print(f"\nRelatório gerado: {arquivo_csv}")


