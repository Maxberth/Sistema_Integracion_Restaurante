from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import random
import time
import sqlite3

def guardar():
    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    datos_recibo=textoRecibo.get(1.0,END)
    url.write(datos_recibo)
    url.close()
    messagebox.showinfo("INFORMACIÓN",message="RECIBO ALMACENADO CON ÉXITO")
    
def enviar():
    pass
def borrar():
    textoRecibo.delete(1.0,END)
    txtLomito_saltado_pollo.set('0')
    txtLomito_saltado_carne.set('0')
    txtTallarines_verdes_pollo.set('0')
    txtChicharron_pollo.set('0')
    txtFilete_pollo.set('0')
    txtTallarin_saltado_pollo.set('0')
    txtTallarines_rojos.set('0')
    txtArroz_Chaufa_pollo.set('0')
    txtBistec_pobre.set('0')
    txtCeviche.set('0')

    txtInka_kola.set('0')
    txtCoca_cola.set('0')
    txtMaracuya.set('0')
    txtCebada.set('0')
    txtChicha.set('0')
    txtLimonada.set('0')
    txtPina.set('0')
    txtNaranja.set('0')
    txtInka_kola_personal.set('0')
    txtCoca_cola_personal.set('0')

    txtPollo_plancha.set('0')
    txtPollo_sancochado.set('0')
    txtPescado_plancha.set('0')
    txtPescado_apanado.set('0')
    txtEnsalada_rusa.set('0')
    txtEnsalada_brocoli.set('0')
    txtArroz_arabe.set('0')
    txtEnsalada_pepino.set('0')
    txtEnsalada_quinua.set('0')
    txtEnsalada_coliflor.set('0')
    
    textLomito_saltado_pollo.config(state=DISABLED)
    textLomito_saltado_carne.config(state=DISABLED)
    textTallarines_verdes_pollo.config(state=DISABLED)
    textChicharron_pollo.config(state=DISABLED)
    textFilete_pollo.config(state=DISABLED)
    textTallarin_saltado_pollo.config(state=DISABLED)
    textTallarines_rojos.config(state=DISABLED)
    textArroz_Chaufa_pollo.config(state=DISABLED)
    textBistec_pobre.config(state=DISABLED)
    textCeviche.config(state=DISABLED)

    textInka_kola.config(state=DISABLED)
    textCoca_cola.config(state=DISABLED)
    textMaracuya.config(state=DISABLED)
    textCebada.config(state=DISABLED)
    textChicha.config(state=DISABLED)
    textLimonada.config(state=DISABLED)
    textPina.config(state=DISABLED)
    textNaranja.config(state=DISABLED)
    textInka_kola_personal.config(state=DISABLED)
    textCoca_cola_personal.config(state=DISABLED)

    textPollo_plancha.config(state=DISABLED)
    textPollo_sancochado.config(state=DISABLED)
    textPescado_plancha.config(state=DISABLED)
    textPescado_apanado.config(state=DISABLED)
    textEnsalada_rusa.config(state=DISABLED)
    textEnsalada_brocoli.config(state=DISABLED)
    textArroz_arabe.config(state=DISABLED)
    textEnsalada_pepino.config(state=DISABLED)
    textEnsalada_quinua.config(state=DISABLED)
    textEnsalada_coliflor.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)


    global varcostocomida, varcostobebida,varcostodieta, varsubtotal, varigv, vartotal
    varcostobebida=0
    varcostocomida=0
    varcostodieta=0
    varsubtotal=0
    varigv=0
    vartotal=0

    casillaCostoComida.config(state=NORMAL)
    casillaCostoComida.delete(0,END)
    casillaCostoComida.insert(0,varcostocomida)
    casillaCostoComida.config(state=DISABLED)

    casillaCostoDieta.config(state=NORMAL)
    casillaCostoDieta.delete(0,END)
    casillaCostoDieta.insert(0,varcostodieta)
    casillaCostoDieta.config(state=DISABLED)
    
    casillasCostoBebidas.config(state=NORMAL)
    casillasCostoBebidas.delete(0,END)
    casillasCostoBebidas.insert(0,varcostodieta)
    casillasCostoBebidas.config(state=DISABLED)

    casillasubtotal.config(state=NORMAL)
    casillasubtotal.delete(0,END)
    casillasubtotal.insert(0,varsubtotal)
    casillasubtotal.config(state=DISABLED)

    casillasigv.config(state=NORMAL)
    casillasigv.delete(0,END)
    casillasigv.insert(0,varigv)
    casillasigv.config(state=DISABLED)

    casillapagoTotal.config(state=NORMAL)
    casillapagoTotal.delete(0,END)
    casillapagoTotal.insert(0,vartotal)
    casillapagoTotal.config(state=DISABLED)

