import functions as f


while True:
    codons = input('Digite os genes: ')

    if codons == '':
        break

    data = f.convert_codons(codons)

    print(data)

    for i in range(len(data[0])):
        print(f'{data[0][i]}\t{data[1][i][0]}\t')
