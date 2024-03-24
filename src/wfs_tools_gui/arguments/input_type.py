import dearpygui.dearpygui as dpg

from ..platforms import PLATFORM


def input_type(parent:int|str):
    __drives = PLATFORM.get_drives()
    _id = dpg.add_text("input", show=False, parent=parent)

    def uid(end: str):
        return str(_id) + end

    usb_combo = uid("usb_combo")
    usb_group = uid("usb_group")
    mlc_group = uid("mlc_group")
    plain_group = uid("plain_group")

    def __refresh_drives():
        dpg.set_value(usb_combo, "")
        __drives = PLATFORM.get_drives()
        dpg.configure_item(usb_combo, items=[drive.label for drive in __drives])

    def __set_input(sender, app_data, user_data):
        for drive in __drives:
            if drive == app_data:
                dpg.set_value("usb_input", drive.path)

    def change_input_type(_, input_type: str):
        for item in ["usb", "mlc", "plain"]:
            group = uid(item + "_group") 
            if item != input_type.lower():
                dpg.hide_item(group)
            else:
                dpg.show_item(group)

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
        ".img",
        color=(150, 255, 150, 255),
        parent=select_mlc,
        custom_text="[image]",
    )

    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_text("Input Type: ")
            dpg.add_radio_button(
                source="input_type",
                items=["USB", "MLC", "Plain"],
                horizontal=True,
                default_value="USB",
                callback=change_input_type,
            )

        with dpg.group(horizontal=True):
            with dpg.group(horizontal=True, tag=usb_group):
                dpg.add_button(label="Refresh Drives", callback=__refresh_drives)
                dpg.add_combo(
                    tag=usb_combo,
                    items=[drive.label for drive in __drives],
                    callback=__set_input,
                )
                with dpg.value_registry():
                    dpg.add_string_value(default_value="", source="usb_input")

            with dpg.group(horizontal=True, tag=mlc_group, show=False):
                dpg.add_button(
                    label="Select MLC image:",
                    callback=lambda: dpg.show_item(select_mlc),
                )
                dpg.add_input_text(source="mlc_input")

            with dpg.group(horizontal=True, tag=plain_group, show=False):
                dpg.add_button(
                    label="Select mount path:",
                    callback=lambda: dpg.show_item(select_plain),
                )
                dpg.add_input_text(source="plain_input")
