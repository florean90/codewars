def camel_case(string):
    return "".join(word.capitalize() for word in string.split())




print(camel_case("camel case word"))