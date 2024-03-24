import dearpygui.dearpygui as dpg


def seeprom():
    with dpg.file_dialog(
        label="seeprom.bin",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "seeprom_path", app_data["file_path_name"]
        ),
        tag="select_seeprom",
        show=False,
    ) as select_seeprom:
        dpg.add_file_extension(
            ".bin",
            color=(150, 255, 150, 255),
            parent=select_seeprom,
            custom_text="[.bin]",
        )
    with dpg.group(horizontal=True, tag="seeprom_group", show=True):
        dpg.add_button(
            label="Select seeprom file (seeprom.bin)",
            callback=lambda: dpg.show_item(select_seeprom),
        )
        dpg.add_input_text(source="seeprom_path")
