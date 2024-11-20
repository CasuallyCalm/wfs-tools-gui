from typing import List

from gooey import Gooey, GooeyParser, options

import wfs_tools
from tools import get_platform


def add_common_args(parser: GooeyParser, drives: List[str]):
    parser.add_argument(
        "otp",
        metavar="otp.bin",
        help="OTP file",
        widget="FileChooser",
        gooey_options=options.FileChooser(wildcard="otp.bin|otp.bin|bin files|*.bin"),
    )
    parser.add_argument(
        "seeprom",
        metavar="seeprom.bin",
        help="Seeprom file",
        widget="FileChooser",
        gooey_options=options.FileChooser(
            wildcard="seeprom.bin|seeprom.bin|bin files|*.bin"
        ),
    )
    input_type = parser.add_argument_group("Input Type")
    input_type_args = input_type.add_mutually_exclusive_group(
        gooey_options=options.MutexGroup(initial_selection=0)
    )
    input_type_args.add_argument(
        "--usb", metavar="USB", help="help", widget="Dropdown", choices=drives
    )
    input_type_args.add_argument(
        "--mlc",
        metavar="MLC",
        widget="FileChooser",
        gooey_options=options.FileChooser(wildcard="mlc.bin|mlc.bin|bin files|*.bin"),
    )
    input_type_args.add_argument(
        "--plain", metavar="Plain", help="help", widget="Dropdown", choices=drives
    )
    # input_type_args.add_argument("--plain", metavar="Plain", widget="DirChooser")


def add_wfs_info(parser: GooeyParser, drives: List[str]):
    # WFS Info
    tool: GooeyParser = parser.add_parser("wfs-info", help="WFS Info")
    tool.add_argument(
        "path",
        metavar="WFS Info",
        help="wfs-info file",
        widget="FileChooser",
        gooey_options=options.FileChooser(wildcard="wfs-info|wfs-info*|All files|*.*"),
    )
    add_common_args(tool, drives)


def add_wfs_extract(parser: GooeyParser, drives: List[str]):
    # WFS Extract
    tool: GooeyParser = parser.add_parser("wfs-extract", help="WFS Extract")
    tool.add_argument(
        "path", metavar="WFS Extract", help="wfs-extract file", widget="FileChooser"
    )

    add_common_args(tool, drives)

    tool.add_argument(
        "dump_path",
        metavar="Dump Path",
        help="The path to dump from the input. Defult is '/'.",
        default="/",
    )
    tool.add_argument(
        "--verbose", metavar="Verbose", action="store_false", default=True
    )


@Gooey(
    program_name="WFS Tools GUI",
    program_description="A GUI for using WFS Tools",
    required_cols=1,
    navigation="TABBED",
)
def main():
    drives: dict[str, str] = get_platform().get_drives()
    parser = GooeyParser()
    tools = parser.add_subparsers(help="commands", dest="command")
    add_wfs_info(tools, drives.keys())
    add_wfs_extract(tools, drives.keys())

    args = parser.parse_args()
    if args.usb:
        input_type = "usb"
        input_value = drives[args.usb]
    if args.mlc:
        input_type = "mlc"
        input_value = args.mlc
    if args.plain:
        input_type = "plain"
        input_value = args.plain

    if hasattr(args, "verbose"):
        # Gooey inverts the value of checkboxes
        args.verbose = not args.verbose

    # print(args, input_value)

    if args.command == "wfs-info":
        wfs_tools.wfs_info(args.path, args.otp, args.seeprom, input_value, input_type)
    if args.command == "wfs-extract":
        wfs_tools.wfs_extract(
            args.path,
            args.otp,
            args.seeprom,
            input_value,
            input_type,
            args.output,
            args.dump_path,
            args.verbose,
        )


if __name__ == "__main__":
    main()
