import flet as ft
from horimetro_app import(
    validar_horimetro,
    converter_para_minutos,
    calcular_diferenca,
    formatar_tempo,
)

def main (page: ft.Page):

   page.title = "Calculadora de Horímetro - Cs3 Revestimentos"


   page.horizontal_alignment =(
       ft.CrossAxisAlignment.CENTER)

   page.vertical_alignment = (
       ft.MainAxisAlignment.CENTER
   )

   def somente_numeros(e):
       valor = "".join(
           caractere for caractere in e.control.value
           if caractere.isdigit()
       )

       if e.control in [minutos_inicial, minutos_final]:
           valor = valor[:2]

       e.control.value = valor
       page.update()

   horas_inicial = ft.TextField(
       label="Horas",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=300
   )

   minutos_inicial = ft.TextField(

       label="Minutos",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=100

   )

   horas_final = ft.TextField(
       label="Horas",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=300
   )

   minutos_final = ft.TextField(
       label="Minutos",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=100,

   )

   resultado = ft.Text(
       "",
       size=22,
       weight=ft.FontWeight.BOLD,)


   mensagem = ft.Text("")



   def calcular(e):

       inicial = f"{horas_inicial.value}:{minutos_inicial.value}"

       final = f"{horas_final.value}:{minutos_final.value}"

       resultado_inicial, erro_inicial = validar_horimetro(inicial)

       resultado_final, erro_final = validar_horimetro(final)

       if not resultado_inicial:
            mensagem.value = erro_inicial
            resultado.value = ""
            page.update()
            return

       if not resultado_final:
           mensagem.value = erro_final
           resultado.value = ""
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

       if diferenca >= 40 * 60:
           mensagem.value = "Atenção: o tempo de corte está acima do padrão esperado. Verifique os horímetros."
           resultado.value = formatar_tempo(diferenca)
           page.update()
           return

       resultado.value = formatar_tempo(diferenca)


       page.update()


   botao_calcular = ft.Button(
       "Calcular",

        icon=ft.Icons.CALCULATE,
        on_click=calcular,
        width=430,

       style=ft.ButtonStyle(
           text_style=ft.TextStyle(
           size=20,
           weight=ft.FontWeight.BOLD)
       )

   )
   titulo = ft.Text(
       "Calculadora de Horímetro",
       size=28,
       weight=ft.FontWeight.BOLD
       )


   page.add(
       ft.Column(
           [
               titulo,

               ft.Row([horas_inicial, minutos_inicial],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER,
                      spacing=20),

               ft.Row([horas_final, minutos_final],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER,
                      spacing=20
                      ),

               botao_calcular,
               resultado,
               mensagem,


           ],
           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
           spacing=20,
       )
   )

ft.run(main)


