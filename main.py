import functions as f


while True:
    '''codons = input('Digite os genes: ')


    if codons == '':
        break'''
    
    codons = ''
    input_file = open('input/input.txt', 'r')
    codons = f.format_str(input_file.read())

    data = f.convert_codons(codons)
    #print(data)

    output_file = open('output/output.txt', 'w')

    option = input('option: ')
    if option == '':
        break

    match option:
        case 'all':
            ptn_num = 1
            codon_num = 0
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    codon_num += 1
                    print(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t')
                    output_file.writelines(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t\n')
                else:
                    print(f'{codon_num}\t{data[0][i]}\t-\t[Proteína {ptn_num}]\n')
                    output_file.writelines(f'{codon_num}\t{data[0][i]}\t-\t[Proteína {ptn_num}]\n\n')
                    ptn_num += 1
                    codon_num = 0

            output_file.close()

        case 'ptn':
            ptn_num = 0
            ptn_format = 1
            for i in range(len(data[0])):
    
                if data[1][i][0] != 'Stop':
                    if ptn_format % 10 == 0:
                        print(f'{data[1][i][0]}')
                        output_file.writelines(f'{data[1][i][0]}\n')
                    else:
                        print(f'{data[1][i][0]}', end=' - ')
                        output_file.writelines(f'{data[1][i][0]} - ')
                    ptn_format += 1
                else:
                    ptn_num += 1
                    print(f'STOP [Proteína {ptn_num}]\n')
                    output_file.writelines(f'STOP [Proteína {ptn_num}]\n\n')
                    ptn_format = 1
                
            output_file.close()

            print()

    #print(data)


