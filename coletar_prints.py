import pyautogui
import time

# Função para capturar a tela e pressionar a seta para baixo
def capturar_prints(num_capturas):
    # Verificar se o número de capturas é válido
    if num_capturas <= 0:
        print("O número de capturas deve ser maior que zero.")
        return
    
    # Loop para realizar as capturas
    for i in range(num_capturas):
        # Capturar a tela
        screenshot = pyautogui.screenshot(region=(891, 326, 86, 288))

        # Salvar o print com um nome diferente para cada captura
        screenshot.save(f'tabela {i+1}.png')
        print(f'Captura {i+1} realizada com sucesso!')
        
        # Aguardar 1 segundo antes de pressionar as setas (para garantir tempo para o movimento da tela)
        time.sleep(1)
        
        # Pressionar a tecla de seta para baixo 14 vezes
        for _ in range(14):
            pyautogui.press('down')
            time.sleep(0.5)
        
        # Aguardar 1 segundo após as teclas serem pressionadas
        time.sleep(1)

# Solicitar o número de capturas ao usuário
num_capturas = 6

# Pressionar Alt + Tab para alternar para a próxima janela
pyautogui.hotkey('alt', 'tab')

capturar_prints(num_capturas)
