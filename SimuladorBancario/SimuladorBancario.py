_author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

'''#-------------------------------------------------------------------------------------------
# Importaciones
-----------------------------------------------------------------------------------------------#'''

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    # Aqui inicia la declaracion de la clase
    
    '''#---------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------------#'''
    __cedula = ""
    __nombre = ""
    __mesActual = 0
    

    '''#---------------------------------------------------------------------
    # Asociaciones
    -------------------------------------------------------------------------#'''

    __cuentaAhorros = CuentaAhorros()
    __cuentaCorriente = CuentaCorriente()
    __cdt = CDT()
    
    '''#--------------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------------------#'''
    
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "ninguno"
    __return__ = "Ninguno"
    __description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self,monto):
        self.__cuentaCorriente.ConsignarSaldo(monto)
        
        
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "ninguno"
    __return__ = "Saldo total de todas las cuentas"
    __description__ = "Metodo que permite calcular el saldo total actual en todos"
    def CalcularSaldoTotal(self):
        # Aqui va mi codigo 
        # Metodo 1
        total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()
        return total

        # Metodo 2
        return self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()

    __method__ = "PasarAhorroACorriente"
    __parameter__ = "ninguno"
    __return__ = "Ninguna"
    __description__ = "Metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui va mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.CuentaDeAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    
    
    __method__ = "PasarCorrienteAAhorros"
    __parameter__ = "ninguno"
    __return__ = "Ninguna"
    __description__ = "Metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros"  
    def PasarCorrienteAAhorros(self, monto):
        # Aqui va mi codigo
        saldoCorriente = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarSaldo(saldoCorriente)
        self.__cuentaAhorros.ConsignarSaldo(saldoCorriente)
        
        
    
    __method__ = "RetirarAhorro"
    __parameter__ = "monto"
    __return__ = "Ninguna"
    __description__ = "Metodo que permite retirar un monto de la cuenta de ahorros"  
    def RetirarAhorro(self, monto):
        # Aqui va mi codigo
    
        self.__cuentaAhorros.RetirarSaldo(monto)

        
        
    __method__ = "DarSaldoCuentaCorriente"
    __parameter__ = "ninguno"
    __return__ = "Saldo de la cuenta corriente"
    __description__ = "Metodo que permite mostrar el saldo de la cuenta corriente"  
    def DarSaldoCuentaCorriente(self):
        # Aqui va mi codigo
        return self.__cuentaCorriente.DarSaldo()
    
    
    __method__ = "RetirarMontoTotal"
    __parameter__ = "ninguno"
    __return__ = "Ninguna"
    __description__ = "Metodo que permite retirar el monto total de la cuenta"  
    def RetirarMontoTotal(self):
        # Aqui va mi codigo
        
        self.RetirarMontoTotal.RetirarSaldo(self.__cuentaAhorros)
        self.RetirarMontoTotal.RetirarSaldo(self.__cuentaCorriente)
        
    
        
        
        
        
        
    
    
        
        


        
    
        
    
    
        