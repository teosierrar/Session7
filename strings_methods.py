from string import punctuation

print(dir("hi"))
methods=dir("hi")
useful_methods=[]
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)

print(help("hi".capitalize))
print("cat".capitalize())
s="i go to school everyday"
print(s.capitalize())

print(help("".casefold))
print("I LIKE CAKE!!@@gmail.com".casefold())
print("hello".center(30,"*"))
print("banananananananan".count("ana"))

print("Ana ana banana".find("ana",5))

print("abcdebg".index("b",2))
words=["i",  "like", "to", "sing"]
print(" ".join(words))

s="I like to go hiking!"
print(s.replace(" ","! !"))
s="I like to go hiking!"

print(s.replace("!","").split())
print(s.upper())
punctuation="!.?-/;',"
sentence="How, are, you? I don't like this"