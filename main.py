try:
    sign = input('sign-> ' )
    lenght = int(input('lenght-> '))
    trigger = input('trigger [vertical - v | horizontal - h]-> ')
    for item in range(0,lenght):
        if trigger == 'v':
            print(sign)
        elif trigger == 'h':
            print(sign, end='')
        else:
            raise Exception('Incorrect choose of trigger')
except Exception as ex:
    print (f'Error information: {ex}')