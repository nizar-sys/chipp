import string


main = string.ascii_lowercase


def generate_key(n, s):
    s = s.replace(" ", "")
    s = s.lower()

    key_matrix = ['' for i in range(n)]
    i = 0
    j = 0
    for c in s:
        if c in main:
            key_matrix[i] += c
            j += 1
            if(j > n-1):
                i += 1
                j = 0
    print("Kunci matrix "+"("+str(n)+'x'+str(n)+") adalah: ")
    print(key_matrix)

    key_num_matrix = []
    for i in key_matrix:
        sub_array = []
        for j in range(n):
            sub_array.append(ord(i[j])-ord('a'))
        key_num_matrix.append(sub_array)

    for i in key_num_matrix:
        print(i)
    return(key_num_matrix)


def message_matrix(s, n):
    s = s.replace(" ", "")
    s = s.lower()
    final_matrix = []
    if(len(s) % n != 0):
        while(len(s) % n != 0):
            s = s+'z'
    print("Konversi text untuk enkripsi: ", s)
    for k in range(len(s)//n):
        message_matrix = []
        for i in range(n):
            sub = []
            for j in range(1):
                # print(j)
                sub.append(ord(s[i+(n*k)])-ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("Kolom matrix dari text dalam nomor:  ")
    for i in final_matrix:
        print(i)
    return(final_matrix)


def getCofactor(mat, temp, p, q, n):
    i = 0
    j = 0
    for row in range(n):
        for col in range(n):
            if (row != p and col != q):
                temp[i][j] = mat[row][col]
                j += 1
                if (j == n - 1):
                    j = 0
                    i += 1


def determinantOfMatrix(mat, n):
    D = 0
    if (n == 1):
        return mat[0][0]

    temp = [[0 for x in range(n)]
            for y in range(n)]

    sign = 1
    for f in range(n):
        getCofactor(mat, temp, 0, f, n)
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1))
        sign = -sign
    return D


def isInvertible(mat, n):
    if (determinantOfMatrix(mat, n) != 0):
        return True
    else:
        return False


def multiply_and_convert(key, message):

    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j] += chr((res_num[i][j] % 26)+97)

    return(res_alpha)


# input 3 untuk urutan matrix
n = int(input("Urutan kuadrat matrix (3): "))
s = input("masukkan kunci contoh (XYZ ABC DEF): ")
key = generate_key(n, s)

# jika nilai kuadrat matrix lebih dari 3 misal 4
# maka kunci ditulis (XYZZ AABB CCEE YKDK)
# jika lebih dari 4 dst
# kunci harus sama dengan nilai urutan kuadrat matrix
# nilai kuadrat matrix maksimal 3, jika lebih maka pesan text akan ditambah characternya

plain_text = input("Masukkan pesan: ")
message = message_matrix(plain_text, n)
final_message = ''
for i in message:
    sub = multiply_and_convert(key, i)
    for j in sub:
        for k in j:
            final_message += k
print("Pesan: ", plain_text)
print("Pesan enkripsi: ", final_message)
