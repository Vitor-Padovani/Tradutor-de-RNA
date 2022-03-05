import functions as f


while True:
    codons = ''

    #print(data)

    f.line(45)
    print("'all' - tudo | 'ptn' - proteínas | 'cdn' - códons | ' ' - sair")
    f.line(45)
    option = input('comando: ').strip()
    print()
    if option == '':
        break

    input_file = open('input/input.txt', 'r')
    output_file = open('output/output.txt', 'w')
    codons = f.format_str(input_file.read())
    data = f.convert_codons(codons)


    match option:
        case 'all':
            ptn_num = 1
            codon_num = 0

            output_file.writelines(f'Número\tCódon\tProteínas\t\n')
            output_file.writelines(f'{"-"*32}\n')
            print(f'Número\tCódon\tProteínas\t')
            f.line(25)

            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    codon_num += 1
                    print(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t')
                    output_file.writelines(f'{codon_num}\t{data[0][i]}\t{data[1][i][0]}\t\n')
                else:
                    codon_num += 1
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
        
        case 'cdn':
            cdn_num = 0
            cdn_format = 1
            for i in range(len(data[0])):
                if data[1][i][0] != 'Stop':
                    if cdn_format % 10 == 0:
                        print(f'{data[0][i]}')
                        output_file.writelines(f'{data[0][i]}\n')
                    else:
                        print(f'{data[0][i]}', end=' - ')
                        output_file.writelines(f'{data[0][i]} - ')
                    cdn_format += 1
                else:
                    cdn_num += 1
                    print(f'STOP [Proteína {cdn_num}]\n')
                    output_file.writelines(f'STOP [Proteína {cdn_num}]\n\n')
                    cdn_format = 1
                
            output_file.close()
            print()

    #print(data)


