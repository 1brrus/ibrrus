import struct

def to_bits(f):
    return struct.unpack('>I', struct.pack('>f', f))[0]

def compare(a, b):
    ba, bb = to_bits(a), to_bits(b)
    print(f"A = {a}: {ba:032b} (0x{ba:08X})")
    print(f"B = {b}: {bb:032b} (0x{bb:08X})")
    print(f"XOR:  {ba ^ bb:032b}")
    print(f"Результат: {'РАВНЫ' if ba == bb else 'НЕ равны'}")

a = float(input("A: "))
b = float(input("B: "))
compare(a, b)