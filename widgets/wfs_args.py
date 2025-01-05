from .input_field import InputField


def otp():
    return InputField(
        "OTP:", "Slect OTP File", filter="otp (otp.bin);;bin (*.bin);;All (*)"
    )


def seeprom():
    return InputField(
        "Seeprom:",
        "Slect Seeprom File",
        filter="seeprom (seeprom.bin);;bin (*.bin);;All (*)",
    )


def output():
    return InputField(
        "Output",
        "Output Directory",
        file_dialog=False,
    )


def dump_path():
    return InputField(
        "Directory to dump from WFS (default: /)",
        "Directory to dump from WFS (default: /)",
        file_dialog=False,
        show_button=False,
    )
