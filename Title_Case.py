def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# def title_case(title, minor_words=''):
#     if title in ("", None):
#         return ""
#     title = title.lower().split()
#     minor_words = minor_words.lower().split()
#     return " ".join([title[0].capitalize()] + [i if i in minor_words else i.capitalize() for i in title[1:] ])





print(title_case('THE WIND IN THE WILLOWS', 'The In'))