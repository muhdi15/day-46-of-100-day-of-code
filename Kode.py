# ini adalah program perbandingan dan penentuan pembuatan sim


user=int(input("Masukkan usia anda :"))

if(user < 17):
    print(f"Usia anda yang {user} belum mencukupi dalam membuat SIM")

elif(user >= 17 and user <= 80):
    print(f"Usia anda yang {user} telah mencukupi untuk membuat SIM")

else:
    print("ERROR")
