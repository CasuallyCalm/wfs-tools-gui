import dearpygui.dearpygui as dpg


def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(title="WFS Tools",width=600, height=400)
dpg.setup_dearpygui()

with dpg.window(label="main_windows", tag='window'):
    with dpg.menu_bar():
        dpg.add_menu_item(label='help')
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.set_primary_window('window', True)
dpg.start_dearpygui()
dpg.destroy_context()