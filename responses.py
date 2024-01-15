from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Are you scared little one?'
    elif 'hello' in lowered:
        return 'Hello human.'
    else:
        return choice(['I dont get you humans...',
                                'Are you dumb?' ])