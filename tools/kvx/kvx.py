#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess
import toml

def cmd_init():
    args = sys.argv[2:]
    # Template dizinini sabit mutlak yol olarak tanımla
    template_dir = "/home/anilerden/KuvixOS-SDK-V3/templates/terminal-app/"

    # Varsayılan: bulunduğun klasöre çıkar
    target_dir = os.getcwd()

    # Eğer -d parametresi verilmişse yeni klasör oluştur
    if len(args) >= 2 and args[0] == "-d":
        project_name = args[1]
        target_dir = os.path.join(os.getcwd(), project_name)
        os.makedirs(target_dir, exist_ok=True)

    # Template dosyalarını kopyala
    for item in os.listdir(template_dir):
        s = os.path.join(template_dir, item)
        d = os.path.join(target_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print(f"Project initialized in {target_dir}")

def cmd_build():
    args = sys.argv[2:]
    if len(args) >= 1:
        project_dir = os.path.abspath(args[0])
    else:
        project_dir = os.getcwd()

    build_dir = os.path.join(project_dir, "build")
    os.makedirs(build_dir, exist_ok=True)

    toml_file = os.path.join(project_dir, "kvx.toml")
    if not os.path.exists(toml_file):
        print("Error: kvx.toml not found in", project_dir)
        return

    config = toml.load(toml_file)
    project_name = config.get("project", {}).get("name", "demo")
    output_file = os.path.join(build_dir, f"{project_name}.kef")

    ld_file = os.path.join(os.path.dirname(__file__), "kvx.ld")

    # Burada SDK src yolunu sabit veriyoruz
    sdk_src = "/home/anilerden/KuvixOS-SDK-V3/src/kuvixos.cpp"
    sdk_include = "/home/anilerden/KuvixOS-SDK-V3/include"

    cmd = [
        "g++",
        os.path.join(project_dir, "main.cpp"),
        "/home/anilerden/KuvixOS-SDK-V3/src/kuvixos.cpp",
        "-I", "/home/anilerden/KuvixOS-SDK-V3/include",
        "-o", output_file,
        "-T", ld_file
    ]

    try:
        subprocess.check_call(cmd)
        print(f"Build successful: {output_file}")
    except subprocess.CalledProcessError:
        print("Build failed.")

def main():
    if len(sys.argv) < 2:
        print("Usage: kvx <command>")
        return

    command = sys.argv[1]
    if command == "init":
        cmd_init()
    elif command == "build":
        cmd_build()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
