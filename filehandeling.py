# f = open("file.txt", "w")
# f.write("hello there")
# f.close
# # print (f)

# f= open ("file.txt","r")
# t= f.read()
# print(t)
# f.close

# Append
# f= open ("file.txt","a")
# t= f.write(" i am Sameer")
# f.close

# with open ("file.txt","a",) as f :
#     f.write("Akram")

# f= open ("file.txt","r")
# text = f.read()
# print(text)

with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)
