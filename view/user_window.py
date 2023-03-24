from dearpygui.dearpygui import *
from control.user_ctrl import *
#from model.user import User

user_ctrl = User_Ctrl()

def criar():
    user_ctrl.create_user(get_value("id"), get_value("name"), get_value("email"))
    configure_item("list", items=user_ctrl.users)

def ler():
    with window(label="Resultado", modal=True):
        add_text(get_value("list"))

def editar():
    if get_value("radio") == "Name":
        user_ctrl.update_user(get_value("id"), get_value("radio"), get_value("name"))
        configure_item("list", items=user_ctrl.users)
    elif get_value("radio") == "Email":
        user_ctrl.update_user(get_value("id"), get_value("radio"), get_value("email"))
        configure_item("list", items=user_ctrl.users)

def deletar():
    user_ctrl.delete_user(get_value("id"))
    configure_item("list", items=user_ctrl.users)

def user_window():
    with window(label="Usuários", width=400):
        with group(horizontal=True, horizontal_spacing=50):
            with group(tag="user_inputs", width=100):
                add_input_int(label="ID", tag="id")
                add_input_text(label="Name", tag="name")
                add_input_text(label="Email", tag="email")

            with group(tag="user_outputs", width=200):
                add_listbox(width=100, tag="list", items=user_ctrl.users)

        with group(horizontal=True):
            add_button(label="Criar", callback=criar)
            add_button(label="Ler", callback=ler)
            add_button(label="Editar", callback=editar)
            add_button(label="Deletar", callback=deletar)
        
        add_radio_button(tag="radio", items=("", "Name", "Email"))