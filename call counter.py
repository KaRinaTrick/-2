calls = 0


def count_calls():
    global calls
    calls += 1



def string_info(string):
    string = ((len(string)), string.upper(), string.lower())
    print(tuple(string))
    count_calls()


def is_contains(string, list_to_search):
    list_to_search = [i.upper() for i in list_to_search]
    string = string.upper()
    if string in list_to_search:
        print(True)
    else:
        print(False)
    print(string, list_to_search)
    count_calls()


string_info('Capybara')
string_info('Armageddon')
string_info('Karina')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
