import subprocess


def wfs_info(path: str, otp: str, seeprom: str, input: str, type: str):
    command = f"{path} --otp {otp} --seeprom {seeprom} --input {input} --type {type}"
    subprocess.Popen(command)


def wfs_extract(
    path: str,
    otp: str,
    seeprom: str,
    input: str,
    type: str,
    output: str,
    dump_path: str,
    verbose: bool,
):
    command = f"{path} --otp {otp} --seeprom {seeprom} --input {input} --type {type} --output {output} --dump-path {dump_path}"
    if verbose:
        command = f"{command} --verbose"
    subprocess.Popen(command)
