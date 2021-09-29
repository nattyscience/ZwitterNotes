#import tkinter
#import tkinter as tk
#window = tk.Tk()
#window.geometry("1000x1000")
#entry = tk.Entry()
#label = tk.Label(text="Protein file name")
#entry.pack()
#label.pack()
#window.mainloop()

#import random
import random

#import parser to find sequence in FASTA file
import fastaparser
#setup variable to store sequence
my_sequence = []
with open("H1.fasta") as fasta_file:
        parser = fastaparser.Reader(fasta_file)
        for seq in parser:
            # seq is a FastaSequence object
            my_sequence = seq.sequence_as_string()
            print('Description:', seq.description)

print (my_sequence)

#Function to convert my_sequence into notes
def music(my_sequence):
    my_music = ""
    for i in my_sequence:
        number = random.randint(0, 1)
        if i == "A" and number == 0:
            my_music += "[B,E,^G]/2"
        elif i == "A" and number == 1:
            my_music += "E/2"

        if i == "C" and number == 0:
            my_music += "[b^d^f]4"
        elif i == "C" and number == 1:
            my_music += "b/2"

        if i == "D" and number == 0:
            my_music += "[^Fad]1"
        elif i == "D" and number == 1:
            my_music += "d/2"

        if i == "E" and number == 0:
            my_music += "[d^fa]1"
        elif i == "E" and number == 1:
            my_music += "^f/2"

        if i == "F" and number == 0:
            my_music += "[e^gb]/2"
        elif i == "F" and number == 1:
            my_music += "^g/2"

        if i == "G" and number == 0:
            my_music += "[gbd]/2"
        elif i == "G" and number == 1:
            my_music += "g/2"

        if i == "H" and number == 0:
            my_music += "[Gce]2"
        elif i == "H" and number == 1:
            my_music += "G/2"

        if i == "I" and number == 0:
            my_music += "[^G,BE]/2"
        elif i == "I" and number == 1:
            my_music += "B/2"

        if i == "K" and number == 0:
            my_music += "[ceg]2"
        elif i == "K" and number == 1:
            my_music += "C/2"

        if i == "L" and number == 0:
            my_music += "[E^GB]/2"
        elif i == "L" and number == 1:
            my_music += "E/2"

        if i == "M" and number == 0:
            my_music += "[^g'b'e']4"
        elif i == "M" and number == 1:
            my_music += "^g/2"

        if i == "N" and number == 0:
            my_music += "[acf]2"
        elif i == "N" and number == 1:
            my_music += "f/2"

        if i == "P" and number == 0:
            my_music += "[a^ce]2"
        elif i == "P" and number == 1:
            my_music += "^c/2"

        if i == "Q" and number == 0:
            my_music += "[cfa]2"
        elif i == "Q" and number == 1:
            my_music += "f/2"

        if i == "R" and number == 0:
            my_music += "[EGc]2"
        elif i == "R" and number == 1:
            my_music += "G/2"

        if i == "S" and number == 0:
            my_music += "[fac]1"
        elif i == "S" and number == 1:
            my_music += "a/2"

        if i == "T" and number == 0:
            my_music += "[FAC]1"
        elif i == "T" and number == 1:
            my_music += "F/2"

        if i == "V" and number == 0:
            my_music += "[e'^g'b']/2"
        elif i == "V" and number == 1:
            my_music += "e'/2"

        if i == "W" and number == 0:
            my_music += "[Gb^e]2"
        elif i == "W" and number == 1:
            my_music += "b/2"

        if i == "Y" and number == 0:
            my_music += "[^Egb]1"
        elif i == "Y" and number == 1:
            my_music += "^E/2"


    return my_music

my_music_result = music(my_sequence)

print (my_music_result)
#Function to write ABC file

def write_abc(my_music_result):
    abc_file = open("output.abc","w")
    abc_file.write("X:1\nT:Title\nM:C\nL:1/4\nK:C\n")
    abc_file.write(my_music_result)
    abc_file.close()

write_abc(my_music_result)






