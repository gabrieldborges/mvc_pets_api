class AlgumaCoisa():
    def __exit__(self, exc_type , exc_val, exc_tb):
        print("Estou saindo")
    def __enter__(self):
        print("Estou entrando")


with AlgumaCoisa() as something:
    print ("Estou no meiooo")
