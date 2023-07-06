from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
"""Crear CRUD de la clase Persona"""

data_personas:list=[{"dni":"76371922",
                     "nombres":"Elvis Jesus" ,
                     "apellidos":"Apaza Yucra",
                     "direccion":"Jr. las flores 255",
                     "telefono":"916859627"},
                     {"dni":"74402669",
                     "nombres":"Yuhusara yoselin",
                      "apellidos":"Coila Apaza",
                     "direccion":"av. julio c. tello",
                     "telefono":"983199148"},
                    {"dni":"74059496",
                    "nombres":"Rosa Maria de los angeles",
                    "apellidos":"Torres Apaza",
                    "direccion":"Jr. Jose Galvez",
                    "telefono":"998989901"},]

lista_de_personas:Persona=[]
def cargar_data_personas():
    for data in data_personas:
        lista_de_personas.append(Persona(data["dni"],
                                         data["nombres"],
                                         data["apellidos"],
                                         data["direccion"],
                                         data["telefono"]))
def registrar_persona():
    print("------------ REGISTRANDO CLIENTE ------------")
    v_dni:str= input("Ingrese el DNI de la persona: ")
    v_nombres:str= input("Ingrese nombres de la persona: ")
    v_apellidos:str= input("Ingrese apellidos de la persona: ")
    v_direccion:str= input("Ingrese direccion de la persona: ")
    v_telefono:str= input("Ingrese telefono de la persona: ")
    persona:Persona= Persona(v_dni,v_nombres,v_apellidos,v_direccion,v_telefono)
    lista_de_personas.append(persona)
    listar_personas()

def listar_personas():
    print("--------------------------------------------------------------------------")
    print("--------------------------- LISTA DE CLIENTES ----------------------------")
    for elemento in lista_de_personas:
        print("--------------------------------------------------------------------------")
        print("|N° DOC. |NOMBRES     |APELLIDOS        |DIRECCION         |TELEFONO       |")
        print(elemento.convertir_a_string())

def bucar_persona():
    v_dni:str = input("Ingrese el DNI de la persona: ")
    print("--------------------------- DATOS DEL CLIENTE ----------------------------")
    print("--------------------------------------------------------------------------")
    print("|N° DOC. |NOMBRES     |APELLIDOS        |DIRECCION         |TELEFONO       |")
    for elemento in lista_de_personas:
        if elemento.dni == v_dni:
            print(elemento.convertir_a_string())
            return elemento
            

def editar_persona():
    listar_personas()  
    v_dni:str =input("Ingrese el DNI de la persona: ")
    for persona in lista_de_personas:
        if persona.dni == v_dni:
            persona.nombres=input("Ingrese nombres de la persona: ")
            persona.apellidos=input("Ingrese apellidos de la persona: ")
            persona.direccion=input("Ingrese direccion de la persona: ")
            persona.telefono=input("Ingrese telefono de la persona: ")
    listar_personas()
    return lista_de_personas

def eliminar_persona():
    dni:str =input("Ingrese el DNI de la persona: ")
    for index, persona in enumerate(lista_de_personas):
        if persona.dni == dni:
            lista_de_personas.pop(index)
    return lista_de_personas


"""Crear CRUD de la clase Producto"""

data_productos:list=[{"codigo":"001",
                     "nombre":"helado de fresa",
                     "precio":2.50},
                     {"codigo":"002",
                     "nombre":"helado de chocolate",
                     "precio":3.00},
                     {"codigo":"003",
                     "nombre":"helado en barquillo",
                     "precio":1.50}
                    ]

lista_de_productos:Producto=[]
def cargar_data_productos():
    for data in data_productos:
        lista_de_productos.append(Producto(data["codigo"],
                                         data["nombre"],
                                         data["precio"]))
