# Emoji Converter Game
emojies = {
    ':)': '😄',
    ':(': '😢',
}

while True:
    message = input('> ')
    if message == 'quit':
        print('You quit the Emoji Converter')
        break
    else:
        messages = message.split(' ')
        converted_msg = ''
        for msg in messages:
            converted_msg += f'{emojies.get(msg, msg)} '  # get(key, defaultValue) --> defaultValue is optional
        print(converted_msg)
