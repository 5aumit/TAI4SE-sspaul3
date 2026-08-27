import tkinter as tk
from tkinter import ttk

from tkinter import messagebox
from Clases.calendarioExamenes import CalendarioExamenes
from tkcalendar import Calendar, DateEntry
import datetime
from datetime import date,timedelta
from Clases.jsonConverter import jsonConverter
import showCalendars as sW
import threading
from tkinter.ttk import Progressbar

class SubWindow(tk.Toplevel):
    def __init__(self, master, *argv):
        super().__init__(master)
        self._second_window = None
        self.grupo = argv[0][1]
        self.title("Generar Excel del {}".format(self.grupo))
        for i in range(3):
            self.columnconfigure(i, weight=1)


            self.rowconfigure(i, weight=1)
        self.calendario = argv[0][0]
        self.txts = ["" for x in range(6)]
        
        # Change what happens when you click the X button
        # This is done so changes also reflect in the main window class
        self.protocol('WM_DELETE_WINDOW', master.close)

        self.lbl1 = ttk.Label(self, text="Parcial 1")
        self.lbl1.grid(column=0, row=0,sticky="nsew", padx=10, pady=5)
        self.lbl2 = ttk.Label(self, text="Parcial 2")
        self.lbl2.grid(column=0, row=1,sticky="nsew", padx=10, pady=5)
        self.lbl3 = ttk.Label(self, text="Parcial 3")
        self.lbl3.grid(column=0, row=2,sticky="nsew", padx=10, pady=5)

        self.txts[0] = ttk.Entry(self, text="")
        self.txts[0].grid(column = 1, row = 0,columnspan=2)
        self.txts[1] = ttk.Entry(self, text="")
        self.txts[1].grid(column = 1, row = 1,columnspan=2)
        self.txts[2] = ttk.Entry(self, text="")
        self.txts[2].grid(column = 1, row = 2,columnspan=2)

        self.lbl4 = ttk.Label(self, text="Fecha ordinario")
        self.lbl4.grid(column=3, row=0,sticky=tk.W, padx=5)
        self.lbl5 = ttk.Label(self, text="Fecha extraordinario 1")
        self.lbl5.grid(column=3, row=1, padx=5)
        self.lbl6 = ttk.Label(self, text="Fecha extraordinario 2")
        self.lbl6.grid(column=3, row=2, padx=5)

        self.txts[3] = ttk.Entry(self, text="")
        self.txts[3].grid(column = 4, row = 0,columnspan=2, padx=10, pady=5)
        self.txts[4] = ttk.Entry(self, text="")
        self.txts[4].grid(column = 4, row = 1,columnspan=2, padx=10, pady=5)
        self.txts[5] = ttk.Entry(self, text="")
        self.txts[5].grid(column = 4, row = 2,columnspan=2, padx=10, pady=5)

        self.btn = ttk.Button(self, text="Generar Excel", command= lambda : self.generateExcel())
        self.btn.grid(column= 4, row=3,sticky="nsew", columnspan=2, padx=5, pady=5, ipadx=5, ipady=5)

        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL,length=100,  mode='indeterminate')

        now = datetime.datetime.now()
        self.dia =now.day
        self.mes =now.month
        self.anio =now.year

        for i in range(6):
            self.txts[i].bind("<Button-1>", self.tkinterCalendar)


    def tkinterCalendar(self, event):
        # respuesta = tk.messagebox.askquestion(parent=self, message="¿Cuenta con la fecha especifica? \n\n Conteste NO para guardar como PENDIENTE", title="Agregar fecha",icon = 'info')
        # if respuesta == 'yes':
            def print_sel():
                f = (cal.selection_get()).weekday()
                if f < 5:
                    event.widget.config(state="normal")
                    self.updateDate(cal.selection_get())
                    event.widget.delete(0, tk.END)
                    event.widget.insert(0, cal.selection_get())
                    event.widget.config(state="disabled")
                    top.destroy()
                else:
                    tk.messagebox.showerror(parent=top, message="Por favor elija un dia valido", title="Seleccionar fecha")

            def print_pendiente():
                event.widget.config(state="normal")
                self.updateDate(cal.selection_get())
                event.widget.delete(0, tk.END)
                event.widget.insert(0, 'Pediente')
                event.widget.config(state="disabled")
                top.destroy()
        
            top = tk.Toplevel(self)
            cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=self.anio, month=self.mes, day=self.dia)
            cal.pack(fill="both", expand=True)
            ttk.Button(top, text="ok", command=print_sel).pack(expand=True, fill=tk.BOTH, ipadx=10, ipady=10, pady=2)   
            ttk.Button(top, text="Guardar como pendiente", command= print_pendiente).pack(expand=True, fill=tk.BOTH, ipadx=10, ipady=10, pady=2)   
        # else:
    def updateDate(self, date):
        self.dia =  date.day
        self.mes =  date.month
        self.anio = date.year
        
    def generateExcel(self):
        def real_traitement():
            self.progress.grid(row=4,column=0,columnspan=6, sticky="nsew")
            self.progress.start()
            
            json = jsonConverter()
            fechas = json.getFechas(self)
            calendariosExamenes = []
            fechaInicio= []
            fechaFinal = []
            listaMateriasNoAplicadas = []
            listaMateriasNoAplicadas2 = []
            for i in range(6):
                fecha = self.txts[i].get()
                if fecha == None or fecha == '' or fecha == 'Pediente':
                    fechaInicio.append('Pendiente')
                    fechaFinal.append('Pendiente')
                    calendariosExamenes.append(
                        'Pendiente'
                    ) 
                else: 
                    array = json.getCalendario(self, self.grupo)
                    fecha = fecha.split('-')
                    objCalendarioExamenes = CalendarioExamenes(array, self.grupo, fechas, fecha)
                    if i < 4:
                        examenes = objCalendarioExamenes.crearCalendarioExmanes()
                    else:
                        examenes = objCalendarioExamenes.crearCalendarioExamenesExtraordinarios()
                         
                    fechaInicio.append(objCalendarioExamenes.fechaInicio)
                    fechaFinal.append(fecha)
                    calendariosExamenes.append(
                        examenes
                    )
                    listaMateriasNoAplicadas.append(
                        objCalendarioExamenes.listaMateriasNoAplicadas
                    )
                    listaMateriasNoAplicadas2.append(
                        objCalendarioExamenes.listaMateriasNoAplicadas
                    )
                    
            array = json.getCalendario(self, self.grupo)    
            self.new_window(calendariosExamenes, array, fechaInicio, self.grupo, fechaFinal, listaMateriasNoAplicadas, listaMateriasNoAplicadas2)

            self.progress.stop()
            self.progress.grid_forget()
            
        threading.Thread(target=real_traitement).start()

        

    def new_window(self, *argv):
        # This prevents multiple clicks opening multiple windows
        if self._second_window is not None:
            return

        self._second_window = sW.SubWindow(self, argv)

    def close(self):
        # Destory the 2nd window and reset the value to None
        if self._second_window is not None:
            self._second_window.destroy()
            self._second_window = None 
        

       
