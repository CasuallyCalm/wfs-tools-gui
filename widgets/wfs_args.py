from .input_field import Input


def otp():
    return Input("OTP:", "Slect OTP File", filter="otp (otp.bin);;bin (*.bin);;All (*)")


def seeprom():
    return Input(
        "Seeprom:",
        "Slect Seeprom File",
        filter="seeprom (seeprom.bin);;bin (*.bin);;All (*)",
    )