def recibo():
    textoRecibo.delete(1.0,END)
    x=random.randint(1,10000)
    noRecibo = 'NO'+str(x)
    fecha=time.strftime('%d/%m/%y')
    textoRecibo.insert(END,'FACTURA->'+ noRecibo+'\t\t\t\t FECHA:'+fecha+'\n')
    textoRecibo.insert(END,'************************************************************************\n')
    textoRecibo.insert(END,'TOTALES \t\t\t CANTIDADES:\n')
    textoRecibo.insert(END,'************************************************************************\n')
    textoRecibo.insert(END,'TOTAL DE COMIDA  ------------------> S/. '+str(varcostocomida)+'.00\n')
    textoRecibo.insert(END,'TOTAL DE BEBIDAS ------------------> S/. '+str(varcostobebida)+'0\n')
    textoRecibo.insert(END,'TOTAL DE DIETA ------------------> S/. '+str(varcostodieta)+'.00\n')
    textoRecibo.insert(END,'SUBTOTAL ------------------------------> S/. '+str(varsubtotal)+'0\n')
    textoRecibo.insert(END,'IGV ---------------------->S/. '+str(varigv)+'0\n')
    textoRecibo.insert(END,'************************************************************************\n\n')
    textoRecibo.insert(END,'MONTO TOTAL A PAGAR -----------------> S/. \t\t\t'+str(vartotal)+'0\n')


#funciones para los totales
def grantotal():
    global varcostocomida, varcostobebida,varcostodieta, varsubtotal, varigv, vartotal
    #valores de comida
    t_Lomito_saltado_pollo=int(textLomito_saltado_pollo.get())
    t_Lomito_saltado_carne=int(textLomito_saltado_carne.get())
    t_Tallarines_verdes_pollo=int(textTallarines_verdes_pollo.get())
    t_Chicharron_pollo=int(textChicharron_pollo.get())
    t_Filete_pollo=int(textFilete_pollo.get())
    t_Tallarin_saltado_pollo=int(textTallarin_saltado_pollo.get())
    t_Tallarines_rojos=int(textTallarines_rojos.get())
    t_Arroz_Chaufa_pollo=int(textArroz_Chaufa_pollo.get())
    t_Bistec_pobre=int(textBistec_pobre.get())
    t_Ceviche=int(textCeviche.get())
    varcostocomida=(t_Lomito_saltado_pollo*10)+(t_Lomito_saltado_carne*11)+(t_Tallarines_verdes_pollo*10)+(t_Chicharron_pollo*11)+(t_Filete_pollo*12)+(t_Tallarin_saltado_pollo*11)+(t_Tallarines_rojos*10)+(t_Arroz_Chaufa_pollo*11)+(t_Bistec_pobre*13)+(t_Ceviche*13)
    casillaCostoComida.config(state=NORMAL)
    casillaCostoComida.delete(0,END)
    casillaCostoComida.insert(0,varcostocomida)
    casillaCostoComida.config(state=DISABLED)

#valores de bebidas
    t_Inka_kola=int(textInka_kola.get())
    t_Coca_cola=int(textCoca_cola.get())
    t_Maracuya=int(textMaracuya.get())
    t_Cebada=int(textCebada.get())
    t_Chicha=int(textChicha.get())
    t_Limonada=int(textLimonada.get())
    t_Pina=int(textPina.get())
    t_Naranja=int(textNaranja.get())
    t_Inka_kola_personal=int(textInka_kola_personal.get())
    t_Coca_cola_personal=int(textCoca_cola_personal.get())
    varcostobebida=(t_Inka_kola*7.50)+(t_Coca_cola*6)+(t_Maracuya*3)+(t_Cebada*3.50)+(t_Chicha*4)+(t_Limonada*3.50)+(t_Pina*3.50)+(t_Naranja*3.50)+(t_Inka_kola_personal*3.50)+(t_Coca_cola_personal*3.50)
    casillasCostoBebidas.config(state=NORMAL)
    casillasCostoBebidas.delete(0,END)
    casillasCostoBebidas.insert(0,varcostobebida)
    casillasCostoBebidas.config(state=DISABLED)

#valores de dieta
    t_Pollo_plancha=int(textPollo_plancha.get())
    t_Pollo_sancochado=int(textPollo_sancochado.get())
    t_Pescado_plancha=int(textPescado_plancha.get())
    t_Pescado_apanado=int(textPescado_apanado.get())
    t_Ensalada_rusa=int(textEnsalada_rusa.get())
    t_Ensalada_brocoli=int(textEnsalada_brocoli.get())
    t_Arroz_arabe=int(textArroz_arabe.get())
    t_Ensalada_pepino=int(textEnsalada_pepino.get())
    t_Ensalada_quinua=int(textEnsalada_quinua.get())
    t_Ensalada_coliflor=int(textEnsalada_coliflor.get())
    varcostodieta=(t_Pollo_plancha*13)+(t_Pollo_sancochado*10)+(t_Pescado_plancha*10)+(t_Pescado_apanado*11)+(t_Ensalada_rusa*9)+(t_Ensalada_brocoli*9)+(t_Arroz_arabe*11)+(t_Ensalada_pepino*10)+(t_Ensalada_quinua*11)+(t_Ensalada_coliflor*10)
    casillaCostoDieta.config(state=NORMAL)
    casillaCostoDieta.delete(0,END)
    casillaCostoDieta.insert(0,varcostodieta)
    casillaCostoDieta.config(state=DISABLED)

    varsubtotal=varcostocomida+ varcostobebida+varcostodieta
    casillasubtotal.config(state=NORMAL)
    casillasubtotal.delete(0,END)
    casillasubtotal.insert(0,varsubtotal)
    casillasubtotal.config(state=DISABLED)

    varigv=float(casillasubtotal.get()) * 0.1
    casillasigv.config(state=NORMAL)
    casillasigv.delete(0,END)
    casillasigv.insert(0,varigv)
    casillasigv.config(state=DISABLED)

    vartotal= varigv + varsubtotal
    casillapagoTotal.config(state=NORMAL)
    casillapagoTotal.delete(0,END)
    casillapagoTotal.insert(0,vartotal)
    casillapagoTotal.config(state=DISABLED)

