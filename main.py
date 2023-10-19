import unittest

from datetime import datetime

class Client:
    def __init__(self, retiros):
        self.debito = []
        self.caja_ahorro_pesos = []
        self.caja_ahorro_dolares = []
        self.cuenta_corriente = []
        self.chequera = None
        self.retiros = retiros

    def alta_tarjeta_debito(self):
        pass

    def alta_caja_de_ahorro(self):
        pass

    def alta_cuenta_corriente(self):
        pass

    def alta_chequera(self):
        pass

class TarjetaDebito:
    def __init__(self):
        pass

class CajaAhorro:
    def __init__(self, moneda):
        self.moneda = moneda

    def determinar_moneda(self):
        respuesta = input("Indica la moneda de tu nueva caja de ahorro (pesos o dólares): ").lower()
        while respuesta != "pesos" and respuesta != "dolares":
            print("Opción no válida. Por favor, elige PESOS o DOLARES.")
            respuesta = input("Indica la moneda de tu nueva caja de ahorro (pesos o dólares): ").lower()
        self.moneda = respuesta

class CuentaCorriente:
    def __init__(self, moneda):
        self.moneda = moneda

    def determinar_moneda(self):
        respuesta = input("Indica la moneda de tu nueva cuenta corriente (pesos o dólares): ").lower()
        while respuesta != "pesos" and respuesta != "dolares":
            print("Opción no válida. Por favor, elige PESOS o DOLARES.")
            respuesta = input("Indica la moneda de tu nueva cuenta corriente (pesos o dólares): ").lower()
        self.moneda = respuesta

class Chequera:
    def __init__(self):
        pass

class Classic(Client):
    def __init__(self, retiros, comision):
        super().__init__(retiros)
        self.comision = comision
        self.transferencias_salientes_comision = 1.0
        self.transferencias_entrantes_comision = 0.5
        self.retiro_maximo_diario = 10000
        self.retiros_realizados = 0

    def alta_tarjeta_debito(self):
        if len(self.debito) < 1:
            nueva_tarjeta = TarjetaDebito()
            self.debito.append(nueva_tarjeta)
            print("Se ha emitido una tarjeta de débito para el cliente Classic.")
        else:
            print("No puedes emitir más tarjetas de débito.")

    def alta_caja_de_ahorro(self):
        nueva_caja = CajaAhorro("")
        nueva_caja.determinar_moneda()
        if nueva_caja.moneda == "pesos" and len(self.caja_ahorro_pesos) < 1:
            self.caja_ahorro_pesos.append(nueva_caja)
            print("Se ha dado de alta tu nueva caja de ahorro en pesos.")
        elif nueva_caja.moneda == "dolares" and len(self.caja_ahorro_dolares) < 1:
            self.caja_ahorro_dolares.append(nueva_caja)
            print("Se ha dado de alta tu nueva caja de ahorro en dólares.")
        else:
            print("No puedes tener más de una caja de ahorro en la misma moneda.")

    def alta_cuenta_corriente(self):
        print("Los clientes Classic no pueden tener cuentas corrientes.")

    def alta_chequera(self):
        print("Los clientes Classic no pueden tener chequeras.")

    def realizar_retiro(self):
        monto=int(input('Ingresar monto para retirar:'))
        if self.retiros_realizados < self.retiros:
            if monto <= self.retiro_maximo_diario:
                self.retiros_realizados += 1
                print(f"Retiro de ${monto} realizado.")
            else:
                print(f"El monto de retiro excede el límite diario.")
        else:
            print("Has alcanzado el límite de retiros permitidos.")

    def transferencia_saliente(self):
        monto=int(input('Ingresar monto para realizar la transferencia:'))
        comision = monto * (self.transferencias_salientes_comision / 100)
        monto_total = monto + comision
        print(f"Se ha realizado una transferencia saliente de ${monto} con una comisión de ${comision}.")

    def transferencia_entrante(self, monto):
        comision = monto * (self.transferencias_entrantes_comision / 100)
        monto_total = monto - comision
        print(f"Se ha recibido una transferencia entrante de ${monto} con una comisión de ${comision}.")

