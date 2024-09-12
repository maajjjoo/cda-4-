_author__ = "Maria Jose De La Cruz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "maria.delacruzma@campusucc.edu.co"

class CDT:
    # Aqui inicia la delcaracion de la clase

    '''#------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------#'''

    montoInicial = 0.0
    tasaInteres = 0.0
    mesesTranscurridos = 0


    
    '''#------------------------------------------------------------------
    #Metodos
    ----------------------------------------------------------------------#'''
    
    __method__ = "CrearCDT"
    __parameter__ = "monto, interes, meses_transcurridos"
    __return__ = "Ninguno"
    __description__ = "metodo que crea el CDT con los valores dados"
    def CrearCDT (self, monto, interes, meses):

        self.montoInicial = monto
        self.tasaInteres = interes
        self.mesesTranscurridos = meses


    _method__ = "DarSaldo"
    __parameter__ = "ninguno"
    __return__ = "Saldo acumulado"
    __description__ = "metodo que retorna el saldo acumulado"
    def DarSaldo(self):
        # Aqui va mi codigo 
        
        return self.saldo; self.saldo = self.montoInicial + (self.tasaInteres * self.mesesTranscurridos)
    

    __method__ = "DarInteresMensual"
    __parameter__ = "ninguno"
    __return__ = "Interes Mensual"
    __description__ = "metodo que retorna el interes mensual"
    def DarInteresMensual(self):
        # Aqui va mi codigo 
        
        return self.interesMensual 
    

    __method__ = "CerrarCDT"
    __parameter__ = "ninguno"
    __return__ = "Valor total del CDT al momento del cierre"
    __description__ = "metodo que cierra el CDT y retorna el valor total acumulado"
    def CerrarCDT (self):
        # Aqui va mi codigo 

        self.cerrarCDT = self.saldoFinal = self.saldo
        self.montoInicial = 0.0
    
        



