try:
    start = int(input('start -> '))
    end = int(input('end -> '))
    for item in range(start, end):
        print(f'sum = {start} + {end} = {start + end}\navg = {}')
        start+=1
except Exception as ex:
    print(ex)