import dearpygui.dearpygui as dpg


def register_font():
    with dpg.font_registry():
        font = dpg.add_font( file='src/fonts/Roboto-Regular.ttf', size=20)
        dpg.bind_font(font)