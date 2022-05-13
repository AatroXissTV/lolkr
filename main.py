# imports
from pynput.keyboard import Events, Key, Controller
from googletrans import Translator


def translate(message):
    translator = Translator()
    translation = translator.translate(message, dest='ko')
    return translation.text


def rewrite(src_message, message):
    print(src_message)
    print(message)
    keyboard = Controller()
    for i in range(len(src_message) + 1):
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    keyboard.type(message)


with Events() as user_inputs:
    n = 0
    src_message = ""

    for input in user_inputs:
        if isinstance(input, Events.Press):
            if input.key == Key.enter:
                n += 1
                print(f"Enter pressed n°{n}")
            else:
                if isinstance(input.key, Key) and n > 0:
                    if input.key == Key.space:
                        src_message += " "
                    elif input.key == Key.backspace:
                        src_message = src_message[:-1]
                    elif input.key == Key.esc:
                        src_message = ""
                elif n > 0:
                    if input.key.char == ",":
                        message = translate(src_message)
                        rewrite(src_message, message)
                    else:
                        src_message += input.key.char
            if n == 2:
                n = 0
                src_message = ""
