try:
    start = int(input('start -> '))
    end = int(input('end -> '))
    while start<= end:
        start+=1
        print(f'sum = {start} + {start} = {start + start}')
except Exception as ex:
    print(ex)