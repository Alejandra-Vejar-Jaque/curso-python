class Celular:
 def __init__(self, marca, modelo, camara):
     
        self.marca = marca 
        self.modelo  = modelo 
        self.camara  = camara
        

celular1 = Celular("Samsung","S23","48mp")
celular2 = Celular("Apple","Sq","98mp")

print(celular1.marca)
print(celular2.marca)

