import flet as ft
from horimetro_app import(
    validar_horimetro,
    converter_para_minutos,
    calcular_diferenca,
    formatar_tempo,
)

def main (page: ft.Page):

   page.title = "Calculadora de Horímetro"


   horas_inicial = ft.TextField(label="Horímetro onicial")
   minutos_inicial = ft.TextField(label="Minutos inicial", max_lenght=2)

   horas_final = ft.TextField(label="Horímetro final")
   minutos_final = ft.TextField(label="Minutos final", max_lenght=2)

   resultado = ft.Text("")

   botao = ft.ElevatedButton("Calcular")


   def calcular(e):
       inicial = f"{horas_inicial.value}:{minutos_inicial.value}"
       final = f"{horas_final.value}:{minutos_final.value}"

       resultado_inicial, erro_inicial = validar_horimetro(inicial)
       resultado_final, erro_final = validar_horimetro(final)

       page.add()

ft.app(target=main)


