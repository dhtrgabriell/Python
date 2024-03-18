import flet

# Título: HashZap
# Botão de iniciar Chat
    # Clicou no botão
        # Popup / Modal
            # Título: Bem Vindo ao HashZap
            # Campo: Escreva seu nome
            # Botão: Entrar no Chat
# Chat
# Embaixo do Chat
    # Campo: Digite sua mensagem
    # Botão: Enviar

def main(pagina):
    texto = flet.Text('HashZap')

    chat = flet.Column()

    def enviar_mensagem(evento):
        texto_mensagem = flet.Text(campo_mensagem.value)
        chat.controls.append(texto_mensagem)
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = flet.TextField(label='Digite sua mensagem')
    botao_enviar = flet.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = flet.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        texto_entrou = flet.Text((f'{nome_usuario.value} entrou no chat.'))
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(texto_entrou)
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = flet.Text('Bem Vindo ao HashZap')
    nome_usuario = flet.TextField(label='Escreva seu nome')
    botao_entrar = flet.ElevatedButton('Entrar no Chat', on_click=entrar_chat)

    popup = flet.AlertDialog(
        open=False,
        modal=True,
        title= titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = flet.ElevatedButton('Iniciar Chat', on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

flet.app(target=main)