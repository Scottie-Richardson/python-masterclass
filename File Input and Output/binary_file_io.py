# When manipulating a non-text file you must include both the type of
#   file and the method i.e. 'br' for read binary, 'bw' for write binary
with open("File Input and Output\\binary", 'bw') as bin_in_file:
    # When actually writing to the file you have to convert
    #   the data into bytes, one way is with the bytes() function
    bin_in_file.write(bytes(range(20)))

with open("File Input and Output\\binary", 'br') as bin_out_file:
    for b in bin_out_file:
        print(b)

# Another way to write to a binary file is with
#   the to_bytes() and from_bytes() functions

# The integer and hexadecimal representations
a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
d = 2998302     # 02 2D C0 1E

with open('File Input and Output\\binary_2', 'bw') as bin_in_file:
    bin_in_file.write(a.to_bytes(2, 'big'))
    bin_in_file.write(a.to_bytes(2, 'little'))
    bin_in_file.write(b.to_bytes(2, 'big'))
    bin_in_file.write(b.to_bytes(2, 'little'))
    bin_in_file.write(c.to_bytes(4, 'big'))
    bin_in_file.write(c.to_bytes(4, 'little'))
    bin_in_file.write(d.to_bytes(4, 'big'))
    bin_in_file.write(d.to_bytes(4, 'little'))

# Without knowing how the data was stored into binary initally, you can get
#   radically different data returned compared to what was initally stored
with open('File Input and Output\\binary_2', 'br') as bin_out_file:
    z = int.from_bytes(bin_out_file.read(2), 'big')
    y = int.from_bytes(bin_out_file.read(2), 'big')
    w = int.from_bytes(bin_out_file.read(2), 'big')
    v = int.from_bytes(bin_out_file.read(2), 'big')
    u = int.from_bytes(bin_out_file.read(4), 'big')
    t = int.from_bytes(bin_out_file.read(4), 'big')
    s = int.from_bytes(bin_out_file.read(4), 'big')
    r = int.from_bytes(bin_out_file.read(4), 'big')
    print("65534 stored as a binary using 'big' format and returned in 'big' format:", end=" ")
    print(z)
    print("65534 stored as a binary using 'little' format and returned in 'big' format:", end=" ")
    print(y)
    print("65535 stored as a binary using 'big' format and returned in 'big' format:", end=" ")
    print(w)
    print("65535 stored as a binary using 'little' format and returned in 'big' format:", end=" ")
    print(v)
    print("65536 stored as a binary using 'big' format and returned in 'big' format:", end=" ")
    print(u)
    print("65536 stored as a binary using 'little' format and returned in 'big' format:", end=" ")
    print(t)
    print("2998302 stored as a binary using 'big' format and returned in 'big' format:", end=" ")
    print(s)
    print("2998302 stored as a binary using 'little' format and returned in 'big' format:", end=" ")
    print(r)