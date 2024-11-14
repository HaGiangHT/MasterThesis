
with open("filenames-of-20240118_13h07m15s.txt", "rt") as fin:
    with open("filenames-of-20240118_13h07m15s_txt.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('.jpg', '.txt'))

