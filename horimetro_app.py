historico = []


# Pega o horimetro inical e final
def pedir_horimetros():
    horimetro_inicial = input("Horímetro inicial (HORAS:MINUTOS): ")
    horimetro_final = input("Horímetro final: (HORAS:MINUTOS): ")
    return horimetro_inicial, horimetro_final

# Validar se a entrada dos dados é correta.
def validar_horimetro(horimetro):
    try:
        ## separar horas e minutos usados com o split
        horas, minutos = horimetro.split(":")

        ## converte para número
        horas = int(horas)
        minutos = int(minutos)

        ## validar os minutos
        if minutos >= 0 and minutos <= 59:
            return True

        else:
            return False

    except:
        return False


def converter_para_minutos(horimetro):

    # aqui eu estou dividindo a entrada de dados nos ":" exemplo: 12325 horas | 25 minutos
    horas, minutos = horimetro.split(":")

    # convertendo horas e minutos para inteiros, já que ele entrou como uma String e nao tem como fazer calculo com textos
    horas = int(horas)
    minutos = int(minutos)

    #converter horas para minutos, e depois somar os minutos
    total_minutos = (horas * 60) + minutos

    return total_minutos

def calcular_diferenca(inicial_minutos, final_minutos):
    return final_minutos - inicial_minutos

def formatar_tempo(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60

    return f"Tempo de corte: {horas}h {minutos}min"

def mostrar_historico(historico):
    for corte in historico:
        print(corte["inicial"])
        print(corte["final"])
        print(corte["tempo"])



def main():
    while True:
        inicial, final = pedir_horimetros()

        resultado_inicial = validar_horimetro(inicial)
        resultado_final = validar_horimetro(final)

        if resultado_inicial and resultado_final:

            inicial_minutos = converter_para_minutos(inicial)

            final_minutos = converter_para_minutos(final)

            if final_minutos < inicial_minutos:
                print('Horímetro final não pode ser menor que o inicial')
                return

            diferenca = calcular_diferenca(inicial_minutos, final_minutos)

            tempo_formatado = formatar_tempo(diferenca)

            corte = {
                "inicial": inicial,
                "final": final,
                "tempo": tempo_formatado
            }
            historico.append(corte)

            print(tempo_formatado)

            print(historico)

        else:
            print("Horímetro inválido. Use o formato HORAS:MINUTOS")

        continuar = input(
            "Deseja calcular outro corte? [S/N]: "
        )
        if continuar.lower() != "s":
            print('Programa encerrado')

            mostrar_historico(historico)
            break



main()