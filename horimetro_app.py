from datetime import datetime

historico = []

# Pega o horímetro inical e final digitados pelo usuário
def pedir_horimetros():
    horimetro_inicial = input("Horímetro inicial (HORAS:MINUTOS): ")
    horimetro_final = input("Horímetro final: (HORAS:MINUTOS): ")

    return horimetro_inicial, horimetro_final

# Validar se o horímetro está no formato correto
def validar_horimetro(horimetro):
    try:
        # Separa horas e minutos usando ":"
        horas, minutos = horimetro.split(":")

        # Converte horas e minutos para número inteiro
        horas = int(horas)
        minutos = int(minutos)

        # Verifica se os minutos sao menores que 0 e maiores que 59
        if minutos < 0 or minutos > 59:
            return False, "Horímetro inválido. Os minutos devem estar entre 00 e 59."
        else:
            return True, ""

    except:
        return False, "Horímetro inválido. Use o formato HORAS:MINUTOS"


# Converte um horímetro no formato HORAS:MINUTOS para minutos totais
def converter_para_minutos(horimetro):
    horas, minutos = horimetro.split(":")

    horas = int(horas)
    minutos = int(minutos)

    # Exemplo: 2:30 vira 150 minutos
    total_minutos = (horas * 60) + minutos

    return total_minutos

# Calcula a diferença entre o horímetro final e o inicial
def calcular_diferenca(inicial_minutos, final_minutos):
    return final_minutos - inicial_minutos


# Transforma o total de minutos em horas e minutos
def formatar_tempo(total_minutos):
    # Divide por 60 e pega somente a parte inteira das horas
    horas = total_minutos // 60

    # Pega o resto da divisão por 60, que representa os minutos restantes
    minutos = total_minutos % 60

    return f"Tempo de corte: {horas}h {minutos}min"


# Mostra o histórico de todos os cortes
def mostrar_historico(historico):

    print("\n=== HISTÓRICO DE CORTES ===")

    for numero, corte in enumerate(historico, start=1):
        print(f"\nCorte {numero}")
        print(f"Inicial: {corte['inicial']}")
        print(f"Final: {corte['final']}")
        print(corte["tempo"])

# Verifica se o tempo de corte digitado pelo usuário é igual ou superior ao tempo limite(40 horas)
def confirmar_tempo_alto(total_minutos):
    tempo_limite = 40 * 60


    if total_minutos >= tempo_limite:

        tempo_formatado = formatar_tempo(total_minutos)

        print(f"\nAtenção: O {tempo_formatado} está acima do padrão de cortes")
        print("Verifique se os horímetros foram digitados corretamente.")

        resposta = input("Deseja continuar mesmo assim? [S/N]: ")

        if resposta.lower() == "s":
            return True
        else:
            return False

    return True

def main():
    # Mantém o programa rodando até o usuário escolher parar
    while True:

        # Chama a função que pede os horímetros e guarda os valores retornados
        inicial, final = pedir_horimetros()

        # Valida o horímetro inicial e o final
        resultado_inicial, erro_inicial = validar_horimetro(inicial)
        resultado_final, erro_final = validar_horimetro(final)

        # Só continua o cálculo se os dois horímetros forem válidos
        if resultado_inicial and resultado_final:

            # Converte o horímetro inicial para minutos totais
            inicial_minutos = converter_para_minutos(inicial)

            # Converte o horímetro final para minutos totais
            final_minutos = converter_para_minutos(final)

            if final_minutos < inicial_minutos:
                print('Horímetro final não pode ser menor que o inicial')
                continue

            # Calcula quanto tempo passou entre o início e o fim
            diferenca = calcular_diferenca(
                inicial_minutos,
                final_minutos
            )


            if not confirmar_tempo_alto(diferenca):
                continue

            tempo_formatado = formatar_tempo(diferenca)

            corte = {
                "inicial": inicial,
                "final": final,
                "tempo": tempo_formatado
            }
            historico.append(corte)

            print(tempo_formatado)


        else:
            if not resultado_inicial:
                print(erro_inicial)

            elif not resultado_final:
                print(erro_final)


        while True:

                continuar = input("Deseja calcular outro corte? [S/N]: ")

                if continuar.lower() == "s":
                    break

                elif continuar.lower() == "n":
                    print("Programa encerrado.")
                    mostrar_historico(historico)
                    return

                else:
                    print("Digite apenas S ou N.")

if __name__ == "__main__":
    main()