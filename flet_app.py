import flet as ft
from horimetro_app import(
    validar_horimetro,
    converter_para_minutos,
    calcular_diferenca,
    formatar_tempo,
    confirmar_tempo_alto
)

def main (page: ft.Page):

   page.title = "Calculadora de Horímetro - Cs3 Revestimentos"


   horas_inicial = ft.TextField(
       label="Horímetro inicial",
       keyboard_type=ft.KeyboardType.NUMBER
   )

   minutos_inicial = ft.TextField(
       label="Minutos inicial",
       max_length=2,
       keyboard_type=ft.KeyboardType.NUMBER
   )

   horas_final = ft.TextField(
       label="Horímetro final",
       keyboard_type=ft.KeyboardType.NUMBER
   )

   minutos_final = ft.TextField(
       label="Minutos final",
       max_length=2,
       keyboard_type=ft.KeyboardType.NUMBER
   )

   resultado = ft.Text("")



   def calcular(e):

       inicial = f"{horas_inicial.value}:{minutos_inicial.value}"

       final = f"{horas_final.value}:{minutos_final.value}"

       resultado_inicial, erro_inicial = validar_horimetro(inicial)

       resultado_final, erro_final = validar_horimetro(final)

       if not resultado_inicial:
            resultado.value = erro_inicial
            page.update()
            return

       if not resultado_final:
           resultado.value = erro_final
           page.update()
           return

       inicial_minutos = converter_para_minutos(inicial)

       final_minutos = converter_para_minutos(final)

       if final_minutos < inicial_minutos:
           resultado.value = (
               "Horímetro final não pode ser menor que o inicial."
           )

           page.update()

           return

       diferenca = calcular_diferenca(
           inicial_minutos,
           final_minutos
       )


       resultado.value = formatar_tempo(diferenca)

       page.update()


   botao_calcular = ft.ElevatedButton(
       "Calcular",
        on_click=calcular
   )



   page.add(

ft.Row([
           horas_inicial,
           minutos_inicial
       ]),

        ft.Row([
           horas_final,
           minutos_final
       ]),

       botao_calcular,

       resultado

   )


ft.app(target=main)


