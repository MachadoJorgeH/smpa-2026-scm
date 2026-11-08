# Módulo de leitura dos sensores de umidade do solo do SMPA

# Leituras simuladas de cada talhão da fazenda (umidade em %)
LEITURAS = {"talhao-01": 18.5, "talhao-02": 32.0, "talhao-03": 45.2}


def ler_umidade(sensor_id):
    # Devolve a umidade medida pelo sensor; 0.0 se o sensor não existir
    return LEITURAS.get(sensor_id, 0.0)


if __name__ == "__main__":
    # Mostra a leitura de cada talhão
    for sensor in LEITURAS:
        print(f"{sensor}: {ler_umidade(sensor)}%")
