import shutil
import os
import time
import xml.etree.ElementTree as ET

SETTINGS_PATH = "settings.xml"
OUTPUT_DIR = "output"
COVERAGE_DIR = "Coverage_analysis/v1"
EXPORT_SRC = "Export_v1.py"
EXPORT_DEST = "Export.py"
TIMER_LOG = "time_v1.txt"

def update_template_path():
    tree = ET.parse(SETTINGS_PATH)
    root = tree.getroot()
    for param in root.findall(".//parameter[@name='template_path']"):
        param.set("value", "test_models_V1/")
    tree.write(SETTINGS_PATH)

def overwrite_export():
    shutil.copyfile(EXPORT_SRC, EXPORT_DEST)

def clear_output():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

def update_template_file_name(i):
    tree = ET.parse(SETTINGS_PATH)
    root = tree.getroot()
    for param in root.findall(".//parameter[@name='template_file_name']"):
        param.set("value", f"h{i}.xml")
    tree.write(SETTINGS_PATH)

def run_generator_and_time(i):
    start = time.time()
    os.system("python3 Generate.py")
    end = time.time()
    duration = end - start
    with open(TIMER_LOG, "a") as f:
        f.write(f"Generator time for tree h{i}: {duration:.2f} seconds\n")

def copy_output_to_coverage(i):
    dest_dir = os.path.join(COVERAGE_DIR, f"treeh{i}")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in os.listdir(OUTPUT_DIR):
        s = os.path.join(OUTPUT_DIR, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def main():
    update_template_path()
    overwrite_export()

    for i in range(3, 7):
        clear_output()
        update_template_file_name(i)
        run_generator_and_time(i)
        copy_output_to_coverage(i)

if __name__ == "__main__":
    main()
