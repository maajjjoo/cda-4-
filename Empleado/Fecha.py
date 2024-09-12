__author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

class Fecha :
    # Aqui inicia la declaracion de la clase

    '''#---------------------------------------------------------------
    Atribuos
    -------------------------------------------------------------------#'''

    dia = 0
    mes = 0
    anio = 0


    '''#---------------------------------------------------------------
    Metodos
    -------------------------------------------------------------------#'''

    __method__ = "DarDia"
    __parameter__ = "ninguno"
    __return__ = "Mes"
    __description__ = "Metodo que regresa el dia"
    
    def Dardia(self):
    # Aqui va mi codigo
        return self.dia


    __method__ = "DarMes"
    __parameter__ = "ninguno"
    __return__ = "Mes"
    __description__ = "Metodo que regresa el mes"


    def DarMes(self):
    # Aqui va mi codigo
        return self.mes

    __method__ = "DarAnio"
    __parameter__ = "ninguno"
    __return__ = "Anio"
    __description__ = "Metodo que regresa el año" 

    def DarAnio(self):
    # Aqui va mi codigo 
        return self.anio

    __method__ = "DarFecha"
    __parameter__ = "ninguno"
    __return__ = "Fecha"
    __description__ = "Metodo que regresa la fecha digitada por el usuario" 


    def Fecha(self): 'self.dia+'/'+self.mes+'/'+self.anio+'

