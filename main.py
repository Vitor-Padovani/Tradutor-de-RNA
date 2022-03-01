import functions as f


while True:
    codons = input('Digite os genes: ')

    if codons == '':
        break

    data = f.convert_codons(codons)
    #print(data)

    option = input('option: ')

    match option:
        case 'all':
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    print(f'{i}\t{data[0][i]}\t{data[1][i][0]}\t')
                else:
                    print(f'{i}\t{data[0][i]}\t-\t')

        case 'ptn':
            num = 1
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    print(f'{data[1][i][0]}', end=' - ')
                else:
                    num += 1
                    print(f'STOP [Proteína {num}]')

            print()

    #print(data)
