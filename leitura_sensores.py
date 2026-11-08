# Módulo de leitura dos sensores de umidade do solo do SMPA

# Leituras simuladas de cada talhão da fazenda (umidade em %)
LEITURAS = {"talhao-01": 18.5, "talhao-02": 32.0, "talhao-03": 45.2}


def ler_umidade(sensor_id):
    # Devolve a umidade medida pelo sensor; 0.0 se o sensor não existir
    return LEITURAS.get(sensor_id, 0.0)


def classificar_umidade(umidade):
    # Classifica a umidade do solo para orientar a irrigação
    if umidade < 20:
        return "seco - irrigar"
    if umidade < 40:
        return "adequado"
    return "encharcado - suspender irrigação"


if __name__ == "__main__":
    # Mostra a leitura e a classificação de cada talhão
    for sensor in LEITURAS:
        umidade = ler_umidade(sensor)
        print(f"{sensor}: {umidade}% ({classificar_umidade(umidade)})")