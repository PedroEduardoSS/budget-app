from dearpygui.dearpygui import *
from view.user_window import *

create_context()
create_viewport(title='Budget App')
setup_dearpygui()

user_window()

show_viewport()
start_dearpygui()
destroy_context()