def registrar_producto():
    print("------------------------------------------")
    print("------- INSERTANDO NUEVO PRODUCTO --------")
    codigo:str= input("Ingrese el codigo del producto: ")
    nombre:str= input("Ingrese nombre del producto: ")
    precio:float= float(input("Ingrese precio del producto: "))

    producto:Producto= Producto(codigo,nombre,precio)
    lista_de_productos.append(producto)
    listar_productos()

def listar_productos():
    print("-----------------------------------------------------------------")
    print("----------------------- LISTA DE PRODUCTOS ----------------------")
    print("-----------------------------------------------------------------")
    print("|N° SERIE|PRODUCTO   |PRECIO |")
    for elemento in lista_de_productos:
        print(elemento.convertir_a_string())

def bucar_producto():
    listar_productos()
    codigo:str = input("Ingrese el codigo del producto: ")
    print("-------- DATOS DEL PRODUCTO --------")
    print("|N° SERIE |PRODUCTO |PRECIO |")
    for elemento in lista_de_productos:
        if elemento.codigo == codigo:
            print(elemento.convertir_a_string())
            return elemento
            

def editar_producto():
    listar_productos()  
    codigo:str =input("Ingrese el codigo del producto: ")
    for producto in lista_de_productos:
        if producto.codigo == codigo:
            producto.nombre=input("Ingrese nombre del producto: ")
            producto.precio=float(input("Ingrese precio del producto: "))
            break
    listar_productos()
    return lista_de_productos

def eliminar_producto():
    codigo:str =input("Ingrese codigo del producto: ")
    for index, producto in enumerate(lista_de_productos):
        if producto.codigo == codigo:
            lista_de_productos.pop(index)
            break
    return lista_de_productos

facturas:Factura=[]
factura_detalles:FacturaDetalle=[]

def agregar_productos_a_la_factura():
    producto:Producto=bucar_producto()
    cantidad:float=float(input(" Ingrese la cantidad de productos a vender: "))
    factura_detalles.append(FacturaDetalle(len(factura_detalles)+1,producto.codigo,producto.nombre,cantidad,producto.precio))


