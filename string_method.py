# Mengubah Format Teks
# .upper => mengubah menjadi huruf besar
text = "hello"
print(text.upper()) # HELLO

# .lower => mengubah menjadi huruf kecil
print(text.lower()) # hello

# .capitalize => mengubah huruf pertama menjadi huruf besar
text = "Hello World"
print(text.capitalize()) # Hello world

# .title => mengubah setiap kata pertama menjadi huruf besar
text = "Hello World"
print(text.title()) # Hello World

#  Menghapus spasi atau karakter tertentu
# .strip() → Menghapus spasi di awal dan akhir string.
text = "   Hello   "
print(text.strip()) # Hello

# .lstrip() → Menghapus spasi di sebelah kiri
print(text.lstrip())

# Mengecek String
# .startswith(substring) → Mengecek apakah string dimulai dengan substring tertentu 
# Case sensitive
text = "Hello"
print(text.startswith("He")) # True

# .endswith(substring) → Mengecek apakah string berakhir dengan substring tertentu.
# Case sensitive
print(text.endswith("lo")) # True

#.isalpha() → Mengecek apakah string hanya terdiri dari huruf.
print("Hello".isalpha()) # True
print("Hello123".isalpha()) # False

# .isdigit() → Mengecek apakah string hanya terdiri dari angka

number_only = "12345"
print(number_only.isdigit()) # True

# .isalnum() → Mengecek apakah string terdiri dari huruf dan atau angka
print("123a".isalnum())
print("123".isalnum())

#. find(substring) → Mencari posisi pertama substring dalam string (jika tidak ditemukan, return -1).
print("Hello Bro".find("r"))

# .replace(old, new) → Mengganti semua kemunculan substring dengan yang baru.
print("Hello bro".replace("bro", "world"))

# Memisahkan dan Menggabungkan String
# .split(separator) → Memisahkan string menjadi list berdasarkan separator
print("apple,banana,grape".split(","))

#.join(iterable) → Menggabungkan elemen dalam iterable menjadi string
text = ["Hello", "World"]
print(" ".join(text))