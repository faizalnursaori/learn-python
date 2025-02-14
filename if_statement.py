x = 10

if x >5:
    print("X lebih besar dari 5")

y = 3
if y > 5:
    print("Y lebih besar dari 5")
else:
    print("Y kurang dari atau sama dengan 5")

grade = 75
if grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
elif grade >= 60:
    print("Grade D")
else:
    print("Anda tidak lulus")

# Operator and, or, not
# And => Operator and mengembalikan True hanya jika kedua kondisi bernilai True
umur = 20
punya_ktp = True

if umur >= 18 and punya_ktp:
    print("Anda boleh membuat SIM")
else:
    print("Anda tidak bisa membuat SIM")

#Or => Operator or mengembalikan True jika salah satu atau kedua kondisi bernilai True
cuaca_cerah = False
ada_payung = True

if cuaca_cerah or ada_payung:
    print("Anda bisa pergi ke luar")
else:
    print("Lebih baik tetap di rumah")

#not =>  membalik nilai boolean
hujan = True

if not hujan:
    print("Kita bisa pergi piknik")
else:
    print("Tunda piknik")

# Kombinasi and, or, dan not
umur = 19
punya_ktp = False
punya_sim = True

if(umur >= 18 and punya_ktp) or punya_sim:
    print("Anda boleh mengendarai motor")
else:
    print("Anda tidak boleh mengendarai motor")