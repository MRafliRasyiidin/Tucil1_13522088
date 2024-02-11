import numpy as np
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
    filename = str(input("Masukkan nama file: "))
    save_path = "../test/" + filename
    savefile = open(save_path, "w")
    savefile.write(f"{max_point}\n")
    for element in sequence_solution:
        savefile.write(f"{element} ")
    savefile.write("\n")
    for element in coordinat_solution:
        savefile.write(f"{element[0]}, {element[1]}\n")
    savefile.close()
    
def solution_output():
    print(f"""\n .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
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

count = 0 
max_point = 0
sequence_solution = []
coordinat_solution = []



print("Silakan pilih metode input:")
print("1. File")
print("2. CLI")
pick = int(input(">> "))

if pick == 1:

    nama_file = input(str("Masukkan nama file: "))
    path = '../test/' + nama_file
    while not os.path.exists(path):
        print("File tidak ditemukan, periksa kembali nama file!\n")
        nama_file = input(str("Masukkan nama file: "))
        path = '../test/' + nama_file

    fp = open(path, "r")
    start = time.time()

    buffer_size = int(fp.readline())    # read buffer size
    temp_line = fp.readline()
    col, row = int(temp_line.split()[0]), int(temp_line.split()[1])
    m = [[0 for i in range(col)] for j in range(row)]
    for i in range (col):         # read matrix Breach Protocol
        temp_line = fp.readline()
        col = 0
        for word in temp_line.split():
            m[i][col] = word
            col += 1

    num_of_sequences = int(fp.readline().split()[0])    # read the sequence and the reward
    m_sequences = []
    for i in range (num_of_sequences):
        temp_line = fp.readline()
        sequences = []
        for word in temp_line.split():
            sequences.append(word)
        m_sequences.append((sequences, int(fp.readline())))

    # width = col
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

elif pick == 2:
    
    number_of_tokens = int(input())
    token_list = str(input()).split()
    buffer_size = int(input())
    matrix_size = str(input()).split()
    number_of_sequence = int(input())
    max_sequence_size = int(input())

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
    
    m_sequences = []
    print("\nSequence:")
    for i in range(number_of_sequence):
        sequence_length = random.randint(2, max_sequence_size)
        sequence = []
        for j in range(sequence_length):
            sequence.append(random.choice(token_list))
        reward = random.randint(0, 100)
        m_sequences.append((sequence, reward))
        for element in m_sequences[i][0]:
            print(element, end=" ")
        print(f"({m_sequences[i][1]})")

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

else:
    print("Masukkan tidak valid!")


