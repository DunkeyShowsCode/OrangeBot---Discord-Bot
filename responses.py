import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'hey there!'

    if p_message == '!roll':
        return str(random.randint(1, 20))

    if p_message == '!help':
        return '`To talk to BotOrange use the commands below`\n' \
               '`!Hello: to have bot say hello.`\n' \
               '`!Roll: to have bot roll a 1-20 dice.`\n' \
               '`!help: for help message.`\n' \
               '`Bot detects if someone edits their message and documents the message.`'
