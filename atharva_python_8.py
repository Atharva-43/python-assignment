#Step1 write the file
file = open("myfile.txt","w")
file.write("Hello Students")
file.close()
#Step2 Append the file
file = open("myfile.txt","a")
file.write("\nWelcome to the Python Programming")
file.close()
#Step3 Read from file
file = open("myfile.txt","r")
data = file.read()
print(data)
file.close()