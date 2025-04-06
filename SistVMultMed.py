from datetime import datetime

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
    
    def verificarExiste(self,historia):
        return historia in self.__caninos or historia in self.__felinos
        
    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos)
    
    def ingresarMascota(self,mascota):
        if mascota.verTipo().lower() == "canino":
            self.__caninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo().lower() == "felino":
            self.__felinos[mascota.verHistoria()] = mascota

    def obtenerMascota(self, historia):
        return self.__caninos.get(historia) or self.__felinos.get(historia)
   

    def verFechaIngreso(self,historia):
        mascota=self.obtenerMascota(historia)
        return mascota.verFecha() if mascota else None
    
    def verMedicamento(self,historia):
        mascota= self.obtenerMascota(historia)
        return mascota.verLista_Medicamentos() if mascota else None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False 
    
    def eliminarMedicamento(self, historia, nombre_med):
        mascota = self.obtenerMascota(historia)
        if mascota:
            lista = mascota.verLista_Medicamentos()
            nueva_lista = [med for med in lista if med.verNombre() != nombre_med]
            mascota.asignarLista_Medicamentos(nueva_lista)
            return True
        return False

def main():
    servicio = sistemaV()

    while True:
        try:
            menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota
                       \n6- Eliminar medicamento administrado a una mascota 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        except ValueError:
            print("Ingrese un número válido.")
            continue
        if menu==1: # Ingresar una mascota 
            if servicio.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            try:
                historia = int(input("Historia clínica: "))
            except ValueError:
                print("La historia clínica debe ser un número.")
                continue
            if not servicio.verificarExiste(historia):
                nombre = input("Nombre: \n")
                tipo = input("Tipo (canino o felino): \n").lower()
                if tipo not in ("canino", "felino"):
                    print("El tipo debe ser 'canino' o 'felino'.")
                    continue

                try:
                    peso= float(input("Peso: "))
                except ValueError:
                    print("Peso inválido.")
                    continue

                fecha = input("Fecha de ingreso (dd/mm/aaaa): \n")
                try:
                   datetime.strptime(fecha, "%d/%m/%Y")
                except ValueError:
                    print("Formato inválido. El formato correcto es dd/mm/aaaa")
                    continue

                try:
                    nm= int(input("Ingrese la cantidad de medicamentos: \n"))
                except ValueError:
                    print("cantidad inválida.")
                    continue

                nombres_meds = set()
                lista_med = []

                for i in range(nm):
                    nombre_med = input(f"Nombre del medicamento #{i+1}: \n")
                    if nombre_med in nombres_meds:
                        print("Este medicamento ya fue ingresado.")
                        continue
                    try:
                        dosis = int(input("Dosis: \n"))
                    except ValueError:
                        print("Dosis inválida.")
                        continue
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_med)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    nombres_meds.add(nombre_med)
                mascota = Mascota()
                mascota.asignarNombre(nombre)
                mascota.asignarHistoria(historia)
                mascota.asignarTipo(tipo)
                mascota.asignarPeso(peso)
                mascota.asignarFecha(fecha)
                mascota.asignarLista_Medicamentos(lista_med)
                servicio.ingresarMascota(mascota)
                print("Mascota registrada con éxito.")
            else:
                print("Ya existe una mascota con esa historia clínica.")

            
        elif menu==2: # Ver fecha de ingreso
            historia = int(input("Historia clínica: "))
            fecha = servicio.verFechaIngreso(historia)
            if fecha:
                print("Fecha de ingreso:", fecha)
            else:
                print("No existe mascota con esa historia.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
              print("Total de mascotas:", servicio.verNumeroMascotas())

        elif menu==4: # Ver medicamentos que se están administrando
            historia = int(input("Historia clínica: "))
            meds = servicio.verMedicamento(historia)
            if meds is not None:
                print("Medicamentos administrados:")
                for med in meds:
                    print(f"- {med.verNombre()} (Dosis: {med.verDosis()})")
            else:
                print("No existe mascota con esa historia.")

        
        elif menu == 5: # Eliminar mascota
            historia = int(input("Historia clínica: "))
            if servicio.eliminarMascota(historia):
                print("Mascota eliminada.")
            else:
                print("No se encontró la mascota.")
        
        elif menu==6:
            historia = int(input("Historia clínica: "))
            nombre_med = input("Nombre del medicamento a eliminar: ")
            if servicio.eliminarMedicamento(historia, nombre_med):
                print("Medicamento eliminado (si existía).")
            else:
                print("No se encontró la mascota o el medicamento.")

        elif menu==7:
            print("Hasta luego.")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()
