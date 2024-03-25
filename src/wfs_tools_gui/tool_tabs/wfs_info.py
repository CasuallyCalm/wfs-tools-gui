import subprocess

import dearpygui.dearpygui as dpg

from .. import arguments
from .tool_tab_abc import ToolTabs


class WFSInfo(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-info"
        super().__init__()
        arguments.input_type(self.tab)
        self.run_button()

    def command(self) -> str:
        cmd = super().command()
        return  f"{cmd} --input {arguments.get_input()} --type {arguments.get_type()}"

    def execute(self) -> None:
        process = subprocess.Popen(
            self.command(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        window_name = f"{self.name}_modal"
        label = f"{self.name}:"
        with dpg.window(
            tag=window_name,
            label=label,
            modal=True,
            on_close=lambda: dpg.delete_item(window_name),
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
        ):
            output = dpg.add_input_text(
                multiline=True,
                readonly=True,
                width=dpg.get_item_width(window_name),
                height=dpg.get_item_height(window_name),
            )
            if stderr:
                dpg.set_value(output, bytes.decode(stderr))
            else:
                dpg.set_value(output, bytes.decode(stdout))
