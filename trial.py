
from tkinter import *
from tkinter import ttk  
#from vidstream import StreamingServer
import socket, argparse, time, sys, tkinter, os, threading,customtkinter


parser = argparse.ArgumentParser(
    description="EYES (Surveillance Software)"
)


    


def on_closing(event=None):
    sys.exit()
    

    
def send():
    show_dashboard()


def show_dashboard():
    # Destroy login page widgets
    

    newWindow = customtkinter.CTkToplevel(master=app)
    newWindow.title("EYES")
    newWindow.configure(bg="000000",fg="green")
    # sets the geometry of toplevel
    newWindow.geometry("300x400")
    lbl= customtkinter.CTkLabel(master=newWindow ,text='Slave List',text_color="green", font=('Times New Roman', 20,"bold"))
    lbl.grid(row=1, column=0, pady=10, padx=20)
    listbox = customtkinter.CTkScrollableFrame(master=newWindow)
    listbox.pack()
    label12 = customtkinter.CTkLabel(newWindow,text='ansh_mac 192.168.1.12 ACTIVE')
    label12.pack()

   
  











app = customtkinter.CTk()
app.geometry("1240x700")
app.title("EYES (Surveillance Software)")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)


app.frame_left = customtkinter.CTkFrame(master=app, width=180, corner_radius=10)
app.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

app.frame_right = customtkinter.CTkFrame(master=app, width=180, corner_radius=10)
app.frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nswe")


app.frame_left.grid_rowconfigure(0, minsize=10) 
app.frame_left.grid_rowconfigure(5, weight=1)
app.frame_left.grid_rowconfigure(8, minsize=20)
app.frame_left.grid_rowconfigure(11, minsize=10)

app.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
app.frame_right.rowconfigure(7, weight=10)
app.frame_right.columnconfigure((0, 1), weight=1)
app.frame_right.columnconfigure(2, weight=0)


app.label_2 = customtkinter.CTkLabel(master=app.frame_left, text='EYES (Surveillance Software)',text_color="red", font=('Times New Roman', 20,"bold"))
app.label_2.grid(row=1, column=0, pady=10, padx=20)

label_3 = customtkinter.CTkLabel(master=app.frame_right, text='CONNECTION INFO')
label_3.pack(pady=12, padx=12)

messages_frame = tkinter.Frame(app.frame_right)
my_msg = tkinter.StringVar()
scrollbar = tkinter.Scrollbar(messages_frame, bg='#0f0f0f')
msg_list = tkinter.Listbox(messages_frame, height=10, width=110, yscrollcommand=scrollbar.set, bg="black",fg='green', font=("Roboto Medium", 12))
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack(pady=15, padx=40, fill="both", expand=True)

entry_field = customtkinter.CTkEntry(master=app.frame_right, placeholder_text="command", width=500, height=25, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack(pady=20, padx=60)
send_button = customtkinter.CTkButton(master=app.frame_right, text="Send", bg_color="yellow",fg_color="black",hover="red")
send_button.pack(pady=20, padx=60)
select_slave = customtkinter.CTkButton(master=app.frame_right, text="Select slave", command=show_dashboard,bg_color="yellow",fg_color="black",hover="red")
select_slave.pack(pady=20, padx=60)
lo = customtkinter.CTkButton(master=app.frame_right, text="Logout", command=send,bg_color="red",fg_color="black",hover="yellow")
lo.pack(pady=20)



app.label_mode = customtkinter.CTkLabel(master=app.frame_left, text="Menu",font=("Roboto Medium", 15,"bold"))
app.label_mode.grid(row=12, column=0, pady=0, padx=20, sticky="w")


app.optionmenu_1 = customtkinter.CTkOptionMenu(master=app.frame_left, values=["INTERACT", "INFECT", "GENERATE"],bg_color="yellow",fg_color="black",hover="red")
app.optionmenu_1.grid(row=13, column=0, pady=15, padx=20, sticky="w")


my_msg_sendfile = tkinter.StringVar()
entry_field_sendfile = customtkinter.CTkEntry(master=app.frame_left, placeholder_text="PATH", width=130, height=25, textvariable=my_msg_sendfile)
entry_field_sendfile.bind("<Return>", send)
entry_field_sendfile.grid(row=2, column=0, pady=10, padx=20)
send_button_sendfile = customtkinter.CTkButton(master=app.frame_left, text="TRANSFER FILE", bg_color="yellow",fg_color="black",hover="red")
send_button_sendfile.grid(row=3, column=0, pady=10, padx=20)


my_msg_getfile = tkinter.StringVar()
entry_field_getfile = customtkinter.CTkEntry(master=app.frame_left, placeholder_text="command", width=130, height=25, textvariable=my_msg_getfile)
entry_field_getfile.bind("<Return>", send)
entry_field_getfile.grid(row=4, column=0, pady=10, padx=20)
send_button_getfile = customtkinter.CTkButton(master=app.frame_left, text="EXPORT FILE", bg_color="yellow",fg_color="black",hover="red")
send_button_getfile.grid(row=5, column=0, pady=10, padx=20)


start_logger_button = customtkinter.CTkButton(master=app.frame_left, text="CAPTURE WEB TRAFFIC", bg_color="yellow",fg_color="black",hover="red")
start_logger_button.grid(row=6, column=0, pady=10, padx=20)

stop_logger_button = customtkinter.CTkButton(master=app.frame_left, text="KEYLOGGER", bg_color="yellow",fg_color="black",hover="red")
stop_logger_button.grid(row=7, column=0, pady=10, padx=20)

placeholder_button = customtkinter.CTkButton(master=app.frame_left, text="ACTIVATE RSHELL",bg_color="yellow",fg_color="black",hover="red")
placeholder_button.grid(row=8, column=0, pady=10, padx=20)

placeholder_button = customtkinter.CTkButton(master=app.frame_left, text="STREAM WEBCAM",bg_color="yellow",fg_color="black",hover="red")
placeholder_button.grid(row=9, column=0, pady=10, padx=20)

placeholder_button = customtkinter.CTkButton(master=app.frame_left, text="CAPTURE SCREENSHOT",bg_color="yellow",fg_color="black",hover="red")
placeholder_button.grid(row=10, column=0, pady=10, padx=20)

placeholder_button = customtkinter.CTkButton(master=app.frame_left, text="CLEAN UP",bg_color="yellow",fg_color="black",hover="red")
placeholder_button.grid(row=11, column=0, pady=10, padx=20)






app.protocol("WM_DELETE_WINDOW", on_closing)

msg_list.insert(tkinter.END, f"\n $> ")

app.mainloop()