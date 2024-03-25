__all__ = ("seeprom", "otp", "argument_registry", "input_type", "output", "dump_path")

import dearpygui.dearpygui as dpg

from .dump import dump_path
from .input_type import input_type
from .otp import otp
from .output import output
from .registry import argument_registry
from .seeprom import seeprom


def get_otp():
    return dpg.get_value("--otp")


def get_seeprom():
    return dpg.get_value("--seeprom")


def get_type():
    return dpg.get_value("--type").lower()


def get_input(input_type:str|None=None):
    _type = input_type or get_type()
    return dpg.get_value("--input " + _type)


def get_outupt():
    return dpg.get_value("--output")


def get_dump_path():
    return dpg.get_value("--dump-path")