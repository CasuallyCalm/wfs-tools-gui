import dearpygui.dearpygui as dpg


def otp():
    with dpg.group(horizontal=True, tag="otp_group", show=True):
        dpg.add_button(
            label="Select otp file (otp.bin)",
            callback=lambda: dpg.show_item("otp_dialog"),
        )
        dpg.add_input_text(source="--otp")
