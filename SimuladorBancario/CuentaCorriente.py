__author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

class CuentaCorriente:
    # Aqui inicia la delcaracion de la clase

    '''#------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------#'''

    __saldo = 0.0
    
    '''#--------------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------------------#'''


    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __return__ = "Saldo de la cuenta"
    __description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        # Aqui inicia mi codigo
        return self.__saldo
    
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "Monto"
    __return__ = "Saldo de la cuenta"
    __description__ = "Metodo que permite consignar saldo a la cuenta corriente"
    def ConsignarSaldo(self, monto):
        #Aqui va mi codigo
        self.__saldo = self.__saldo + monto
        
        
    __method__ = "RetirarSaldo"
    __parameter__ = "Monto"
    __return__ = "Nuevo saldo"
    __description__ = "Metodo que permite retirar monto de la cuenta corriente"

    def RetirarSaldo(self, monto):
        #Aqui va mi codigo
        self.__saldo = self.__saldo + monto

    __method__ = "consultar_saldo"
    __parameter__ = "ninguno"
    __return__ = "Saldo actual"
    __description__ = "Metodo que retorna el saldo actual de la cuenta corriente"

    def consultarSaldo(self):
        # Aqui va mi codigo

        return self.saldo

