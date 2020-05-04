class Automovil:

    def __init__(self, modelo, marca, color):
        self.model = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        
        

    def acelerar(self, velocidad = 0):
        
        if velocidad >= 50:
            self._motor.inyecta_gasolina(velocidad)
            self._estado = 'partimos con todo'    
            self._motor._estado_gasolina
        else:
            self._motor.inyecta_gasolina(velocidad)
            self._estado = 'partimos lento pero seguro'   
            self._motor._estado_gasolina

class Motor:

    def __init__ (self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self._estado_gasolina = 'El estanque está lleno'

    def inyecta_gasolina(self, cantidad):
        if cantidad >=50:
            self._estado_gasolina = 'Estamos quemando mucho'
        else:
            self._estado_gasolina = 'Estamos ahorrando gasolina'

if __name__ == '__main__':
  
    marca_vehiculo = input('Ingresa marca del vehiculo: ')
    color_vehiculo = input('Ingresa Color: ')
    velocidad_acelera = int(input('Ingresa velocidad de aceleracion: '))
    auto_1 = Automovil( '1123',marca_vehiculo, color_vehiculo)

    auto_1.acelerar(velocidad_acelera)
    print(f'Vehiculo {auto_1.color} marca {auto_1.marca} \n¡vamos! ¡{auto_1._estado}! \nEstado gasolina: {auto_1._motor._estado_gasolina}')