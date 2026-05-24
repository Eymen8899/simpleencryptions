import __init__ as simple # importing

# xor + dynamic caesar
inputt = "03091284523845189349818394819* mjdsnh fhduası " # Change if you want
y = simple.xorandcaesar(inputt,5)

# text
print(f"Encrypted text: {y}")

# lets decryript
text = simple.xorandcaesar_decode(y,5)

# printing again
print(f"Decrypted text: {text}")

binary = simple.strtobinary(text)
print(f"Binary text: {binary}, {simple.strtobinary(y)}")
# now lets check
assert text == inputt, "cant decode"