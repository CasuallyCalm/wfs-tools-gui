from pathlib import Path

import dearpygui.dearpygui as dpg

from .platforms import PLATFORM


def load_tool_path(_, app_data):
    for tab in dpg.get_item_children("tool_tab_bar", 1):
        dpg.hide_item(tab)
    path = app_data["file_path_name"]
    dpg.set_value("tools_path", path)
    for item in Path(path).iterdir():
        if item.is_file() and item.name.lower() in PLATFORM.executables:
            name = item.stem
            dpg.show_item(name + "_tab")
            dpg.set_value(name + "_path", item)
    dpg.configure_item("otp_dialog", default_path=path)
    dpg.configure_item("seeprom_dialog", default_path=path)
    dpg.configure_item("plain_dialog", default_path=path)
    dpg.configure_item("mlc_dialog", default_path=path)
    dpg.configure_item("output_dialog", default_path=path)
    dpg.configure_item("inject-file_dialog", default_path=path)


def load_file_dialogs():
    dpg.add_file_dialog(
        label="Tools Directory",
        directory_selector=True,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=load_tool_path,
        tag="tools_dialog",
        show=False,
    )

    with dpg.file_dialog(
        label="MLC image",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--input mlc", app_data["file_path_name"]
        ),
        tag="mlc_dialog",
        show=False,
    ):
        dpg.add_file_extension(
            ".img",
            color=(150, 255, 150, 255),
            custom_text="[image]",
        )

    dpg.add_file_dialog(
        label="Mount Path",
        directory_selector=True,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--input plain", app_data["file_path_name"]
        ),
        tag="plain_dialog",
        show=False,
    )

    with dpg.file_dialog(
        label="seeprom.bin",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--seeprom", app_data["file_path_name"]
        ),
        tag="seeprom_dialog",
        show=False,
    ):
        dpg.add_file_extension(".bin", color=(150, 255, 150, 255), custom_text="[.bin]")

    with dpg.file_dialog(
        label="otp.bin",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--otp", app_data["file_path_name"]
        ),
        tag="otp_dialog",
        show=False,
    ):
        dpg.add_file_extension(".bin", color=(150, 255, 150, 255), custom_text="[.bin]")

    dpg.add_file_dialog(
        label="Output Directory",
        directory_selector=True,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--output", app_data["file_path_name"]
        ),
        tag="output_dialog",
        show=False,
    )

    with dpg.file_dialog(
        label="Inject File",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "--inject-file", app_data["file_path_name"]
        ),
        tag="inject-file_dialog",
        show=False,
    ):
        dpg.add_file_extension(
            ".zip",
            color=(150, 255, 150, 255),
            custom_text="[zip]",
        )