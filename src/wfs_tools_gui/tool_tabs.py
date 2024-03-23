import subprocess
from abc import ABC

import dearpygui.dearpygui as dpg


class ToolTabs(ABC):
    name: str

    def __init__(self) -> None:
        with dpg.tab(label=self.name, tag=self.tag, show=False):
            with dpg.value_registry():
                self.path_value = dpg.add_string_value(default_value="unset", tag=f"{self.name}_path")
            dpg.add_button(label="RUN", callback=self.execute, height=30, width= 100)

    @property
    def tag(self):
        return self.name + "_tab"

    @property
    def command(self) -> str:
        _path = dpg.get_value(self.path_value)
        _input_type = dpg.get_value('input_type').lower() 
        _input = dpg.get_value(f'{_input_type}_input') 
        _seeprom = dpg.get_value('seeprom_path') 
        _otp = dpg.get_value('otp_path')  
        return f"{_path} --input {_input} --type {_input_type} --otp {_otp} --seeprom {_seeprom}"

    def execute(self) -> None:
        print(self.command)

class WFSExtract(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()


class WFSFileInjector(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-file-injector"
        super().__init__()


class WFSFuse(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-fuse"
        super().__init__()


class WFSInfo(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-info"
        super().__init__()

    def execute(self) -> None:
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate() 
        window_name = f"{self.name}_modal"
        label =f"{self.name}:"
        with dpg.window(tag=window_name,label=label,modal=True, on_close=lambda: dpg.delete_item(window_name), width=dpg.get_viewport_width()-100, height=dpg.get_viewport_height()-100):
            output = dpg.add_input_text(multiline=True, readonly=True, width=dpg.get_item_width(window_name), height=dpg.get_item_height(window_name)) 
            if stderr:
                dpg.set_value(output, bytes.decode(stderr))
            else:
                dpg.set_value(output, bytes.decode(stdout))

class WFSReencryptor(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-reencryptor"
        super().__init__()