# Funciones para activar y desactivar casillas para comida
def lomito_saltado_pollo():
    if var1.get() == 1:
        textLomito_saltado_pollo.config(state=NORMAL)
        textLomito_saltado_pollo.delete(0, END)
        textLomito_saltado_pollo.focus()
    else:
        textLomito_saltado_pollo.config(state=DISABLED)
        txtLomito_saltado_pollo.set('0')

def lomito_saltado_carne():
    if var2.get() == 1:
        textLomito_saltado_carne.config(state=NORMAL)
        textLomito_saltado_carne.delete(0, END)
        textLomito_saltado_carne.focus()
    else:
        textLomito_saltado_carne.config(state=DISABLED)
        txtLomito_saltado_carne.set('0')

def tallarines_verdes_pollo():
    if var3.get() == 1:
        textTallarines_verdes_pollo.config(state=NORMAL)
        textTallarines_verdes_pollo.delete(0, END)
        textTallarines_verdes_pollo.focus()
    else:
        textTallarines_verdes_pollo.config(state=DISABLED)
        txtTallarines_verdes_pollo.set('0')

def chicharron_pollo():
    if var4.get() == 1:
        textChicharron_pollo.config(state=NORMAL)
        textChicharron_pollo.delete(0, END)
        textChicharron_pollo.focus()
    else:
        textChicharron_pollo.config(state=DISABLED)
        txtChicharron_pollo.set('0')

def filete_pollo():
    if var5.get() == 1:
        textFilete_pollo.config(state=NORMAL)
        textFilete_pollo.delete(0, END)
        textFilete_pollo.focus()
    else:
        textFilete_pollo.config(state=DISABLED)
        txtFilete_pollo.set('0')

def tallarin_saltado_pollo():
    if var6.get() == 1:
        textTallarin_saltado_pollo.config(state=NORMAL)
        textTallarin_saltado_pollo.delete(0, END)
        textTallarin_saltado_pollo.focus()
    else:
        textTallarin_saltado_pollo.config(state=DISABLED)
        txtTallarin_saltado_pollo.set('0')

def tallarines_rojos():
    if var7.get() == 1:
        textTallarines_rojos.config(state=NORMAL)
        textTallarines_rojos.delete(0, END)
        textTallarines_rojos.focus()
    else:
        textTallarines_rojos.config(state=DISABLED)
        txtTallarines_rojos.set('0')

def arroz_chaufa_pollo():
    if var8.get() == 1:
        textArroz_Chaufa_pollo.config(state=NORMAL)
        textArroz_Chaufa_pollo.delete(0, END)
        textArroz_Chaufa_pollo.focus()
    else:
        textArroz_Chaufa_pollo.config(state=DISABLED)
        txtArroz_Chaufa_pollo.set('0')

def bistec_pobre():
    if var9.get() == 1:
        textBistec_pobre.config(state=NORMAL)
        textBistec_pobre.delete(0, END)
        textBistec_pobre.focus()
    else:
        textBistec_pobre.config(state=DISABLED)
        txtBistec_pobre.set('0')

def ceviche():
    if var10.get() == 1:
        textCeviche.config(state=NORMAL)
        textCeviche.delete(0, END)
        textCeviche.focus()
    else:
        textCeviche.config(state=DISABLED)
        txtCeviche.set('0')

# Funciones para activar y desactivar casillas para bebidas
def inka_kola():
    if var11.get() == 1:
        textInka_kola.config(state=NORMAL)
        textInka_kola.delete(0, END)
        textInka_kola.focus()
    else:
        textInka_kola.config(state=DISABLED)
        txtInka_kola.set('0')

def coca_cola():
    if var12.get() == 1:
        textCoca_cola.config(state=NORMAL)
        textCoca_cola.delete(0, END)
        textCoca_cola.focus()
    else:
        textCoca_cola.config(state=DISABLED)
        txtCoca_cola.set('0')

def maracuya():
    if var13.get() == 1:
        textMaracuya.config(state=NORMAL)
        textMaracuya.delete(0, END)
        textMaracuya.focus()
    else:
        textMaracuya.config(state=DISABLED)
        txtMaracuya.set('0')

def cebada():
    if var14.get() == 1:
        textCebada.config(state=NORMAL)
        textCebada.delete(0, END)
        textCebada.focus()
    else:
        textCebada.config(state=DISABLED)
        txtCebada.set('0')

