import sys
from pathlib import Path

import flet as ft

from horimetro_app import(
    validar_horimetro,
    converter_para_minutos,
    calcular_diferenca,
    formatar_tempo,
)

def asset_path(nome):
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return base / "assets" / nome
historico = []

historico_visual = ft.Column(
    [],
    spacing=5,
    scroll=ft.ScrollMode.AUTO,
    height=180,
)

def main (page: ft.Page):

   page.title = "Calculadora de Horímetro - Cs3 Revestimentos"
   page.window.icon = str(asset_path("icone.ico"))

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
       width=300,
       height=55,
   )

   minutos_inicial = ft.TextField(

       label="Minutos",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=100,
       height=55,

   )

   horas_final = ft.TextField(
       label="Horas",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=300,
       height=55,
   )

   minutos_final = ft.TextField(
       label="Minutos",
       keyboard_type=ft.KeyboardType.NUMBER,
       on_change=somente_numeros,
       width=100,
       height=55,

   )

   resultado = ft.Text(
       "",
       color="#4ADE80",
       size=22,
       weight=ft.FontWeight.BOLD,)


   mensagem = ft.Text("",
                      color="#F87171",
                      size=14,
                      )




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

       corte = {
           "inicial": inicial,
           "final": final,
           "tempo": resultado.value
       }

       historico.append(corte)

       historico_visual.controls.append(
           ft.Text(
               f"{inicial} -> {final} | {resultado.value}",
               size=13,
               color="#CBD5E1"
           )
       )
       mensagem.value = ""

       page.update()



   botao_calcular = ft.Button(
       content=ft.Row(
           [
               ft.Icon(ft.Icons.CALCULATE, size=28),

               ft.Text(
                   "Calcular",
                   size=24,
                   weight=ft.FontWeight.BOLD
               ),
           ],
           alignment=ft.MainAxisAlignment.CENTER,
           spacing=8,
       ),
       on_click=calcular,

       width=520,
       height=55,

       style=ft.ButtonStyle(
           bgcolor="#2563EB",
           color="white",
       )

   )
   titulo = ft.Text(
       "Calculadora de Horímetro",
       size=28,
       height=75,
       weight=ft.FontWeight.BOLD,

       )


   page.add(


     ft.Container(

           content=ft.Column(
               [
                   titulo,


                    ft.Text(
                       "Horímetro Inicial",
                       size=18,
                       weight=ft.FontWeight.BOLD,
                       color="#60A5FA"
                   ),

                   ft.Row([horas_inicial, minutos_inicial],
                          alignment=ft.MainAxisAlignment.CENTER,
                          vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=20
                          ),

                   ft.Text(
                       "Horímetro Final",
                       size=18,
                       weight=ft.FontWeight.BOLD,
                       color="#4ADE80"
                   ),


                   ft.Row([horas_final, minutos_final],
                          alignment=ft.MainAxisAlignment.CENTER,
                          vertical_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=20
                          ),

                   botao_calcular,
                   ft.Container(height=10),

                   resultado,
                   mensagem,
                   ft.Text(
                       "Histórico",
                       size=23,
                       weight=ft.FontWeight.BOLD,
                       color="#CBD5E1"
                   ),
                   historico_visual,

                   ft.Row(
                       [
                           ft.Text(
                               "Desenvolvido por Tiago",
                               size=12,
                               color="#94A3B8",
                           ),
                           ft.TextButton(
                               "GitHub",
                               url="https://github.com/Kishimura",
                           ),
                       ],
                       alignment=ft.MainAxisAlignment.CENTER,
                   ),



               ],
               horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               spacing=20,
               ),
           padding=30,
           border_radius=20,
           bgcolor="#111827",
           width=620,

           shadow=ft.BoxShadow(
             blur_radius=30,
             color="#000000",
             spread_radius=1,
         )


          )
     )
ft.run(main)