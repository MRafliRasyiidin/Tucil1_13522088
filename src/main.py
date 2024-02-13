import time
import random
import os

def solve(coordinat, length, vertical):
    if length < buffer_size:
        if vertical:
            for i in range(row):
                if (i+1, coordinat+1) not in temp_coordinat:
                    temp_sequence.append(m[i][coordinat])
                    temp_coordinat.append((i+1, coordinat+1))
                    compare_sequence(temp_sequence)
                    solve(i, length+1, False)
                    temp_sequence.pop()
                    temp_coordinat.pop()
        else:
            for i in range(col):
                if (coordinat+1, i+1) not in temp_coordinat:
                    temp_sequence.append(m[coordinat][i])
                    temp_coordinat.append((coordinat+1, i+1))
                    compare_sequence(temp_sequence)
                    solve(i, length+1, True)
                    temp_sequence.pop()
                    temp_coordinat.pop()

def compare_sequence(sequence):
    global count
    global max_point
    global sequence_solution
    global coordinat_solution
    if check_sequence(sequence):
        if point > max_point:
            max_point = point
            sequence_solution = []
            coordinat_solution = []
            for i in range (len(sequence)):
                sequence_solution.append(sequence[i])
                coordinat_solution.append(temp_coordinat[i])
        elif point == max_point:
            if len(sequence) < len(sequence_solution):
                max_point = point
                sequence_solution = []
                coordinat_solution = []
                for i in range (len(sequence)):
                    sequence_solution.append(sequence[i])
                    coordinat_solution.append(temp_coordinat[i])

            
        count += 1

def check_sequence(sequence):
    global point
    point = 0
    check2 = False
    for i in range(len(m_sequences)):
        check = False
        if len(sequence) >= len(m_sequences[i][0]):
            for j in range (len(sequence)):
                if sequence[j] == m_sequences[i][0][0]:
                    k = 0
                    check = True
                    while k < len(m_sequences[i][0]) and check:
                        if j+k<len(sequence):
                            if sequence[j+k] != m_sequences[i][0][k]:
                                check = False
                            else:
                                k += 1
                        else:
                            check = False
                    if check:
                        point += m_sequences[i][1]
                        check2 = True
                        break
    return check2

def save():
    filename = str(input("Masukkan nama file (contoh: hasil.txt): "))
    save_path = "../test/" + filename
    savefile = open(save_path, "w")
    savefile.write(f"{max_point}\n")
    for element in sequence_solution:
        savefile.write(f"{element} ")
    savefile.write("\n")
    for element in coordinat_solution:
        savefile.write(f"{element[0]}, {element[1]}\n")
    print("\nSolusi berhasil disimpan!")
    savefile.close()
    
def solution_output():
    print(f""" .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ____     | || | _____  _____ | || | ____  _____  | || |  ________    | |
| | |_   ___  |  | || |   .'    `.   | || ||_   _||_   _|| || ||_   \|_   _| | || | |_   ___ `.  | |
| |   | |_  \_|  | || |  /  .--.  \  | || |  | |    | |  | || |  |   \ | |   | || |   | |   `. \ | |
| |   |  _|      | || |  | |    | |  | || |  | '    ' |  | || |  | |\ \| |   | || |   | |    | | | |
| |  _| |_       | || |  \  `--'  /  | || |   \ `--' /   | || | _| |_\   |_  | || |  _| |___.' / | |
| | |_____|      | || |   `.____.'   | || |    `.__.'    | || ||_____|\____| | || | |________.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  """)
    print("\nResult")
    print(f"Maximum reward: {max_point}")
    print("Token combination: ", end="")
    for element in sequence_solution:
        print(element, end=" ")
    print()
    for i in range(len(coordinat_solution)):
        print(f"({coordinat_solution[i][1]},{coordinat_solution[i][0]})")

