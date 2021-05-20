def encrypt(message, rows):
    table = [['' for j in range(len(message))] for i in range(rows)]
    row = 0
    row_change = -1
    for i in range(len(message)):
        table[row][i] = message[i]
        if row == 0 or row == rows - 1:
            row_change *= -1
        row += row_change
    encryption = ''
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] != '':
                encryption += table[r][c]
    return encryption

def decrypt(encryption, rows):
    decryption = [' ' for i in range(len(encryption))]
    e_i = 0
    for i in range(rows):
        if i == 0:
            points = [i for i in range(len(encryption)) if i % (2 * rows - 2) == 0]
            for point in points:
                decryption[point] = encryption[e_i]
                e_i += 1
        elif i == rows - 1:
            points = [i + rows - 1 for i in range(len(encryption) - rows + 1) if i % (2 * rows - 2) == 0]
            for point in points:
                decryption[point] = encryption[e_i]
                e_i += 1
        else:
            points = [i]
            while points[-1] <= len(encryption) - 1:
                points.append(points[-1] + rows * 2 - 2 - 2 * i)
                if points[-1] <= len(encryption) - 1:
                    points.append(points[-1] + i*2)
            for point in points[:-1]:
                decryption[point] = encryption[e_i]
                e_i += 1
    return ''.join(decryption)

def test():
    message = 'poopoodoodoofart'
    print ('message = ' + message)
    encryption = encrypt(message, 6)
    print ('encryption = ' + encryption)
    decryption = decrypt(encryption, 6)
    print ('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()