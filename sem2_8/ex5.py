tag = input()
s = input()

tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
if tag not in tags:
    print('Введен неверный тег')
else:
    print(f'<{tag}>{s}</{tag}>')
