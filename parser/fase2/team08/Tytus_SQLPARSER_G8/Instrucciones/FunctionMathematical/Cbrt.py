from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Primitivo import Primitivo
import math
import numpy as np

class Cbrt(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.DOUBLE_PRECISION),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función cbrt("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if resultado < 0:
            error = Excepcion('2201F',"Semántico","La función CBRT únicamente acepta valores númericos positivos",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        return np.cbrt(resultado)
    
    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        
        retorno = self.valor.traducir(tabla,arbol)
        #print(retorno.temporalAnterior)
        #print(type(self.valor))
        #print(self.valor.opIzq.traducir(tabla,arbol).temporalAnterior)
        return f"CBRT({self.valor.traducir(tabla,arbol).temporalAnterior})"

    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        
        if isinstance(self.valor, Primitivo):
            return f"CBRT({self.valor.traducir(tabla,arbol).temporalAnterior})"

        return f"CBRT({self.valor.concatenar(tabla,arbol)})"