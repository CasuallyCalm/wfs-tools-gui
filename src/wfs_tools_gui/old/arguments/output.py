import dearpygui.dearpygui as dpg


def output(parent: int | str):
    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_button(
                label="Output Path",
                callback=lambda: dpg.show_item("output_dialog"),
            )
            dpg.add_input_text(source="--output")