def chicha():
    if var15.get() == 1:
        textChicha.config(state=NORMAL)
        textChicha.delete(0, END)
        textChicha.focus()
    else:
        textChicha.config(state=DISABLED)
        txtChicha.set('0')

def limonada():
    if var16.get() == 1:
        textLimonada.config(state=NORMAL)
        textLimonada.delete(0, END)
        textLimonada.focus()
    else:
        textLimonada.config(state=DISABLED)
        txtLimonada.set('0')

def pina():
    if var17.get() == 1:
        textPina.config(state=NORMAL)
        textPina.delete(0, END)
        textPina.focus()
    else:
        textPina.config(state=DISABLED)
        txtPina.set('0')

def naranja():
    if var18.get() == 1:
        textNaranja.config(state=NORMAL)
        textNaranja.delete(0, END)
        textNaranja.focus()
    else:
        textNaranja.config(state=DISABLED)
        txtNaranja.set('0')

def inka_kola_personal():
    if var19.get() == 1:
        textInka_kola_personal.config(state=NORMAL)
        textInka_kola_personal.delete(0, END)
        textInka_kola_personal.focus()
    else:
        textInka_kola_personal.config(state=DISABLED)
        txtInka_kola_personal.set('0')

def coca_cola_personal():
    if var20.get() == 1:
        textCoca_cola_personal.config(state=NORMAL)
        textCoca_cola_personal.delete(0, END)
        textCoca_cola_personal.focus()
    else:
        textCoca_cola_personal.config(state=DISABLED)
        txtCoca_cola_personal.set('0')

#Funciones para activar o desactivar las casillas de dietas
def pollo_plancha():
    if var21.get() == 1:
        textPollo_plancha.config(state=NORMAL)
        textPollo_plancha.delete(0, END)
        textPollo_plancha.focus()
    else:
        textPollo_plancha.config(state=DISABLED)
        txtPollo_plancha.set('0')

def pollo_sancochado():
    if var22.get() == 1:
        textPollo_sancochado.config(state=NORMAL)
        textPollo_sancochado.delete(0, END)
        textPollo_sancochado.focus()
    else:
        textPollo_sancochado.config(state=DISABLED)
        txtPollo_sancochado.set('0')

def pescado_plancha():
    if var23.get() == 1:
        textPescado_plancha.config(state=NORMAL)
        textPescado_plancha.delete(0, END)
        textPescado_plancha.focus()
    else:
        textPescado_plancha.config(state=DISABLED)
        txtPescado_plancha.set('0')

def pescado_apanado():
    if var24.get() == 1:
        textPescado_apanado.config(state=NORMAL)
        textPescado_apanado.delete(0, END)
        textPescado_apanado.focus()
    else:
        textPescado_apanado.config(state=DISABLED)
        txtPescado_apanado.set('0')

def ensalada_rusa():
    if var25.get() == 1:
        textEnsalada_rusa.config(state=NORMAL)
        textEnsalada_rusa.delete(0, END)
        textEnsalada_rusa.focus()
    else:
        textEnsalada_rusa.config(state=DISABLED)
        txtEnsalada_rusa.set('0')

def ensalada_brocoli():
    if var26.get() == 1:
        textEnsalada_brocoli.config(state=NORMAL)
        textEnsalada_brocoli.delete(0, END)
        textEnsalada_brocoli.focus()
    else:
        textEnsalada_brocoli.config(state=DISABLED)
        txtEnsalada_brocoli.set('0')

def arroz_arabe():
    if var27.get() == 1:
        textArroz_arabe.config(state=NORMAL)
        textArroz_arabe.delete(0, END)
        textArroz_arabe.focus()
    else:
        textArroz_arabe.config(state=DISABLED)
        txtArroz_arabe.set('0')

def ensalada_pepino():
    if var28.get() == 1:
        textEnsalada_pepino.config(state=NORMAL)
        textEnsalada_pepino.delete(0, END)
        textEnsalada_pepino.focus()
    else:
        textEnsalada_pepino.config(state=DISABLED)
        txtEnsalada_pepino.set('0')

def ensalada_quinua():
    if var29.get() == 1:
        textEnsalada_quinua.config(state=NORMAL)
        textEnsalada_quinua.delete(0, END)
        textEnsalada_quinua.focus()
    else:
        textEnsalada_quinua.config(state=DISABLED)
        txtEnsalada_quinua.set('0')

def ensalada_coliflor():
    if var30.get() == 1:
        textEnsalada_coliflor.config(state=NORMAL)
        textEnsalada_coliflor.delete(0, END)
        textEnsalada_coliflor.focus()
    else:
        textEnsalada_coliflor.config(state=DISABLED)
        txtEnsalada_coliflor.set('0')



#diseño de la ventana principal
ventana = Tk()
ventana.title("SARITA COLONIA")
ventana.state("zoomed")  # Maximizar ventana automáticamente
#ventana.geometry("1500x800")  # Dimensiones iniciales de la ventana
ventana.resizable(True, True)  # Permitir redimensionar la ventana
ventana.config(bg="lightgreen")

#estableciento las fuentes
Title=("arial black",25)
Subtitle=("consolas", 14)

