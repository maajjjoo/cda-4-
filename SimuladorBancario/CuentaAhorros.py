__author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

class CuentaAhorros:
    # Aqui inicia la declaracion de la clase

    '''#------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------#'''

    saldo = 0.0
    tasa_interes = 0.6

    '''#-------------------------------------------------------------------------
    # Metodos
    ---------------------------------------------------------------------------#'''

    
    
    __method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __return__ = "Saldo de la cuenta"
    __description__ = "metodo que retorna el saldo de la cuenta"

    def DarSaldo(self):
        # Aqui va mi codigo

        return self.saldo
    
    
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "nuevoValor"
    __return__ = "Valor"
    __description__ = "metodo que actualiza el valor de la cuenta de ahorros"

    def ConsignarValor(self, nuevoValor):
        # Aqui va mi codigo 

        self.saldo = self.saldo + nuevoValor
    

    __method__ = "RetirarValor"
    __parameter__ = "monto"
    __return__ = "Valor a retirar"
    __description__ = "metodo que retorna el valor a retirar"

    def RetirarValor(self, monto):
        # Aqui va mi codigo

        return self.saldo = self.saldo - monto


    __method__ = "DarInteresMensual"
    __parameter__ = "ninguno"
    __return__ = "Interes Mensual"
    __description__ = "metodo que retorna el interes mensual"

    def DarInteresMensual(self):
        # Aqui va mi codigo

        return self.interesmensual 

    

    __method__ = "ActualizarSaldoPorPasoMes"
    __parameter__ = "ninguno"
    __return__ = "Saldo Actualizado"
    __description__ = "metodo que actualiza el saldo por paso mes"

        
    def ActualizarSaldoPorPasoMes(self): 
        # Aqui va mi codigo
    
        self.interesmensual = self.tasa_interes * self.saldo


    def ActulizarSaldoPorPasoMes(self): 