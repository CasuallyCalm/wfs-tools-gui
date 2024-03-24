import dearpygui.dearpygui as dpg


def otp():
    with dpg.file_dialog(
        label="otp.bin",
        directory_selector=False,
        modal=True,
        width=dpg.get_viewport_width() - 100,
        height=dpg.get_viewport_height() - 100,
        callback=lambda _, app_data: dpg.set_value(
            "otp_path", app_data["file_path_name"]
        ),
        tag="select_otp",
        show=False,
    ) as select_otp:
        dpg.add_file_extension(".bin", color=(150, 255, 150, 255), custom_text="[.bin]")

    with dpg.group(horizontal=True, tag="otp_group", show=True):
        dpg.add_button(
            label="Select otp file (otp.bin)",
            callback=lambda: dpg.show_item(select_otp),
        )
        dpg.add_input_text(source="otp_path")