#marco de titulo principal
marcoSuperior=Frame(ventana,bd=12, relief=RIDGE,bg="green")
marcoSuperior.pack(side=TOP)
#titulo principal
tituloPrincipal=Label(marcoSuperior,text="RESTAURANTE SARITA COLONIA", font=Title, fg="white",bg="green",width=53)
tituloPrincipal.grid(row=0,column=0)

#marcos secundarios
marcoMenu=Frame(ventana, bd=10, relief=RIDGE, bg="green")
marcoMenu.pack(side=LEFT)
marcoCosto=Frame(marcoMenu, bd=2, relief=RIDGE, bg="green")
marcoCosto.pack(side=BOTTOM)
marcoComida=LabelFrame(marcoMenu,text='Platillos', bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
marcoComida.pack(side=LEFT)
marcoBebidas=LabelFrame(marcoMenu,text='Bebidas', bd=5,font=Subtitle, relief=RIDGE, bg="lightgray")
marcoBebidas.pack(side=LEFT)
marcoDieta=LabelFrame(marcoMenu,text='Dietas', bd=5,font=Subtitle, relief=RIDGE, bg="lightgray")
marcoDieta.pack(side=LEFT)

#marcos para el lado derecho
marcoDerecho=Frame(ventana,bd=10, relief=RIDGE, bg="green")
marcoDerecho.pack(side=RIGHT)
marcoMesas=Frame(marcoDerecho,bd=5, relief=RIDGE, bg="lightgray")
marcoMesas.pack()
marcoRecibo=Frame(marcoDerecho,bd=5, relief=RIDGE,bg="green")
marcoRecibo.pack()
marcoBotones=Frame(marcoDerecho,bd=5, relief=RIDGE, bg="green")
marcoBotones.pack()

#variableAusar
#variables para comida
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
#variables para las bebidas
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
#varibles para las dietas
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()

#Variables para las cajas de texto de la comida
txtLomito_saltado_pollo=StringVar()
txtLomito_saltado_pollo.set('0')
txtLomito_saltado_carne=StringVar()
txtLomito_saltado_carne.set('0')
txtTallarines_verdes_pollo=StringVar()
txtTallarines_verdes_pollo.set('0')
txtChicharron_pollo=StringVar()
txtChicharron_pollo.set('0')
txtFilete_pollo=StringVar()
txtFilete_pollo.set('0')
txtTallarin_saltado_pollo=StringVar()
txtTallarin_saltado_pollo.set('0')
txtTallarines_rojos=StringVar()
txtTallarines_rojos.set('0')
txtArroz_Chaufa_pollo=StringVar()
txtArroz_Chaufa_pollo.set('0')
txtBistec_pobre=StringVar()
txtBistec_pobre.set('0')
txtCeviche=StringVar()
txtCeviche.set('0')

#variables para las cajas de texto de las bebidas
txtInka_kola=StringVar()
txtInka_kola.set('0')
txtCoca_cola=StringVar()
txtCoca_cola.set('0')
txtMaracuya=StringVar()
txtMaracuya.set('0')
txtCebada=StringVar()
txtCebada.set('0')
txtChicha=StringVar()
txtChicha.set('0')
txtLimonada=StringVar()
txtLimonada.set('0')
txtPina=StringVar()
txtPina.set('0')
txtNaranja=StringVar()
txtNaranja.set('0')
txtInka_kola_personal=StringVar()
txtInka_kola_personal.set('0')
txtCoca_cola_personal=StringVar()
txtCoca_cola_personal.set('0')

#variables para las cajas de texto de dietas
txtPollo_plancha=StringVar()
txtPollo_plancha.set('0')
txtPollo_sancochado=StringVar()
txtPollo_sancochado.set('0')
txtPescado_plancha=StringVar()
txtPescado_plancha.set('0')
txtPescado_apanado=StringVar()
txtPescado_apanado.set('0')
txtEnsalada_rusa=StringVar()
txtEnsalada_rusa.set('0')
txtEnsalada_brocoli=StringVar()
txtEnsalada_brocoli.set('0')
txtArroz_arabe=StringVar()
txtArroz_arabe.set('0')
txtEnsalada_pepino=StringVar()
txtEnsalada_pepino.set('0')
txtEnsalada_quinua=StringVar()
txtEnsalada_quinua.set('0')
txtEnsalada_coliflor=StringVar()
txtEnsalada_coliflor.set('0')

#variables pra las casillas de subtotales y total 
varcostocomida=StringVar()
varcostobebida=StringVar()
varcostodieta=StringVar()
varsubtotal=StringVar()
varigv=StringVar()
vartotal=StringVar()


#comida
#etiqueta y boton para seleccionar
Lomito_saltado_pollo=Checkbutton(marcoComida,text='LOMITO DE POLLO',font=Subtitle,onvalue=1,offvalue=0,variable=var1,command=lomito_saltado_pollo)
Lomito_saltado_pollo.grid(row=0,column=0,sticky=W)
Lomito_saltado_carne=Checkbutton(marcoComida,text='LOMITO DE CARNE',font=Subtitle,onvalue=1,offvalue=0,variable=var2,command=lomito_saltado_carne)
Lomito_saltado_carne.grid(row=1,column=0,sticky=W)
Tallarines_verdes_pollo=Checkbutton(marcoComida,text='TALLARINES VERDES',font=Subtitle,onvalue=1,offvalue=0,variable=var3,command=tallarines_verdes_pollo)
Tallarines_verdes_pollo.grid(row=2,column=0,sticky=W)
Chicharron_pollo=Checkbutton(marcoComida,text='CHICHARRON DE POLLO',font=Subtitle,onvalue=1,offvalue=0,variable=var4, command=chicharron_pollo)
Chicharron_pollo.grid(row=3,column=0,sticky=W)
Filete_pollo=Checkbutton(marcoComida,text='FILETE DE POLLO',font=Subtitle,onvalue=1,offvalue=0,variable=var5, command=filete_pollo)
Filete_pollo.grid(row=4,column=0,sticky=W)
Tallarin_saltado_pollo=Checkbutton(marcoComida,text='TALLARIN SALTADO',font=Subtitle,onvalue=1,offvalue=0,variable=var6, command=tallarin_saltado_pollo)
Tallarin_saltado_pollo.grid(row=5,column=0,sticky=W)
Tallarines_rojos=Checkbutton(marcoComida,text='TALLARINES ROJOS',font=Subtitle,onvalue=1,offvalue=0,variable=var7, command=tallarines_rojos)
Tallarines_rojos.grid(row=6,column=0,sticky=W)
Arroz_Chaufa_pollo=Checkbutton(marcoComida,text='ARROZ CHAUFA',font=Subtitle,onvalue=1,offvalue=0,variable=var8, command=arroz_chaufa_pollo)
Arroz_Chaufa_pollo.grid(row=7,column=0,sticky=W)
Bistec_pobre=Checkbutton(marcoComida,text='BISTEC A LO POBRE',font=Subtitle,onvalue=1,offvalue=0,variable=var9, command=bistec_pobre)
Bistec_pobre.grid(row=8,column=0,sticky=W)
Ceviche=Checkbutton(marcoComida,text='CEVICHE',font=Subtitle,onvalue=1,offvalue=0,variable=var10, command=ceviche)
Ceviche.grid(row=9,column=0,sticky=W)

#cajas de texto para cada comida
textLomito_saltado_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtLomito_saltado_pollo)
textLomito_saltado_pollo.grid(row=0,column=1)
textLomito_saltado_carne=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtLomito_saltado_carne)
textLomito_saltado_carne.grid(row=1,column=1)
textTallarines_verdes_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtTallarines_verdes_pollo)
textTallarines_verdes_pollo.grid(row=2,column=1)
textChicharron_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtChicharron_pollo)
textChicharron_pollo.grid(row=3,column=1)
textFilete_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtFilete_pollo)
textFilete_pollo.grid(row=4,column=1)
textTallarin_saltado_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtTallarin_saltado_pollo)
textTallarin_saltado_pollo.grid(row=5,column=1)
textTallarines_rojos=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtTallarines_rojos)
textTallarines_rojos.grid(row=6,column=1)
textArroz_Chaufa_pollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtArroz_Chaufa_pollo)
textArroz_Chaufa_pollo.grid(row=7,column=1)
textBistec_pobre=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtBistec_pobre)
textBistec_pobre.grid(row=8,column=1)
textCeviche=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCeviche)
textCeviche.grid(row=9,column=1)