class Gold(Client):
    def __init__(self, retiros, comision):
        super().__init__(retiros)
        self.comision = comision
        self.transferencias_salientes_comision = 0.5
        self.transferencias_entrantes_comision = 0.1
        self.retiro_maximo_diario = 20000
        self.cajas_ahorro_max = 2
        self.cuenta_corriente_max = 1
        self.tarjetas_visa = 0
        self.tarjetas_mastercard = 0
        self.inversion = None
        self.chequera = False

    def alta_tarjeta_debito(self):
        if len(self.debito) < 1:
            nueva_tarjeta = TarjetaDebito()
            self.debito.append(nueva_tarjeta)
            print("Se ha emitido una tarjeta de débito para el cliente Gold.")
        else:
            print("No puedes emitir más tarjetas de débito.")

    def alta_caja_de_ahorro(self):
        if len(self.caja_ahorro_pesos) + len(self.caja_ahorro_dolares) < self.cajas_ahorro_max:
            nueva_caja = CajaAhorro("")
            nueva_caja.determinar_moneda()
            if nueva_caja.moneda == "pesos":
                self.caja_ahorro_pesos.append(nueva_caja)
                print("Se ha dado de alta tu nueva caja de ahorro en pesos.")
            elif nueva_caja.moneda == "dolares":
                if len(self.caja_ahorro_dolares) < 1:
                    self.caja_ahorro_dolares.append(nueva_caja)
                    print("Se ha dado de alta tu nueva caja de ahorro en dólares.")
                else:
                    print("No puedes tener más de una caja de ahorro en dólares.")
        else:
            print("Has alcanzado el límite de cajas de ahorro permitidas.")

    def alta_cuenta_corriente(self):
        if len(self.cuenta_corriente) < self.cuenta_corriente_max:
            nueva_cuenta = CuentaCorriente("")
            nueva_cuenta.determinar_moneda()
            self.cuenta_corriente.append(nueva_cuenta)
            print("Se ha dado de alta tu nueva cuenta corriente.")
        else:
            print("Has alcanzado el límite de cuentas corrientes permitidas.")

    def alta_chequera(self):
        if not self.chequera:
            self.chequera = Chequera()
            print("Se ha dado de alta tu nueva chequera.")
        else:
            print("No puedes emitir más chequeras.")

    def realizar_retiro(self):
        monto=int(input('Ingresar monto para retirar:'))
        if monto <= self.retiro_maximo_diario:
            print(f"Retiro de ${monto} realizado.")
        else:
            print(f"El monto de retiro excede el límite diario de $20,000.")

    def transferencia_saliente(self):
        monto=int(input('Ingresar monto para realizar la transferencia:'))
        comision = monto * (self.transferencias_salientes_comision / 100)
        monto_total = monto + comision
        print(f"Se ha realizado una transferencia saliente de ${monto} con una comisión de ${comision}.")

    def transferencia_entrante(self, monto):
        comision = monto * (self.transferencias_entrantes_comision / 100)
        monto_total = monto - comision
        print(f"Se ha recibido una transferencia entrante de ${monto} con una comisión de ${comision}.")

