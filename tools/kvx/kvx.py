#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess

def cmd_init():
    # Template klasörünü proje dizinine kopyala
    template_dir = os.path.join(os.path.dirname(__file__), "../../templates/terminal-app")
    project_dir = os.getcwd()
    for item in os.listdir(template_dir):
        s = os.path.join(template_dir, item)
        d = os.path.join(project_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("Project initialized with terminal-app template.")

def cmd_build():
    # main.cpp ve src/kuvixos.cpp dosyalarını derle
    project_dir = os.getcwd()
    build_dir = os.path.join(project_dir, "build")
    os.makedirs(build_dir, exist_ok=True)

    output_file = os.path.join(build_dir, "demo.kef")
    cmd = ["g++", "main.cpp", "src/kuvixos.cpp", "-o", output_file]
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