#bebidas
#etiqueta y boton check
Inka_kola=Checkbutton(marcoBebidas,text='1L.INKA KOLA',font=Subtitle,onvalue=1,offvalue=0,variable=var11, command=inka_kola)
Inka_kola.grid(row=0,column=0,sticky=W)
Coca_cola=Checkbutton(marcoBebidas,text='1L.COCA COLA',font=Subtitle,onvalue=1,offvalue=0,variable=var12, command=coca_cola)
Coca_cola.grid(row=1,column=0,sticky=W)
Maracuya=Checkbutton(marcoBebidas,text='1/2 J.MARACUYA',font=Subtitle,onvalue=1,offvalue=0,variable=var13, command=maracuya)
Maracuya.grid(row=2,column=0,sticky=W)
Cebada=Checkbutton(marcoBebidas,text='1/2 J.CEBADA',font=Subtitle,onvalue=1,offvalue=0,variable=var14, command=cebada)
Cebada.grid(row=3,column=0,sticky=W)
Chicha=Checkbutton(marcoBebidas,text='1/2 J.CHICHA',font=Subtitle,onvalue=1,offvalue=0,variable=var15, command=chicha)
Chicha.grid(row=4,column=0,sticky=W)
Limonada=Checkbutton(marcoBebidas,text='1/2 J.LIMONADA',font=Subtitle,onvalue=1,offvalue=0,variable=var16, command=limonada)
Limonada.grid(row=5,column=0,sticky=W)
Pina=Checkbutton(marcoBebidas,text='1/2 J.PIÑA',font=Subtitle,onvalue=1,offvalue=0,variable=var17, command=pina)
Pina.grid(row=6,column=0,sticky=W)
Naranja=Checkbutton(marcoBebidas,text='1/2 J.NARANJA',font=Subtitle,onvalue=1,offvalue=0,variable=var18, command=naranja)
Naranja.grid(row=7,column=0,sticky=W)
Inka_kola_personal=Checkbutton(marcoBebidas,text='PER.INKA KOLA',font=Subtitle,onvalue=1,offvalue=0,variable=var19, command=inka_kola_personal)
Inka_kola_personal.grid(row=8,column=0,sticky=W)
Coca_cola_personal=Checkbutton(marcoBebidas,text='PER.COCA COLA',font=Subtitle,onvalue=1,offvalue=0,variable=var20, command=coca_cola_personal)
Coca_cola_personal.grid(row=9,column=0,sticky=W)

