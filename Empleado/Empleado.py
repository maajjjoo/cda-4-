__author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

from Fecha import Fecha

class Empleado:
    # Aqui inicia la delcaracion de la clase

    '''#------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------#'''

    nombre = ""
    apellido = ""
    salario = 0

    '''#-----------------------------------------------------------------
    # 1 = Masculino, 2 = Femenino 
    ---------------------------------------------------------------------#'''

    sexo = 0  

    '''#------------------------------------------------------------------
    # Asociación
    ----------------------------------------------------------------------#'''

    fechaIngreso = Fecha()
    fechaNacimiento = Fecha() 
    
    '''#---------------------------------------------------------------
    #Metodos
    -------------------------------------------------------------------#'''
    # Este metodo retorna el nombre del empleado

    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre 
    
    __method__ = "CambiarSalario"
    __parameter__ = "nuevoSalario"
    __return__ = "Salario"
    __description__ = "metodo que actualiza el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo
        self.salario = nuevoSalario
    # Retorna el salario del empleado

    def DarSalario(self):
        # Aqui va mi codigo
        return self.DarSalario

    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()
    
    
    __method__ = "CalcularSalarioAnual"
    __parameter__ = "nuevoSalario"
    __return__ = "Salario anual"
    __description__ = "muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # Aqui va mi codigo
        #forma 1
        #total = self.salario*12
        #return total 
        
        return self.salario*1
    
    
    __method__ = "CalcularImpuestoSalarioAnual" 
    __parameter__ = "ninguno"
    __return__ = "Impuesto del salario anual"
    __description__ = "muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        #salarioAnual=self.CalcularSalarioAnual()
        #impuestoAnual=salarioAnual*0.19
        #return impuestoAnual
        return self.CalcularSalarioAnual()*0.19 
    
    
    __method__ = "CalcularImpuestoSalario" 
    __parameter__ = "ninguno"
    __return__ = "Impuesto del salario"
    __description__ = "muestra el impuesto del salario del empleado"
    def CalcularImpuestoSalarioMensual(self):
        # Aqui va mi codigo
        return self.DarSalario(self)*0.19
    
    
    
    
    
        