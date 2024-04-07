import dearpygui.dearpygui as dpg


def inject_path(parent: int | str):
    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_text("Inject Path:")
            dpg.add_input_text(source="--inject-path")
