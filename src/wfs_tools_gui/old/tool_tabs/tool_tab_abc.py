from abc import ABC

import dearpygui.dearpygui as dpg

from .. import arguments


class ToolTabs(ABC):
    name: str

    def __init__(self) -> None:
        self.tab = dpg.add_tab(label=self.name, tag=self.tag, show=False)
        with dpg.value_registry():
            self.executable_path = dpg.add_string_value(
                tag=f"{self.name}_path"
            )

    def run_button(self):
        return dpg.add_button(label="RUN", callback=self.execute, height=30, width=dpg.get_viewport_width(), parent=self.tab)

    @property
    def tag(self):
        return self.name + "_tab"

    def command(self) -> str:
        exec = dpg.get_value(self.executable_path)
        return f"{exec} --otp {arguments.get_otp()} --seeprom {arguments.get_seeprom()}"

    def execute(self) -> None:
        print(self.command())
