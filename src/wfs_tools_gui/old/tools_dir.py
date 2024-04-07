__all__ = ("tools_dir",)


import dearpygui.dearpygui as dpg


def tools_dir():
    with dpg.group(horizontal=True):
        dpg.add_button(
            label="Select wfs-tools directory",
            callback=lambda: dpg.show_item("tools_dialog"),
        )
        dpg.add_input_text(tag="tools_path")
