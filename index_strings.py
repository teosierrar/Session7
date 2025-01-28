s1="hello world!"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[4],s1[7])
print(s1[10],s1[-1])
print(s1[-2])

print(s1[14//2])
s1="hello"
s2="world"

print(s1+" "+s2+"!")

if "bob":
    print("bob is")
else:
    print("bob is not")

if "":
    print("empty string is True")
else:
    print("empty string is False")
s="abcdefghijklmnop"
print(len(s))

for character in s:
    print(character, end=" ")

i=0
while i<len(s):
    print(s[len(s)-i-1], end=" ")
    i+=1

# slice is a fancy index
s="0123456789"
print(s)
print(s[2:3])
print(s[4:6])
print(s[:3])
print(s[3:])
print(s[1:7:2])
print(s[::-1])
print(s[::-2])
