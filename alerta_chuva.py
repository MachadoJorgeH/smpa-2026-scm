# Módulo de alerta de chuva forte para os produtores (nova funcionalidade)

# Previsão de chuva, em milímetros, a partir da qual o alerta é enviado
LIMITE_CHUVA_MM = 50


def verificar_alerta(previsao_mm):
    # Retorna a mensagem de alerta quando a previsão passa do limite
    if previsao_mm >= LIMITE_CHUVA_MM:
        return f"ALERTA: chuva forte prevista ({previsao_mm} mm). Adie a aplicação de defensivos."
    return f"Sem alerta: previsão de {previsao_mm} mm."


if __name__ == "__main__":
    # Testa o alerta com uma previsão fraca e uma forte
    for previsao in [12, 65]:
        print(verificar_alerta(previsao))