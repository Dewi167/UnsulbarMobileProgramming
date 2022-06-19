class mahasiswa():
    jurusan = "teknik informatika"
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
 
dewi = mahasiswa("Dewi Nurliana")
 
print(mahasiswa.jurusan)
print(dewi.jurusan)