#casilla de entrada 
textInka_kola=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtInka_kola)
textInka_kola.grid(row=0,column=1)
textCoca_cola=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCoca_cola)
textCoca_cola.grid(row=1,column=1)
textMaracuya=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtMaracuya)
textMaracuya.grid(row=2,column=1)
textCebada=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCebada)
textCebada.grid(row=3,column=1)
textChicha=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtChicha)
textChicha.grid(row=4,column=1)
textLimonada=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtLimonada)
textLimonada.grid(row=5,column=1)
textPina=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPina)
textPina.grid(row=6,column=1)
textNaranja=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtNaranja)
textNaranja.grid(row=7,column=1)
textInka_kola_personal=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtInka_kola_personal)
textInka_kola_personal.grid(row=8,column=1)
textCoca_cola_personal=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCoca_cola_personal)
textCoca_cola_personal.grid(row=9,column=1)


#dieta
#etiqueta y boton check
Pollo_plancha=Checkbutton(marcoDieta,text='POLLO A LA PLANCHA',font=Subtitle,onvalue=1,offvalue=0,variable=var21,command=pollo_plancha)
Pollo_plancha.grid(row=0,column=0,sticky=W)
Pollo_sancochado=Checkbutton(marcoDieta,text='POLLO SANCOCHADO',font=Subtitle,onvalue=1,offvalue=0,variable=var22,command=pollo_sancochado)
Pollo_sancochado.grid(row=1,column=0,sticky=W)
Pescado_plancha=Checkbutton(marcoDieta,text='PESCADO A LA PLANCHA',font=Subtitle,onvalue=1,offvalue=0,variable=var23,command=pescado_plancha)
Pescado_plancha.grid(row=2,column=0,sticky=W)
Pescado_apanado=Checkbutton(marcoDieta,text='PESCADO APANADO',font=Subtitle,onvalue=1,offvalue=0,variable=var24,command=pescado_apanado)
Pescado_apanado.grid(row=3,column=0,sticky=W)
Ensalada_rusa=Checkbutton(marcoDieta,text='ENSALADA RUSA',font=Subtitle,onvalue=1,offvalue=0,variable=var25,command=ensalada_rusa)
Ensalada_rusa.grid(row=4,column=0,sticky=W)
Ensalada_brocoli=Checkbutton(marcoDieta,text='ENSALADA BROCOLÍ',font=Subtitle,onvalue=1,offvalue=0,variable=var26,command=ensalada_brocoli)
Ensalada_brocoli.grid(row=5,column=0,sticky=W)
Arroz_arabe=Checkbutton(marcoDieta,text='ARROZ ÁRABE',font=Subtitle,onvalue=1,offvalue=0,variable=var27,command=arroz_arabe)
Arroz_arabe.grid(row=6,column=0,sticky=W)
Ensalada_pepino=Checkbutton(marcoDieta,text='ENSALADA PEPINO',font=Subtitle,onvalue=1,offvalue=0,variable=var28,command=ensalada_pepino)
Ensalada_pepino.grid(row=7,column=0,sticky=W)
Ensalada_quinua=Checkbutton(marcoDieta,text='ENSALADA QUINUA',font=Subtitle,onvalue=1,offvalue=0,variable=var29,command=ensalada_quinua)
Ensalada_quinua.grid(row=8,column=0,sticky=W)
Ensalada_coliflor=Checkbutton(marcoDieta,text='ENSALADA COLIFLOR',font=Subtitle,onvalue=1,offvalue=0,variable=var30,command=ensalada_coliflor)
Ensalada_coliflor.grid(row=9,column=0,sticky=W)

#casilla de dietas
textPollo_plancha=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPollo_plancha)
textPollo_plancha.grid(row=0,column=1)
textPollo_sancochado=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPollo_sancochado)
textPollo_sancochado.grid(row=1,column=1)
textPescado_plancha=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPescado_plancha)
textPescado_plancha.grid(row=2,column=1)
textPescado_apanado=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPescado_apanado)
textPescado_apanado.grid(row=3,column=1)
textEnsalada_rusa=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada_rusa)
textEnsalada_rusa.grid(row=4,column=1)
textEnsalada_brocoli=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada_brocoli)
textEnsalada_brocoli.grid(row=5,column=1)
textArroz_arabe=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtArroz_arabe)
textArroz_arabe.grid(row=6,column=1)
textEnsalada_pepino=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada_pepino)
textEnsalada_pepino.grid(row=7,column=1)
textEnsalada_quinua=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada_quinua)
textEnsalada_quinua.grid(row=8,column=1)
textEnsalada_coliflor=Entry(marcoDieta,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada_coliflor)
textEnsalada_coliflor.grid(row=9,column=1)

