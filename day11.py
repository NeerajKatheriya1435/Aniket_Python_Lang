
# num=6
# def greet():
#     # num=67
#     num=56
#     print(num)
#     print("Hello")

# greet()
# print(num)

# file=open("rohan.txt","r")
# content=file.read()
# print(content)
# file.close()

# f = open("data.txt", "rb")
# # f.write(" kaise ho rohan")
# print(f.read())
# f.close()

# with open("data.txt","rb") as f:
#     print(f.read())



# print("Closed autometic")

# file=open("rohan.txt","r")
# content=file.readline()
# print(file.readline())
# print(file.readline())

# file=open("rohan.txt","r")
# count=0
# while True:
#     content=file.readline()
#     count+=1
#     if count<=1:
#         continue
#     if not content:
#         break
#     if(count==2):
#         print(content)

# print(file.readlines())

# f = open('myfile.txt', 'w')
# f.write("Hello i amgood \nhello")
# l1=["Hello i am good\n","dusri value\n","tessra content\n"]
# f.writelines(l1)
# f.close()

# f = open('data.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']

# for item in lines:
#     f.write(item + '\n')
# f.close()

# f = open('data.txt', 'r')
# # f.seek(6)
# f.readline()
# print(f.tell())

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)
