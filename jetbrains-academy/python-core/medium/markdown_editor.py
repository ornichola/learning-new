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
                if formatted:
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


def format_list(format_type: str) -> [str]:
    rows = list()
    while True:
        rows_num = input('Number of rows: ')
        try:
            rows_num = int(rows_num)
            if rows_num >= 1:
                for i in range(rows_num):
                    prefix = f'{i + 1}.' if format_type == 'ordered-list' else '*'
                    rows.append(f'{prefix} {input(f"Row #{i + 1}: ")}\n')
                return rows
            raise ValueError
        except ValueError:
            print('The number of rows should be greater than zero')


formatters = {
    'plain': format_plain,
    'bold': format_bold,
    'italic': format_italic,
    'header': format_header,
    'link': format_link,
    'inline-code': format_inline_code,
    'new-line': format_new_line,
    'ordered-list': format_list,
    'unordered-list': format_list,
}
special_commands = {
    '!help': '',
    '!done': '',
}

formatted = list()
while True:
    chose = input('Choose a formatter: ')
    if chose in formatters:
        if chose in ('ordered-list', 'unordered-list'):
            formatted.extend(formatters[chose](chose))
        else:
            formatted.append(formatters[chose]())
    elif chose == '!help':
        print(f'Available formatters: {" ".join(formatters)}')
        print(f'Special commands: {" ".join(special_commands)}')
    elif chose == '!done':
        with open('output.md', 'w') as f:
            f.write(''.join(formatted))
        break
    else:
        print('Unknown formatting type or command')

    print(''.join(formatted))
