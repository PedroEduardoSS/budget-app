from dearpygui.dearpygui import *
from control.budget_ctrl import *

budget_ctrl = Budget_Ctrl()


def budget_window():
    with window(label="Orçamentos", width=400):
        with group(horizontal=True, horizontal_spacing=50):
            with group(tag="budget_inputs", width=100):
                add_input_text(label="Title", tag="title")
                add_input_text(label="Email", tag="email")

            with group(tag="user_outputs", width=200):
                add_listbox(width=100, tag="list", items=user_ctrl.users)

        with group(horizontal=True):
            add_button(label="Criar", callback=criar)
            add_button(label="Ler", callback=ler)
            add_button(label="Editar", callback=editar)
            add_button(label="Deletar", callback=deletar)
        
        add_radio_button(tag="radio", items=("", "Name", "Email"))