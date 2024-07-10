from random import choice, randint
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?','Can you explain that differently?',
            'I am not sure what you mean.',
            'Could you provide more context?',
            'I\'m having trouble following that.',
            'Can you say that another way?',
            'I didn\'t catch that, could you repeat?',
            'That\'s unclear to me.',
            'I\'m confused by your statement.',
            'Sorry, I\'m not sure I get it.',
            'Could you clarify that for me?',
            'I don\'t have an answer for that.',
            'Can you give me more details?',
            'I\'m not certain what you\'re asking.',
            'Could you restate your question?',
            'I\'m not sure how to respond to that.',
            'That doesn\'t make sense to me.',
            'Could you be more specific?',
            'I need more information to understand.',
            'I\'m not following you.',
            'I don\'t quite get what you\'re saying.',
            'Could you say that in another way?',
            'I\'m not clear on what you mean.',
            'What do you mean by that?',
            'I\'m not sure what that means.',
            'I need a bit more clarity on that.',
            'That’s a bit confusing to me.',
            'I\'m sorry, could you clarify?',
            'I\'m not sure I understand.',
            'Can you explain it a little more?',
            'That’s a bit ambiguous.',
            'Can you provide more information?',
            'I\'m not getting the full picture.',
            'That\'s a bit over my head.',
            'Could you put that differently?',
            'I\'m not following your point.'])
