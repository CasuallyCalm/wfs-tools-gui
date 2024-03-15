import dearpygui.dearpygui as dpg


def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(title="WFS Tools",width=600, height=400)
dpg.setup_dearpygui()

with dpg.window(label="main_windows", tag='window'):
    with dpg.menu_bar():
        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Set Tools Path..", tag='tools_dir')
            with dpg.tooltip("tools_dir"):
                dpg.add_text("The directory containing the wfs tools executables")
            dpg.add_menu_item(label="wfs-extract")
            dpg.add_menu_item(label="wfs-file-injector")
            dpg.add_menu_item(label="wfs-fuse")
            dpg.add_menu_item(label="wfs-info")
            dpg.add_menu_item(label="wfs-reencryptor")
        
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")



dpg.show_viewport()
dpg.set_primary_window('window', True)
dpg.start_dearpygui()
dpg.destroy_context()