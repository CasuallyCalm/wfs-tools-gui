import dearpygui.dearpygui as dpg


def seeprom():
    with dpg.group(horizontal=True, tag="seeprom_group", show=True):
        dpg.add_button(
            label="Select seeprom file (seeprom.bin)",
            callback=lambda: dpg.show_item('seeprom_dialog'),
        )
        dpg.add_input_text(source="--seeprom")
