class Celular:
 def __init__(self, marca, modelo, camara):
     
        self.marca = marca 
        self.modelo  = modelo 
        self.camara  = camara
        
     
 def llamar(self):
        print("Estas haciendo una llamada")
        
        
 def cortar(self):
         print("Estas cortando una llamada")       


celular1 = Celular("Samsung","S23","48mp")
celular2 = Celular("Apple","Sq","98mp")
celular3 = Celular("Xiomi","hp","mp")
celular4 = Celular("sony","hp","mp")

celular1.llamar()
celular1.cortar()



print(celular1.marca)
print(celular2.marca)
print(celular3.marca)


        