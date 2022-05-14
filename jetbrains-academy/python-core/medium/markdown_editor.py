def format_plain() -> str:
    return f'{input("Text: ")}'


def format_bold() -> str:
    return f'**{input("Text: ")}**'


def format_italic() -> str:
    return f'*{input("Text: ")}*'


def format_header() -> str:
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                if formatted:  # kludge for new-line if heading among other text
                    return f'\n{"#" * level} {input("Text: ")}\n'
                return f'{"#" * level} {input("Text: ")}\n'
            raise ValueError
        except ValueError:
            print('The level should be within the range of 1 to 6')


def format_link() -> str:
    return f'[{input("Label: ")}]({input("URL: ")})'


def format_inline_code() -> str:
    return f'`{input("Text: ")}`'


def format_new_line() -> str:
    return '\n'


formatters = {
    'plain': format_plain,
    'bold': format_bold,
    'italic': format_italic,
    'header': format_header,
    'link': format_link,
    'inline-code': format_inline_code,
    'new-line': format_new_line,
}
special_commands = {
    '!help': '',
    '!done': '',
}

formatted = list()
while True:
    chose = input('Choose a formatter: ')
    if chose in formatters:
        formatted.append(formatters[chose]())
    elif chose == '!help':
        print(f'Available formatters: {" ".join(formatters)}')
        print(f'Special commands: {" ".join(special_commands)}')
    elif chose == '!done':
        break
    else:
        # print('Unknown formatting type or command', end='')  # end='' is another kludge for tests
        print('Unknown formatting type or command')

    print(''.join(formatted))
