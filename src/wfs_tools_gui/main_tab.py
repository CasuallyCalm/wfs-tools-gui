from pathlib import Path

import dearpygui.dearpygui as dpg

from .platforms import get_platform

PLATFORM= get_platform()

class Main:

    def __init__(self) -> None:

        def load_tool_path(sender, app_data, user_data):
            [dpg.hide_item(tab) for tab in dpg.get_item_children('tab_bar',1)[1:]]
            path = app_data['file_path_name']
            dpg.set_value('tools_path', path)
            for item in Path(path).iterdir():
                if item.is_file() and item.name.lower() in PLATFORM.executables:
                    dpg.show_item(item.stem.lower()+"_tab")
            dpg.configure_item(select_otp,default_path=path)
            dpg.configure_item(select_seeprom,default_path=path)


                    

        select_tools = dpg.add_file_dialog(label='Tools Directory',directory_selector=True, modal=True, width=dpg.get_viewport_width()-100,height=dpg.get_viewport_height()-100, callback= load_tool_path, show=False)
        select_otp = dpg.add_file_dialog(label='otp.bin', directory_selector=False, modal=True,width=dpg.get_viewport_width()-100, height=dpg.get_viewport_height()-100, callback=lambda _, app_data: dpg.set_value('otp_path', app_data['file_path_name']), show=False)
        select_seeprom = dpg.add_file_dialog(label='seeprom.bin',directory_selector=False, modal=True, width=dpg.get_viewport_width()-100, height=dpg.get_viewport_height()-100, callback=lambda _, app_data: dpg.set_value('seeprom_path', app_data['file_path_name']), show=False)
        dpg.add_file_extension("*otp.bin", color=(150, 255, 150, 255), parent=select_otp, custom_text='[.bin]')
        dpg.add_file_extension(".bin", color=(150, 255, 150, 255), parent=select_seeprom, custom_text='[.bin]')
        


        with dpg.tab(label='Main', tag='main_tab'):
            with dpg.group( horizontal=True):
                dpg.add_button(label='Select wfs-tools directory', callback=lambda: dpg.show_item(select_tools))
                dpg.add_text(tag='tools_path')
            with dpg.group( horizontal=True):
                dpg.add_button(label='Select otp file (otp.bin)', callback=lambda: dpg.show_item(select_otp))
                dpg.add_text(tag='otp_path')
            with dpg.group( horizontal=True):
                dpg.add_button(label='Select seeprom file (seeprom.bin)', callback=lambda: dpg.show_item(select_seeprom))
                dpg.add_text(tag='seeprom_path')

