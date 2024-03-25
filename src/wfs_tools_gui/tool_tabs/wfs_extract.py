import dearpygui.dearpygui as dpg

from .. import arguments
from .tool_tab_abc import ToolTabs


class WFSExtract(ToolTabs):
    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()
        arguments.input_type(parent=self.tab)
        arguments.output(parent=self.tab)
        arguments.dump_path(parent=self.tab)
        self.run_button()
    
    def command(self) -> str:
        cmd = super().command()
        _type = dpg.get_value('--type').lower()
        _input = dpg.get_value('--input '+_type)
        output = dpg.get_value('--output')
        dump_path = dpg.get_value('--dump-path')
        return  f"{cmd} --input {_input} --type {_type} --output {output} --dump-path {dump_path} --verbose"

    def execute(self) -> None:
        return super().execute()