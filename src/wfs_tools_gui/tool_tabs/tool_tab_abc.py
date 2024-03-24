from abc import ABC

import dearpygui.dearpygui as dpg


class ToolTabs(ABC):
    name: str

    def __init__(self) -> None:
        self.tab = dpg.add_tab(label=self.name, tag=self.tag, show=False)
        with dpg.value_registry():
            self.path_value = dpg.add_string_value(
                tag=f"{self.name}_path"
            )

    def run_button(self):
        return dpg.add_button(label="RUN", callback=self.execute, height=30, width=dpg.get_viewport_width(), parent=self.tab)

    @property
    def tag(self):
        return self.name + "_tab"

    @property
    def command(self) -> str:
        _path = dpg.get_value(self.path_value)
        _seeprom = dpg.get_value("seeprom_path")
        _otp = dpg.get_value("otp_path")
        return f"{_path} --otp {_otp} --seeprom {_seeprom}"

    def execute(self) -> None:
        print(self.command)