class Black(Client):
    def __init__(self, retiros):
        super().__init__(retiros)
        self.transferencias_salientes_comision = 0.0
        self.transferencias_entrantes_comision = 0.0
        self.retiro_maximo_diario = 100000
        self.tarjetas_visa = 0
        self.tarjetas_mastercard = 0
        self.tarjetas_amex = 0
        self.cajas_ahorro_max = 5
        self.cuenta_corriente_max = 3
        self.inversion = None
        self.chequeras_max = 2
        self.chequeras_emitidas = 0

    def alta_tarjeta_debito(self):
        if len(self.debito) < 5:
            nueva_tarjeta = TarjetaDebito()
            self.debito.append(nueva_tarjeta)
            print("Se ha emitido una tarjeta de débito para el cliente Black.")
        else:
            print("No puedes emitir más tarjetas de débito.")

    def alta_caja_de_ahorro(self):
        if len(self.caja_ahorro_pesos) + len(self.caja_ahorro_dolares) < self.cajas_ahorro_max:
            nueva_caja = CajaAhorro("")
            nueva_caja.determinar_moneda()
            if nueva_caja.moneda == "pesos":
                self.caja_ahorro_pesos.append(nueva_caja)
                print("Se ha dado de alta tu nueva caja de ahorro en pesos.")
            elif nueva_caja.moneda == "dolares":
                if len(self.caja_ahorro_dolares) < 1:
                    self.caja_ahorro_dolares.append(nueva_caja)
                    print("Se ha dado de alta tu nueva caja de ahorro en dólares.")
                else:
                    print("No puedes tener más de una caja de ahorro en dólares.")
        else:
            print("Has alcanzado el límite de cajas de ahorro permitidas.")

    def alta_cuenta_corriente(self):
        if len(self.cuenta_corriente) < self.cuenta_corriente_max:
            nueva_cuenta = CuentaCorriente("")
            nueva_cuenta.determinar_moneda()
            self.cuenta_corriente.append(nueva_cuenta)
            print("Se ha dado de alta tu nueva cuenta corriente.")
        else:
            print("Has alcanzado el límite de cuentas corrientes permitidas.")

    def alta_chequera(self):
        if self.chequeras_emitidas < self.chequeras_max:
            self.chequera = Chequera()
            self.chequeras_emitidas += 1
            print("Se ha dado de alta tu nueva chequera.")
        else:
            print("No puedes emitir más chequeras.")

    def realizar_retiro(self):
        monto=int(input('Ingresar monto para retirar:'))
        if monto <= self.retiro_maximo_diario:
            print(f"Retiro de ${monto} realizado.")
        else:
            print(f"El monto de retiro excede el límite diario de $100,000.")

    def transferencia_saliente(self):
        monto=int(input('Ingresar monto para realizar la transferencia:'))
        print(f"Se ha realizado una transferencia saliente de ${monto}. No se aplica comisión.")

    def transferencia_entrante(self, monto):
        print(f"Se ha recibido una transferencia entrante de ${monto}. No se aplica comisión.")

class Calculator:
    def calcular_monto_total(self, precio_dolar, cantidad_deseada):
        monto_total = precio_dolar * cantidad_deseada
        impuesto = monto_total * (75/100)
        monto_total = monto_total + impuesto
        return monto_total

    def descontar_comision(self, monto, porcentaje_comision):
        comision = (monto * porcentaje_comision) / 100
        monto_total = monto - comision
        return monto_total
    
    def calcular_monto_plazo_fijo(self, monto, interes):
        monto_final = monto + (monto * (interes / 100))
        return monto_final

class CalculatorTestCase(unittest.TestCase):
    def test_calcular_monto_total(self):
        calculator = Calculator()

        resultado = calculator.calcular_monto_total(100, 5)
        self.assertEqual(resultado, 875.0)

        resultado = calculator.calcular_monto_total(350, 20)
        self.assertEqual(resultado, 12.250)

    def test_descontar_comision(self):
        calculator = Calculator()

        resultado = calculator.descontar_comision(100, 5)
        self.assertEqual(resultado, 95)

        resultado = calculator.descontar_comision(350, 20)
        self.assertEqual(resultado, 280)
        
    def test_calcular_monto_plazo_fijo(self):
        calculator = Calculator()

        resultado = calculator.calcular_monto_plazo_fijo(100, 5)
        self.assertEqual(resultado, 105)

        resultado = calculator.calcular_monto_plazo_fijo(350, 20)
        self.assertEqual(resultado, 420)


# Crear una instancia de Classic
cliente_classic = Classic(5, 10)

# Llamar a las funciones de Classic

cliente_classic.alta_caja_de_ahorro()
cliente_classic.alta_tarjeta_debito()
cliente_classic.alta_cuenta_corriente()
cliente_classic.transferencia_entrante(100)
cliente_classic.transferencia_saliente()
cliente_classic.realizar_retiro()
cliente_classic.alta_chequera()
        

# Crear una instancia de Gold
cliente_gold = Gold(5, 10)

# Llamar a las funciones de Gold
cliente_gold.alta_caja_de_ahorro()
cliente_gold.alta_cuenta_corriente()
cliente_gold.realizar_retiro()
cliente_gold.alta_chequera()
cliente_gold.alta_tarjeta_debito()
cliente_gold.transferencia_saliente()
cliente_gold.transferencia_entrante(100)

# Crear una instancia de Black
cliente_black = Black(5)

# Llamar a las funciones de Black
cliente_black.alta_caja_de_ahorro()
cliente_black.alta_chequera()
cliente_black.alta_tarjeta_debito()
cliente_black.transferencia_entrante(100)
cliente_black.transferencia_saliente()
cliente_black.realizar_retiro()
cliente_black.alta_chequera()

