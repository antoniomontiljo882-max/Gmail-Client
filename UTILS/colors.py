# STANDARD COLORS

def red(text):
    return f"\033[31m{text}\033[0m"        # red

def green(text):
    return f"\033[32m{text}\033[0m"        # green

def yellow(text):
    return f"\033[33m{text}\033[0m"        # yellow

def blue(text):
    return f"\033[34m{text}\033[0m"        # blue

def magenta(text):
    return f"\033[35m{text}\033[0m"        # magenta

def cyan(text):
    return f"\033[36m{text}\033[0m"        # cyan / light blue

def white(text):
    return f"\033[37m{text}\033[0m"        # white

def grey(text):
    return f"\033[90m{text}\033[0m"        # grey


# BRIGHT COLORS

def bright_red(text):
    return f"\033[91m{text}\033[0m"        # bright red

def bright_green(text):
    return f"\033[92m{text}\033[0m"        # bright green

def bright_yellow(text):
    return f"\033[93m{text}\033[0m"        # bright yellow

def bright_blue(text):
    return f"\033[94m{text}\033[0m"        # bright blue

def bright_magenta(text):
    return f"\033[95m{text}\033[0m"        # bright magenta

def bright_white(text):
    return f"\033[97m{text}\033[0m"        # bright white


# TEXT STYLES

def bold(text):
    return f"\033[1m{text}\033[0m"         # bold

def dim(text):
    return f"\033[2m{text}\033[0m"         # dim

def italic(text):
    return f"\033[3m{text}\033[0m"         # italic (not supported in every terminal)

def underline(text):
    return f"\033[4m{text}\033[0m"         # underline

def blink(text):
    return f"\033[5m{text}\033[0m"         # blink (often disabled)

def reverse(text):
    return f"\033[7m{text}\033[0m"         # swap foreground/background

def strikethrough(text):
    return f"\033[9m{text}\033[0m"         # strikethrough


# BACKGROUND COLORS

def bg_red(text):
    return f"\033[41m{text}\033[0m"

def bg_green(text):
    return f"\033[42m{text}\033[0m"

def bg_yellow(text):
    return f"\033[43m{text}\033[0m"

def bg_blue(text):
    return f"\033[44m{text}\033[0m"

def bg_magenta(text):
    return f"\033[45m{text}\033[0m"

def bg_cyan(text):
    return f"\033[46m{text}\033[0m"

def bg_white(text):
    return f"\033[47m{text}\033[0m"


if __name__ == "__main__":
    pass