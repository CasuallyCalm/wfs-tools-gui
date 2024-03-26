import dearpygui.dearpygui as dpg


def inject_file(parent:int|str):
    with dpg.group(horizontal=True, parent=parent):
        dpg.add_button(
            label="Select file to inject",
            callback=lambda: dpg.show_item("inject-file_dialog"),
        )
        dpg.add_input_text(source="--inject-file")
