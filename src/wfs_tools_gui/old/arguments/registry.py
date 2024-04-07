import dearpygui.dearpygui as dpg


def argument_registry():
    with dpg.value_registry():
        dpg.add_string_value(tag="--otp")
        dpg.add_string_value(tag="--seeprom")
        dpg.add_string_value(tag="--type", default_value="USB")
        dpg.add_string_value(tag="--image")
        dpg.add_string_value(tag="--inject-file")
        dpg.add_string_value(tag="--inject-path")
        dpg.add_string_value(tag="--input usb")
        dpg.add_string_value(tag="--input mlc")
        dpg.add_string_value(tag="--input plain")
        dpg.add_string_value(tag="--output")
        dpg.add_string_value(tag="--dump-path", default_value="/")
        dpg.add_string_value(tag="usb_label")
