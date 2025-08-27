import os
import subprocess
import difflib

hyprland_config_path = "~/.config/hypr/hyprland.conf"
rofi_config_path = "~/.config/rofi/config.rasi"
waybar_config_path= "~/.config/waybar/config.jsonc"
waybar_ui_config_path = "~/.config/waybar/style.css"
hyprpaper_config_path = "~/.config/hypr/hyprpaper.conf"
sddm_config_path = "~/etc/sddm.conf.d/autologin.conf"
sddm_lock_config_path = "~/etc/xdg/kscreenlockerrc"

config_paths = [hyprland_config_path,rofi_config_path,waybar_config_path,waybar_ui_config_path,hyprpaper_config_path,sddm_config_path,sddm_lock_config_path]

process_names = ["waybar","hyprpaper"]

def file_diff(path_1,path_2):
    with open(os.path.expanduser(path_1), 'r') as file1:
        lines1 = file1.readlines()
    with open(path_2, 'r') as file2:
        lines2 = file2.readlines()

    diff = difflib.unified_diff(
        lines1,
        lines2,
        fromfile=path_1,
        tofile=path_2,
        lineterm=''  # Prevents extra newline characters in the output
        )
    
    return len(list(diff)) > 0

# def kill_or_start(process_names,kill):

#     result = subprocess.run("ps -e", shell=True, capture_output=True)
#     print(result)
#     # print(result.stdout)

#     for process_name in process_names:
#         if process_name in result and kill:
#             result = subprocess.run(f"killall {process_name}", shell=True)
#         else:
#             result = subprocess.run(f"{process_name}", shell=True)



if __name__ == "__main__":
    if not os.path.isdir("config_files"):
        os.mkdir("config_files")

    if len(os.listdir("config_files")) < len(config_paths):
        for config_path in config_paths:
            file_name = config_path.split("/")[-1]
            print(f"Copying {file_name} to config folder.")
            result = subprocess.run(f"cp {config_path} config_files/{file_name}", shell=True)
    
    
    # kill_or_start(process_names,True)

    for process_name in process_names:
        result = subprocess.run(f"killall {process_name}", shell=True)

    for config_path in config_paths:
        file_name = config_path.split("/")[-1]
        # if file_diff(config_path, f"config_files/{file_name}"):
        print(f"Overriding {config_path}")
        if "etc" not in config_path:
            result = subprocess.run(f"cp config_files/{file_name} {config_path}", shell=True)
        else:
            result = subprocess.run(f"sudo cp config_files/{file_name} {config_path}", shell=True)
                
    # kill_or_start(process_names, False)
    
    