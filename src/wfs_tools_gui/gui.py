import ctypes
import sys

import dearpygui.dearpygui as dpg

from .arguments import Arguments
from .platforms import PLATFORM
from .style import register_font
from .tool_tabs import WFSExtract, WFSFileInjector, WFSFuse, WFSInfo, WFSReencryptor


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run():
    if PLATFORM.name == 'win':
        if is_admin():
            gui()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    elif PLATFORM.name == 'linux':
        gui()

def gui():
    dpg.create_context()
    dpg.create_viewport(title="WFS Tools", width=800, height=600)
    dpg.setup_dearpygui()
    register_font()

    with dpg.window( tag="window"):
        Arguments()
        with dpg.tab_bar(tag="tool_tab_bar"):
            WFSExtract()
            WFSFileInjector()
            if PLATFORM.name == "linux":
                WFSFuse()
            WFSInfo()
            WFSReencryptor()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()



if __name__ == "__main__":
    run()