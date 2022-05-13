import os  # library
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--labels_path", required=True, help="Path to labels' directory")
args = parser.parse_args()
char = len("--labels_path")

labels_path = args.labels_path
dir_list = os.listdir(labels_path)

print("-----------------------------------------")
print("Files and directories in '", labels_path, "' :")
print(dir_list)



for file_name in dir_list:
    txt_path = os.path.join(labels_path, file_name)
    print(f"txt_path: {txt_path}")

    with open(txt_path, mode="r") as f:
        first_line = f.read()

    modified_label = first_line.replace('-1', '0', char)
    with open(txt_path, mode="w") as f:
        f.write(modified_label)
print(f"Successfully processed labels in {labels_path} directory")
