import functions as f


while True:
    codons = input('Digite os genes: ')

    if codons == '':
        break

    data = f.convert_codons(codons)
    #print(data)

    output = open('output/output.txt', 'w')

    option = input('option: ')

    match option:
        case 'all':
            num = 0
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    num += 1
                    print(f'{num}\t{data[0][i]}\t{data[1][i][0]}\t')
                    output.writelines(f'{num}\t{data[0][i]}\t{data[1][i][0]}\t\n')
                else:
                    print(f'{num}\t{data[0][i]}\t-\t\n')
                    output.writelines(f'{num}\t{data[0][i]}\t-\t\n\n')
                    num = 0

            output.close()

        case 'ptn':
            num = 0
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    print(f'{data[1][i][0]}', end=' - ')
                else:
                    num += 1
                    print(f'STOP [Proteína {num}]')

            print()

    #print(data)


