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
            codon_num = 0
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    codon_num += 1
                    print(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t')
                    output.writelines(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t\n')
                else:
                    print(f'{codon_num}\t{data[0][i]}\t-\t\n')
                    output.writelines(f'{codon_num}\t{data[0][i]}\t-\t\n\n')
                    codon_num = 0

            output.close()

        case 'ptn':
            ptn_num = 0
            ptn_format = 1
            for i in range(len(data[0])):
    
                if data[1][i][0] != 'Stop':
                    if ptn_format % 10 == 0:
                        print(f'{data[1][i][0]}')
                        output.writelines(f'{data[1][i][0]}\n')
                    else:
                        print(f'{data[1][i][0]}', end=' - ')
                        output.writelines(f'{data[1][i][0]} - ')
                    ptn_format += 1
                else:
                    ptn_num += 1
                    print(f'STOP [Proteína {ptn_num}]\n')
                    output.writelines(f'STOP [Proteína {ptn_num}]\n\n')
                    ptn_format = 1
                
            output.close()

            print()

    #print(data)