#etiquetas de totales y entradas para los valores
costoComida=Label(marcoCosto, text="TOTAL EN COMIDAS", font=Subtitle, bd=10, bg="green",fg="white")
costoComida.grid(row=0,column=0)
casillaCostoComida=Entry(marcoCosto,font=Subtitle,bd=10, width=14, state="readonly", textvariable=costoComida)
casillaCostoComida.grid(row=0, column=1, padx=5)
costoBebidas=Label(marcoCosto, text="TOTAL EN BEBIDAS", font=Subtitle,bd=10,width=14, bg="green",fg="white")
costoBebidas.grid(row=1,column=0)
casillasCostoBebidas=Entry(marcoCosto, font=Subtitle,bd=10,width=14, fg="white", bg="green", state="readonly", textvariable=costoBebidas)
casillasCostoBebidas.grid(row=1,column=1)
costoDieta=Label(marcoCosto,font=Subtitle,text="TOTAL EN DIETAS", bd=10,bg="green", fg="white")
costoDieta.grid(row=2,column=0)
casillaCostoDieta=Entry(marcoCosto,font=Subtitle,state="readonly",bd=10,width=14, textvariable=costoDieta)
casillaCostoDieta.grid(row=2,column=1)

subtotal=Label(marcoCosto, text="SUBTOTAL", font=Subtitle,bd=10, bg="green",fg="white")
subtotal.grid(row=0,column=2)
casillasubtotal=Entry(marcoCosto,font=Subtitle,bd=10, width=14, state="readonly", textvariable=subtotal)
casillasubtotal.grid(row=0, column=3, padx=41)
igv=Label(marcoCosto, text="IGV", font=Subtitle,bd=10,width=14, bg="green",fg="white")
igv.grid(row=1,column=2)
casillasigv=Entry(marcoCosto, font=Subtitle,bd=10,width=14, fg="white", bg="green", state="readonly", textvariable=igv)
casillasigv.grid(row=1,column=3)
pagoTotal=Label(marcoCosto,font=Subtitle,text="PAGO TOTAL", bd=10,bg="green", fg="white")
pagoTotal.grid(row=2,column=2)
casillapagoTotal=Entry(marcoCosto,font=Subtitle,state="readonly",bd=10,width=14)
casillapagoTotal.grid(row=2,column=3)

#programacion mesas

# Variables para el estado de las mesas
estados_mesas = [StringVar() for _ in range(30)]
for i in range(30):
    estados_mesas[i].set("Libre")

def cambiar_estado_mesa(numero_mesa):
    if estados_mesas[numero_mesa].get() == "Libre":
        estados_mesas[numero_mesa].set("Ocupada")
        botones_mesas[numero_mesa].config(bg="red")
    else:
        estados_mesas[numero_mesa].set("Libre")
        botones_mesas[numero_mesa].config(bg="green")

# Crear botones para las mesas
botones_mesas = []
for i in range(30):
    fila = i // 6
    columna = i % 6
    boton = Button(marcoMesas, text=f"Mesa {i+1}", font=('arial', 8), 
                   fg="white", bg="green", bd=3, width=8, height=2,
                   command=lambda x=i: cambiar_estado_mesa(x))
    boton.grid(row=fila, column=columna, padx=2, pady=2)
    botones_mesas.append(boton)

# Etiqueta para mostrar el estado de las mesas
etiqueta_estado = Label(marcoMesas, text="Verde: Libre | Rojo: Ocupada", 
                        font=('arial', 10), bg="lightgreen")
etiqueta_estado.grid(row=5, column=0, columnspan=6, pady=5)



# recibo
textoRecibo=Text(marcoRecibo, font=('arial',12,'bold'),bd=3,width=48,height=12)
textoRecibo.grid(row=0,column=0)
#botones
botonTotal=Button(marcoBotones,text='TOTAL',font=Subtitle, fg="white",bg="green",bd=4,padx=5, command=grantotal).grid(row=0,column=0)
botonRecibo=Button(marcoBotones,text='RECIBO',font=Subtitle, fg="white",bg="green",bd=4,padx=5, command=recibo).grid(row=0,column=1)
botonGuardar=Button(marcoBotones,text='GUARDAR',font=Subtitle, fg="white",bg="green",bd=4,padx=5, command=guardar).grid(row=0,column=2)
botonEnviar=Button(marcoBotones,text='ENVIAR',font=Subtitle, fg="white",bg="green",bd=4,padx=5, command=enviar).grid(row=0,column=3)
botonBorrar=Button(marcoBotones,text='BORRAR',font=Subtitle, fg="white",bg="green",bd=4,padx=5, command=borrar)
botonBorrar.grid(row=0,column=4)


ventana.mainloop()

#===================================================================================================================================

