import dearpygui.dearpygui as dpg

from ..platforms import PLATFORM

INPUTS = dict(usb=[], mlc=[], plain=[])
RADIOS = []


def input_type(parent: int | str):
    drives = PLATFORM.get_drives()

    def refresh_drives():
        dpg.set_value(usb_combo, "")
        drives = PLATFORM.get_drives()
        dpg.configure_item(usb_combo, items=[drive.label for drive in drives])

    def set_input(_, app_data, __):
        for drive in drives:
            if drive == app_data:
                dpg.set_value("--input usb", drive.path)

    def change_input_type(_, input_type: str):
        for radio in RADIOS:
            dpg.set_value(radio, input_type)
        for _type, item_group in INPUTS.items():
            for item in item_group:
                if _type != input_type.lower():
                    dpg.hide_item(item)
                else:
                    dpg.show_item(item)

    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_text("Input Type: ")
            radio = dpg.add_radio_button(
                items=["USB", "MLC", "Plain"],
                horizontal=True,
                callback=change_input_type,
                source="--type",
            )

        with dpg.group(horizontal=True):
            with dpg.group(horizontal=True) as usb:
                dpg.add_button(label="Refresh Drives", callback=refresh_drives)
                usb_combo = dpg.add_combo(
                    # tag=usb_combo,
                    items=[drive.label for drive in drives],
                    callback=set_input,
                    source="usb_label",
                )
                with dpg.value_registry():
                    dpg.add_string_value(default_value="", source="--input usb")

            with dpg.group(horizontal=True, show=False) as mlc:
                dpg.add_button(
                    label="Select MLC image:",
                    callback=lambda: dpg.show_item("mlc_dialog"),
                )
                dpg.add_input_text(source="--input mlc")

            with dpg.group(horizontal=True, show=False) as plain:
                dpg.add_button(
                    label="Select mount path:",
                    callback=lambda: dpg.show_item("plain_dialog"),
                )
                dpg.add_input_text(source="--input plain")

            # Used to sync input state across tabs
            INPUTS["usb"].append(usb)
            INPUTS["mlc"].append(mlc)
            INPUTS["plain"].append(plain)
            RADIOS.append(radio)
