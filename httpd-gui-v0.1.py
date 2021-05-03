from tkinter import *
import subprocess


def cmd_status():
    comando = subprocess.run(['systemctl', 'status', 'httpd'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    mensaje = comando.stdout

    label_status = Label(v_general, text=mensaje, bg='#eeeeee').place(x=200, y=10)
    print(type(mensaje))


def cmd_start():
    comando = subprocess.run(['systemctl', 'start', 'httpd'])
    mensaje = comando.returncode
    if mensaje == 0:
        label_start = Label(v_general, text='Se Inicio el servicio HTTPD.', bg='#eeeeee').place(x=200, y=10)
    else:
        return "Error"


def cmd_restart():
    comando = subprocess.run(['systemctl', 'restart', 'httpd'])
    mensaje = comando.returncode
    if mensaje == 0:
        label_restart = Label(v_general, text='Se Reinicio el servicio HTTPD.', bg='#eeeeee').place(x=200, y=10)
    else:
        return "Error"


def cmd_stop():
    comando = subprocess.run(['systemctl', 'stop', 'httpd'])
    mensaje = comando.returncode
    if mensaje == 0:
        label_restart = Label(v_general, text='Se Debuto el servicio HTTPD.', bg='#eeeeee').place(x=200, y=10)
    else:
        return "Error"


v_general = Tk()
v_general.title('HTPD-Gui')
v_general.geometry("1053x395")
boton_start = Button(v_general, text='▶ Iniciar Servicio️', command=cmd_start, width=20).place(x=6, y=10)
boton_restart = Button(v_general, text='🔃 Reiniciar Servicio', command=cmd_restart, width=20).place(x=6, y=90)
boton_stop = Button(v_general, text='⏹️ Detener Servicio', command=cmd_stop, width=20).place(x=6, y=50)
boton_status = Button(v_general, text='❗ Ver status', command=cmd_status, width=20).place(x=6, y=130)
info = Label(v_general, text='Panel de basico de control.').place(x=15, y=160)

v_general.mainloop()
