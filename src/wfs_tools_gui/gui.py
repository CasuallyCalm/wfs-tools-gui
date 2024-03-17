import dearpygui.dearpygui as dpg

from .main_tab import Main
from .style import register_font
from .tool_tabs import WFSExtract, WFSFileInjector, WFSFuse, WFSInfo, WFSReencryptor


def run():
    dpg.create_context()
    dpg.create_viewport(title="WFS Tools",width=800, height=600)
    dpg.setup_dearpygui()
    register_font()

    with dpg.window(label="main_windows", tag='window'):
        Main()
        with dpg.tab_bar(tag='tool_tab_bar'):
            WFSExtract()
            WFSFileInjector()
            WFSFuse()
            WFSInfo()
            WFSReencryptor()
    dpg.show_viewport()
    dpg.set_primary_window('window', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    run()