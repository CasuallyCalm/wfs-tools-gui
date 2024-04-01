import subprocess
import threading
import time

import dearpygui.dearpygui as dpg

from .. import arguments
from .tool_tab_abc import ToolTabs


class WFSExtract(ToolTabs):
    run_task = True
    thread = None

    def __init__(self) -> None:
        self.name = "wfs-extract"
        super().__init__()
        arguments.input_type(parent=self.tab)
        arguments.output(parent=self.tab)
        arguments.dump_path(parent=self.tab)
        self.run_button()

    def command(self) -> str:
        cmd = super().command()
        return f"{cmd} --input {arguments.get_input()} --type {arguments.get_type()} --output {arguments.get_outupt()} --dump-path {arguments.get_dump_path()} --verbose"

    def start_thread(self, logger: str):
        process = subprocess.Popen(
            self.command(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
        )
        for line in process.stdout:
            if self.run_task:
                dpg.set_value(logger, dpg.get_value(logger) + line)
                dpg.set_y_scroll("logger_window", -1.0)
            else:
                process.terminate()
        for line in process.stderr:
            if self.run_task:
                dpg.set_value(logger, dpg.get_value(logger) + line)
                dpg.set_y_scroll("logger_window", -1.0)
            else:
                process.terminate()
        print("cancelled")

    def cancel_task(self, sender, app_data, logger):
        self.run_task = False
        while self.thread.is_alive():
            time.sleep(0.001)
        dpg.set_value(logger, dpg.get_value(logger) + "Cancelled!")
        # dpg.add_text("Extract Cancelled!", parent=logger)
        dpg.configure_item(sender, enabled=False)

    def close_window(self, sender):
        self.run_task = False
        dpg.delete_item(sender)
        self.run_task = True

    def execute(self) -> None:
        with dpg.window(
            label=self.name,
            modal=True,
            on_close=self.close_window,
            width=dpg.get_viewport_width() - 100,
            height=dpg.get_viewport_height() - 100,
            tag="modal_window",
        ) as window:
            dpg.add_button(
                label="Cancel", callback=self.cancel_task, user_data="logger"
            )

            with dpg.child_window(
                autosize_x=True, autosize_y=True, tag="logger_window"
            ) as logger_window:
                logger = dpg.add_input_text(
                    height=-1,
                    width=-1,
                    readonly=True,
                    multiline=True,
                    tracked=True,
                    track_offset=1.0,
                    tag="logger",
                )
                self.thread = threading.Thread(
                    target=self.start_thread, args=(logger,), daemon=True
                )
                self.thread.start()
