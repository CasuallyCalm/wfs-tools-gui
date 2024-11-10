import subprocess


def wfs_info(path:str, otp:str, seeprom:str, input:str, type:str):
        command = f"{path} --otp {otp} --seeprom {seeprom} --input {input} --type {type}"
        subprocess.Popen(
            command #, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )