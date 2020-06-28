name =  input('enter the name of the music note')
c = 261.63
d = 293.66
e = 329.63
f = 349.23
g = 392.00
a = 440.00
b = 493.88
note = name[0]
octave = int(name[1])
if note == 'c':
    freq = c
elif note == 'd':
    freq = d
elif note == 'e':
    freq = e
elif note == 'f':
    freq = f
elif note == 'g':
    freq = g
elif note == 'a':
    freq = a
elif note == 'b':
    freq = b
freq = freq / 2 ** (4 - octave)
print('enter the frequncy', name, 'is', freq)