from pathlib import Path

import dearpygui.dearpygui as dpg

from .platforms import PLATFORM


class Arguments:
    def __init__(self) -> None:
        self.__drives = PLATFORM.get_drives()

        def load_tool_path(_, app_data):
            [dpg.hide_item(tab) for tab in dpg.get_item_children("tool_tab_bar", 1)]
            path = app_data["file_path_name"]
            dpg.set_value("tools_path", path)
            for item in Path(path).iterdir():
                if item.is_file() and item.name.lower() in PLATFORM.executables:
                    name = item.stem
                    dpg.show_item(name + "_tab")
                    dpg.set_value(name + "_path", item)
            dpg.configure_item(select_otp, default_path=path)
            dpg.configure_item(select_seeprom, default_path=path)

        def change_input_type(_, input_type: str):
            for item in ["usb", "mlc", "plain"]:
                group = item + "_group"
                if item != input_type.lower():
                    dpg.hide_item(group)
                else:
                    dpg.show_item(group)

        select_tools = dpg.add_file_dialog(
            label="Tools Directory",
            directory_selector=True,
            modal=True,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            callback=load_tool_path,
            show=False,
        )
        select_otp = dpg.add_file_dialog(
            label="otp.bin",
            directory_selector=False,
            modal=True,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            callback=lambda _, app_data: dpg.set_value(
                "otp_path", app_data["file_path_name"]
            ),
            show=False,
        )
        select_seeprom = dpg.add_file_dialog(
            label="seeprom.bin",
            directory_selector=False,
            modal=True,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            callback=lambda _, app_data: dpg.set_value(
                "seeprom_path", app_data["file_path_name"]
            ),
            show=False,
        )
        select_mlc = dpg.add_file_dialog(
            label="MLC image",
            directory_selector=False,
            modal=True,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            callback=lambda _, app_data: dpg.set_value(
                "mlc_input", app_data["file_path_name"]
            ),
            show=False,
        )

        select_plain = dpg.add_file_dialog(
            label="Mount Path",
            directory_selector=True,
            modal=True,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            callback=lambda _, app_data: dpg.set_value(
                "plain_input", app_data["file_path_name"]
            ),
            show=False,
        )

        dpg.add_file_extension(
            ".bin", color=(150, 255, 150, 255), parent=select_otp, custom_text="[.bin]"
        )

        dpg.add_file_extension(
            ".bin",
            color=(150, 255, 150, 255),
            parent=select_seeprom,
            custom_text="[.bin]",
        )

        dpg.add_file_extension(
            ".img",
            color=(150, 255, 150, 255),
            parent=select_mlc,
            custom_text="[image]",
        )

        with dpg.group():
            with dpg.group(horizontal=True):
                dpg.add_text("Input Type: ")
                dpg.add_radio_button(
                    tag="input_type",
                    items=["USB", "MLC", "Plain"],
                    horizontal=True,
                    default_value="USB",
                    callback=change_input_type,
                )

            with dpg.group(horizontal=True):
                with dpg.group(horizontal=True, tag="usb_group"):
                    dpg.add_button(
                        label="Refresh Drives", callback=self.__refresh_drives
                    )
                    dpg.add_combo(
                        tag="usb_combo",
                        items=[drive.label for drive in self.__drives],
                        callback=self.__set_input,
                    )
                    with dpg.value_registry():
                        dpg.add_string_value(default_value="", tag='usb_input')

                with dpg.group(horizontal=True, tag="mlc_group", show=False):
                    dpg.add_button(
                        label="Select MLC image:",
                        callback=lambda: dpg.show_item(select_mlc),
                    )
                    dpg.add_input_text(tag="mlc_input")

                with dpg.group(horizontal=True, tag="plain_group", show=False):
                    dpg.add_button(
                        label="Select mount path:",
                        callback=lambda: dpg.show_item(select_plain),
                    )
                    dpg.add_input_text(tag="plain_input")

            with dpg.group(horizontal=True):
                dpg.add_button(
                    label="Select wfs-tools directory",
                    callback=lambda: dpg.show_item(select_tools),
                )
                dpg.add_input_text(tag="tools_path")

            with dpg.group(horizontal=True, tag="otp_group", show=True):
                dpg.add_button(
                    label="Select otp file (otp.bin)",
                    callback=lambda: dpg.show_item(select_otp),
                )
                dpg.add_input_text(tag="otp_path")

            with dpg.group(horizontal=True, tag="seeprom_group", show=True):
                dpg.add_button(
                    label="Select seeprom file (seeprom.bin)",
                    callback=lambda: dpg.show_item(select_seeprom),
                )
                dpg.add_input_text(tag="seeprom_path")

        dpg.add_spacer(height=10)

    def __refresh_drives(self):
        dpg.set_value("usb_combo", "")
        self.__drives = PLATFORM.get_drives()
        dpg.configure_item("usb_combo", items=[drive.label for drive in self.__drives])

    def __set_input(self, sender, app_data, user_data):
        for drive in self.__drives:
            if drive == app_data:
                dpg.set_value('usb_input', drive.path)
                self.input = drive.path
        
