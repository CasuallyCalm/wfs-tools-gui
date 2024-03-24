import dearpygui.dearpygui as dpg


def argument_registry():
    with dpg.value_registry():
        dpg.add_string_value(tag='otp_path')
        dpg.add_string_value(tag='seeprom_path')
        dpg.add_string_value(tag='input_type')
        dpg.add_string_value(tag='usb_input')
        dpg.add_string_value(tag='mlc_input')
        dpg.add_string_value(tag='plain_input')
        dpg.add_string_value(tag='output_path')
        dpg.add_string_value(tag='dump_path')
        dpg.add_string_value(tag='image_path')