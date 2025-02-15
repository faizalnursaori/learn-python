username = input("Enter a username: ")

if len(username) > 12 or len(username)<6 :
    print("Username harus memiliki 6 hingga 12 karakter")
elif not username.find(" ") == -1:
    print("Username tidak boleh mengandung spasi")
elif not username.isalpha():
    print("Username tidak boleh mengandung angka")    
else: 
    print(f"Selamat datang {username}")
