import dearpygui.dearpygui as dpg


def dump_path(parent: int | str):
    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_text("Dump Path:")
            dpg.add_input_text(source="--dump-path")
