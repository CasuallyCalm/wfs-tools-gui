import dearpygui.dearpygui as dpg

from ..platforms import PLATFORM


def input_type(parent: int | str):
    drives = PLATFORM.get_drives()
    _id = dpg.add_text("input", show=False, parent=parent)

    def uid(end: str):
        return str(_id) + end

    usb_combo = uid("usb_combo")
    usb_group = uid("usb_group")
    mlc_group = uid("mlc_group")
    plain_group = uid("plain_group")

    def refresh_drives():
        dpg.set_value(usb_combo, "")
        __drives = PLATFORM.get_drives()
        dpg.configure_item(usb_combo, items=[drive.label for drive in __drives])

    def set_input(sender, app_data, user_data):
        for drive in drives:
            if drive == app_data:
                dpg.set_value("--input usb", drive.path)

    def change_input_type(_, input_type: str):
        for item in ["usb", "mlc", "plain"]:
            group = uid(item + "_group")
            if item != input_type.lower():
                dpg.hide_item(group)
            else:
                dpg.show_item(group)

    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_text("Input Type: ")
            dpg.add_radio_button(
                items=["USB", "MLC", "Plain"],
                horizontal=True,
                callback=change_input_type,
                source="--type",
            )

        with dpg.group(horizontal=True):
            with dpg.group(horizontal=True, tag=usb_group):
                dpg.add_button(label="Refresh Drives", callback=refresh_drives)
                dpg.add_combo(
                    tag=usb_combo,
                    items=[drive.label for drive in drives],
                    callback=set_input,
                    source="usb_label",
                )
                with dpg.value_registry():
                    dpg.add_string_value(default_value="", source="--input usb")

            with dpg.group(horizontal=True, tag=mlc_group, show=False):
                dpg.add_button(
                    label="Select MLC image:",
                    callback=lambda: dpg.show_item("mlc_dialog"),
                )
                dpg.add_input_text(source="--input mlc")

            with dpg.group(horizontal=True, tag=plain_group, show=False):
                dpg.add_button(
                    label="Select mount path:",
                    callback=lambda: dpg.show_item("plain_dialog"),
                )
                dpg.add_input_text(source="--input plain")
