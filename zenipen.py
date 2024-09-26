import argparse

ZP_MAPPING = str.maketrans("zenitpolar", "polarzenit")
ZP_MAPPING_UPPER = str.maketrans("zenitpolar".upper(), "polarzenit".upper())

PIGPEN_MAPPING = {
        "a": "_|.", "A": "_|.", "b": "|_|.", "B": "|_|.", "c": "|_.", "C": "|_.",
        "d": "=|.", "D": "=|.", "e": "[].", "E": "[].", "f": "|=.", "F": "|=.",
        "g": "-|.", "G": "-|.", "h": "|-|.", "H": "|-|.", "i": "|-.", "I": "|-.",
        "j": "*_|.", "J": "*_|.", "k": "*|_|.", "K": "*|_|.", "l": "*|_.", "L": "*|_.",
        "m": "*=|.", "M": "*=|.", "n": "*[].", "N": "*[].", "o": "*|=.", "O": "*|=.",
        "p": "*-|.", "P": "*-|.", "q": "*|-|.", "Q": "*|-|.", "r": "*|-.", "R": "*|-.",
        "s": "V.", "S": "V.", "t": ">.", "T": ">.", "u": ">.", "U": "<.",
        "v": "^.", "V": "^.", "w": "*V.", "W": "*V.", "x": "*>.", "X": "*>.",
        "y": "*>.", "Y": "*<.", "z": "*^.", "Z": "*^.",
        "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": ";", "7": "&", "8": ":", "9": "(", "0": ")"
    }

def arg_parser():
    arg = argparse.ArgumentParser(description="Obfuscate your texts")

    arg.add_argument("-zp", "--zenit-polar", help="Uses Zenit Polar Cipher", action='store_true')
    arg.add_argument("-p", "--pigpen", help="Uses PigPen Cipher", action='store_true')
    arg.add_argument("-f", "--file", type=str)
    arg.add_argument("-t", "--text", type=str)
    arg.add_argument("-PA", "--print-all", action="store_true", help="Print All Cipher Mapping")
    arg.add_argument("-Pz", "--print-zenitpolar", action="store_true", help="Print Zenit Polar Cipher Mapping")
    arg.add_argument("-Pp", "--print-pigpen", action="store_true", help="Print PigPen Cipher Mapping")

    return arg.parse_args()


def obfuscate(args):
    text, opt = text_prepare(args)
    text2 = ""

    if opt == 1:
        text2 = zenit_polar(text)
    elif opt == 2:
        text2 = pigpen(text)
    elif opt == 3:
        text2 = zenit_polar(text)
        text2 = pigpen(text2)
    return text2


def zenit_polar(text):
    return text.translate(ZP_MAPPING).translate(ZP_MAPPING_UPPER)


def pigpen(text):
    obfuscated_text = ''.join(PIGPEN_MAPPING.get(char, char) for char in text)
    return obfuscated_text

def get_text(args):
    if args.text:
        return args.text
    else:
        return None


def get_file(args):
    if args.file:
        with open(args.file, "r+") as file:
            result = file.read()
            return result.strip()
    else:
        return None

def zenit_mapping():
    print("Zenit Polar Mapping".upper())
    print({chr(k): chr(v) for k, v in ZP_MAPPING.items()})
    print({chr(k): chr(v) for k, v in ZP_MAPPING_UPPER.items()})

def pigpen_mapping():
    print("PigPen Mapping".upper())
    print(PIGPEN_MAPPING)

def text_prepare(args):
    opt = 0
    text = ""

    if args.zenit_polar and args.pigpen:
        opt = 3
    elif not args.pigpen:
        opt = 1
    elif not args.zenit_polar:
        opt = 2

    if args.file:
        text = get_file(args)

    elif args.text:
        text = get_text(args)

    return text, opt

if __name__ == '__main__':
    print("""
███████╗███████╗███╗   ██╗██╗██████╗ ███████╗███╗   ██╗
╚══███╔╝██╔════╝████╗  ██║██║██╔══██╗██╔════╝████╗  ██║
  ███╔╝ █████╗  ██╔██╗ ██║██║██████╔╝█████╗  ██╔██╗ ██║
 ███╔╝  ██╔══╝  ██║╚██╗██║██║██╔═══╝ ██╔══╝  ██║╚██╗██║
███████╗███████╗██║ ╚████║██║██║     ███████╗██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝
                        Created by: Leonardo Oi                   
    """)
    args = arg_parser()
    if args.print_zenitpolar or args.print_pigpen or args.print_all:
        if args.print_all:
            print("----------------------------------------------------------------------------------------------------")
            zenit_mapping()
            print("----------------------------------------------------------------------------------------------------")
            pigpen_mapping()
            print("----------------------------------------------------------------------------------------------------")

        elif args.print_zenitpolar:
            zenit_mapping()
        elif args.print_pigpen:
            pigpen_mapping()
    else:
        print(obfuscate(args))
