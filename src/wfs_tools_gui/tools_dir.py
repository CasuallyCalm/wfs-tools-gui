__all__ = ("tools_dir",)

from pathlib import Path

import dearpygui.dearpygui as dpg

from .platforms import PLATFORM


def tools_dir():
    def load_tool_path(_, app_data):
        [dpg.hide_item(tab) for tab in dpg.get_item_children("tool_tab_bar", 1)]
        path = app_data["file_path_name"]
        dpg.set_value("tools_path", path)
        for item in Path(path).iterdir():
            if item.is_file() and item.name.lower() in PLATFORM.executables:
                name = item.stem
                dpg.show_item(name + "_tab")
                dpg.set_value(name + "_path", item)
        dpg.configure_item("select_otp", default_path=path)
        dpg.configure_item("select_seeprom", default_path=path)

    select_tools = dpg.add_file_dialog(
        label="Tools Directory",
        directory_selector=True,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=load_tool_path,
        show=False,
    )
    with dpg.group(horizontal=True):
        dpg.add_button(
            label="Select wfs-tools directory",
            callback=lambda: dpg.show_item(select_tools),
        )
        dpg.add_input_text(tag="tools_path")
