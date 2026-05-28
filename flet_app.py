import flet as ft

def main (page: ft.Page):

   campo = ft.TextField(
       label="Horímetro Inicial"
   )
   campo_2 = ft.TextField(
       label="Horímetro Final"
   )
   botao = ft.ElevatedButton("Calcular")

   page.add(campo,
            campo_2,
            botao)

ft.app(target=main)