def generar_pdf_factura(factura):

    total_factura = 0
    for detalle in factura.detalle:
        total_factura += detalle.total

    archivo_pdf = f"factura_{factura.numero}.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    c.drawImage("helado.jpg", 72, 450, width=330, height=330)
    c.drawString(72, 700, "                                HELADERIA REY                   ")
    c.drawString(72, 680, "                         CAR. LAMPA km. 4.0 JUL.  ")
    c.drawString(72, 660, "                       PUNO - SAN ROMAN - JULIACA")
    c.drawString(72, 620, "-=-=-=-=-=-=-=-=-= BOLETA DE VENTA -=-=-=-=-=-=-=-=-=")
    c.drawString(72, 610, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, 600, f"CLIENTE       :  {factura.cliente.apellidos}, {factura.cliente.nombres}")
    c.drawString(72, 580, f"DNI            :  {factura.cliente.dni}")
    c.drawString(72, 560, f"DIRECCION   :  {factura.cliente.direccion}")
    c.drawString(72, 550, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, 540, "Detalles de venta:")
    c.drawString(72, 530, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, 520, "|CANT |  DESCRIPCION       |IMPORTE |")
    c.drawString(72, 510, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    y_position = 500
    for detalle in factura.detalle:
        c.drawString(72, y_position, f"| {detalle.cantidad}    | {detalle.nombre}    |S/.{detalle.total:.2f}  |")
        y_position -= 20
    c.drawString(72, y_position, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, y_position-10, "                               TIPO DE PAGO")
    c.drawString(72, y_position-30, "                                 EFECTIVO")
    c.drawString(72, y_position-50, f"Total a pagar: S/.{total_factura:.2f}")
    c.drawString(72, y_position-60, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, y_position-80, "cajero: APAZA YUCRA, Elvis Jesus")
    c.drawString(72, y_position-90, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    c.drawString(72, y_position-100, "v. Resumen: X")
    c.drawString(72, y_position-120, "Autorizado mediante resolucion Nro.")
    c.drawString(72, y_position-140, "0180050002255 / SUNAT")
    c.drawString(72, y_position-160, "-=-=-=REPRESENTACION DE LA BOLETA DE-=-=-=")
    c.drawString(72, y_position-180, "=-=-=-=-=-=-=-VENTA ELECTRONICA-=-=-=-=--=-=-")
    c.drawString(72, y_position-250, "AVISO: toda informacion no sera revelada a ")
    c.drawString(72, y_position-270, "terceros por parte de la empresa ")
    c.drawString(72, y_position-290, "!GRACIAS POR SU COMPRA!")
    c.save()


    print(f"Factura generada exitosamente: {archivo_pdf}")

def registrar_factura():
    cliente = bucar_persona()
    continuar_agregando_producto = True
    while continuar_agregando_producto:
        print("1: para agregar producto 2: para guardar factura")
        opcion = input("ingrese la opcion deseada: ")
        if opcion == "1":
            agregar_productos_a_la_factura()
        elif opcion == "2":
            continuar_agregando_producto = False
        else:
            print("Opción inválida. Intente nuevamente.")

    total_factura = 0
    for factura_detalle in factura_detalles:
        total_factura += factura_detalle.total

    factura = Factura(len(facturas) + 1, cliente, total_factura, factura_detalles)
    facturas.append(factura)


    generar_pdf_factura(factura)

    return facturas

def listar_facturas():
    for factura in facturas:
        print("-----------------------------------------------------------------")
        print("------------------------ BOLETA DE VENTA ------------------------")
        print("-----------------------------------------------------------------")
        print("|N° DE VENTA|NOMBRE DEL COMPRADOR|PRECIO TOTAL DE CADA PRODUCTO|")
        print(factura.convertir_a_string())
        
def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in facturas:
        if factura.numero==numero:
            print("----------------- FACTURA -----------------")
            print("----------------- CLIENTE -----------------")
            print(factura.convertir_a_string())
            print("--------------------------------------------------------")
            for detalle in factura.detalle:
                print(detalle.convertir_a_string())
            return factura

def eliminar_venta():
    listar_facturas()
    numero:int=int(input("ingrese el numero de la venta para eliminar: "))   
    for indice, factura in enumerate(facturas):
        if factura.numero==numero:
            facturas.pop(indice)
    print("-----------------------------------------------------------------")
    listar_facturas()
    return facturas








def menu_principal():
    print("============= MENU===========")
    print("--------- CRUD CLIENTE ---------")
    print("1: Para registrar persona")
    print("2: Para listar persona")
    print("3: Para buscar persona")
    print("4: Para editar persona")
    print("5: Para eliminar persona")
    print("--------- CRUD PRODUCTO ---------")
    print("6: Para registrar producto")
    print("7: Para listar producto")
    print("8: Para buscar producto")
    print("9: Para editar producto")
    print("10: Para eliminar producto")
    print("--------- CRUD FACTURA ----------")
    print("11: Para registrar factura")
    print("12: Para listar factura")
    print("13: Para buscar factura")
    print("14: para eliminar factura")
    print("salir: para salir del programa")
    return True
def menu():
    continuar_programa:bool=True
    while continuar_programa:
        menu_principal()
        opcion:str=input("Ingrese la opcion: ")
        match opcion:
            case "1":
                registrar_persona()
            case "2":
                listar_personas()
            case "3":
                bucar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                registrar_producto()
            case "7":
                listar_productos()
            case "8":
                bucar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "11":
                registrar_factura()
            case "12":
                listar_facturas()
            case "13":
                buscar_factura()
            case "14":
                eliminar_venta()

            case "salir":
                print("---Saliendo del programa---")
                print("-----!muchas gracias!-----")
                continuar_programa= False

def main():
    cargar_data_personas()
    cargar_data_productos()
    menu()
    return True

if __name__=='__main__':
    main()