def no_solution_output():
    print(f""" .-----------------. .----------------.  .----------------.     .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. |   | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || |     ____     | || |  _________   | |   | |  _________   | || |     ____     | || | _____  _____ | || | ____  _____  | || |  ________    | |
| ||_   \|_   _| | || |   .'    `.   | || | |  _   _  |  | |   | | |_   ___  |  | || |   .'    `.   | || ||_   _||_   _|| || ||_   \|_   _| | || | |_   ___ `.  | |
| |  |   \ | |   | || |  /  .--.  \  | || | |_/ | | \_|  | |   | |   | |_  \_|  | || |  /  .--.  \  | || |  | |    | |  | || |  |   \ | |   | || |   | |   `. \ | |
| |  | |\ \| |   | || |  | |    | |  | || |     | |      | |   | |   |  _|      | || |  | |    | |  | || |  | '    ' |  | || |  | |\ \| |   | || |   | |    | | | |
| | _| |_\   |_  | || |  \  `--'  /  | || |    _| |_     | |   | |  _| |_       | || |  \  `--'  /  | || |   \ `--' /   | || | _| |_\   |_  | || |  _| |___.' / | |
| ||_____|\____| | || |   `.____.'   | || |   |_____|    | |   | | |_____|      | || |   `.____.'   | || |    `.__.'    | || ||_____|\____| | || | |________.'  | |
| |              | || |              | || |              | |   | |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |   | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'     '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)
    print("\nResult")
    print("Maximum reward: 0")
    print("No solution was found!")

def printBreachProtocol():
    print("""d8888b. d8888b. d88888b  .d8b.   .o88b. db   db                     
88  `8D 88  `8D 88'     d8' `8b d8P  Y8 88   88                     
88oooY' 88oobY' 88ooooo 88ooo88 8P      88ooo88                     
88~~~b. 88`8b   88~~~~~ 88~~~88 8b      88~~~88                     
88   8D 88 `88. 88.     88   88 Y8b  d8 88   88                     
Y8888P' 88   YD Y88888P YP   YP  `Y88P' YP   YP                     
                                                                    
                                                                    
d8888b. d8888b.  .d88b.  d888888b  .d88b.   .o88b.  .d88b.  db      
88  `8D 88  `8D .8P  Y8. `~~88~~' .8P  Y8. d8P  Y8 .8P  Y8. 88      
88oodD' 88oobY' 88    88    88    88    88 8P      88    88 88      
88~~~   88`8b   88    88    88    88    88 8b      88    88 88      
88      88 `88. `8b  d8'    88    `8b  d8' Y8b  d8 `8b  d8' 88booo. 
88      88   YD  `Y88P'     YP     `Y88P'   `Y88P'  `Y88P'  Y88888P 
                                                                    
                                                                    """)


programLoop = True
while programLoop:
    count = 0 
    max_point = 0
    sequence_solution = []
    coordinat_solution = []
    print()
    printBreachProtocol()
    print("Silakan pilih metode input:")
    print("1. File")
    print("2. CLI")
    print("3. Exit program")
    pick = input(">> ")
    print()

    if pick == "1":
        checkError = False
        checkReadedSequence = True
        nama_file = input(str("Masukkan nama file: "))
        print()
        path = '../test/' + nama_file
        while not os.path.exists(path):
            print("File tidak ditemukan, periksa kembali nama file!\n")
            nama_file = input(str("Masukkan nama file: "))
            print()
            path = '../test/' + nama_file
        fp = open(path, "r")
        start = time.time()
        try:
            buffer_size = int(fp.readline())    # read buffer size
        except ValueError:
            print("Error: Ukuran buffer tidak valid")
            checkError = True
        try:
            temp_line = fp.readline()
            col, row = int(temp_line.split()[0]), int(temp_line.split()[1])
            m = [[0 for i in range(col)] for j in range(row)]
        except ValueError:
            print("Error: Ukuran matriks tidak valid")
            checkError = True
        else:
            try:
                for i in range (col):         # read Breach Protocol Matrix
                    temp_line = fp.readline()
                    col = 0
                    for word in temp_line.split():
                        if len(word) != 2:
                            print("Error: panjang token pada matriks tidak valid")
                            checkReadedSequence = False
                        if not word.isalnum():
                            print("Error: token terdiri dari karakter non alfanumerik")
                            checkReadedSequence = False
                        m[i][col] = word
                        col += 1
            except:
                print("Error: Jumlah kolom tidak sesuai")
                checkError = True
            else:
                try:
                    num_of_sequences = int(fp.readline().split()[0])    # read the sequence and the reward
                except ValueError:
                    print("Error: jumlah sequence tidak valid")
                    checkError = True
                else:
                    m_sequences = []
                    for i in range (num_of_sequences):
                        temp_line = fp.readline()
                        sequences = []
                        for word in temp_line.split():
                            if len(word) != 2:
                                print("Error: panjang token pada sequence tidak valid")
                                checkReadedSequence = False
                            if not word.isalnum():
                                print("Error: token terdiri dari karakter non alfanumerik")
                                checkReadedSequence = False
                            sequences.append(word)
                        try:
                            m_sequences.append((sequences, int(fp.readline())))
                        except ValueError:
                            print("Error: nilai reward tidak valid")
                            checkError = True
        if not checkError and checkReadedSequence:
            pass
        else:
            print("Silakan periksa kembali file yang akan digunakan!")
            checkError = False
            checkReadedSequence = True
            fp.close()
            continue
        # wdth = col
        # height = row

        temp_sequence = []
        temp_coordinat = []

        for i in range(col):
            temp_sequence.append(m[0][i])
            temp_coordinat.append((1, i+1))
            solve(i, 1, True)
            temp_sequence.pop()
            temp_coordinat.pop()

        if max_point != 0:
            solution_output()
        else:
            no_solution_output()

        end = time.time()
        td = (end-start)
        print(f"\n{td*1000:.03f} ms\n")

        print("Apakah Anda ingin menyimpan solusi? (y/n)")
        status = False
        while not status:
            choose = str(input(">> "))
            if choose == "y":
                save()
                status = True
            elif choose == "n":
                status = True
            else:
                print("Masukkan y atau n saja!")

        fp.close()

    elif pick == "2":
        checkReadedSequence = True
        try:
            number_of_tokens = int(input("Masukkan jumlah token: "))
            token_list = str(input("Masukkan token dalam 1 baris: ")).split()
            if len(token_list) != number_of_tokens:
                print()
                print("Error: banyak token tidak sesuai")
                print("Periksa kembali masukan yang diberikan!")
                continue
            for i in range(number_of_tokens):
                if not token_list[i].isalnum():
                    print()
                    print("Error: token terdiri dari karakter non alfanumerik")
                    print("Periksa kembali masukan yang diberikan!")
                    checkReadedSequence = False
                    break
                if len(token_list[i]) != 2:
                    print()
                    print("Error: panjang token tidak valid")
                    print("Periksa kembali masukan yang diberikan!")
                    checkReadedSequence = False
                    break
                if len(token_list) != len(set(token_list)):
                    print()
                    print("Error: token tidak unik")
                    print("Periksa kembali masukan yang diberikan!")
                    checkReadedSequence = False
                    break
            if not checkReadedSequence:
                continue
            buffer_size = int(input("Masukkan panjang buffer maksimal: "))
            matrix_size = str(input('Masukkan ukuran matriks dengan format "baris kolom" (contoh: 6 6): ')).split()
            number_of_sequence = int(input("Masukkan jumlah sequence: "))
            max_sequence_size = int(input("Masukkan panjang maksimal sequence: "))
        except ValueError:
            print()
            print("Error: masukan tidak valid")
            print("Periksa kembali masukan yang diberikan!")
            continue
        start = time.time()

        row = int(matrix_size[0])
        col = int(matrix_size[1])
        m = [[random.choice(token_list) for i in range(col)] for j in range(row)]
        print()
        print("Matrix:")
        for i in range(row):
            for j in range(col):
                print(m[i][j], end=" ")
            print()

        checkSame = False
        m_sequences = []
        print("\nSequence:")
        for i in range(number_of_sequence):
            sequence_length = random.randint(2, max_sequence_size)
            sequence = []
            for j in range(sequence_length):
                sequence.append(random.choice(token_list))
            reward = random.randint(0, 100)
            for j in range(len(m_sequences)):
                if sequence == m_sequences[j][0]:
                    checkSame = True
                    break
            if checkSame:
                continue
            m_sequences.append((sequence, reward))
            for element in m_sequences[i][0]:
                print(element, end=" ")
            print(f"({m_sequences[i][1]})")
        if checkSame:
            print("\nAda sequence yang tidak unik, sequence telah dihapus dan jumlah sequence telah dikurangi")
        print()

        temp_sequence = []
        temp_coordinat = []

        for i in range(col):
            temp_sequence.append(m[0][i])
            temp_coordinat.append((1, i+1))
            solve(i, 1, True)
            temp_sequence.pop()
            temp_coordinat.pop()

        if max_point != 0:
            solution_output()
        else:
            no_solution_output()

        end = time.time()
        td = (end-start)
        print(f"\n{td:.03f} ms\n")

        print("Apakah Anda ingin menyimpan solusi? (y/n)")
        status = False
        while not status:
            choose = str(input(">> "))
            if choose == "y":
                save()
                status = True
            elif choose == "n":
                status = True
            else:
                print("Masukkan y atau n saja!")
    elif pick == "3":
        programLoop = False
    else:
        print("Masukan tidak valid!")
