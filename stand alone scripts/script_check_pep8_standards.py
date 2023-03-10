import os
from datetime import datetime

LOG_FILE = "pep8_log.log"


def add_log(filepath):
    with open(LOG_FILE, "a") as fp:
        fp.write("\nfile" + filepath + "\n")
    os.system("pycodestyle " + filepath + " >> " + LOG_FILE)


def check_pep8_standards(path):
    if os.path.isfile(path):
        filepath = str(path)
        if filepath.endswith(".py"):
            add_log(filepath)

    for path, subdirs, files in os.walk(path):
        for name in files:
            filepath = str(os.path.join(path, name))
            if name.endswith(".py"):
                add_log(filepath)


def clear_previous_logs():
    open(LOG_FILE, "w").close()


def print_logs():
    print(f"Printing logs from {LOG_FILE}")
    with open(LOG_FILE, "r") as fp:
        print(fp.read())


def add_new_logs_entry_time():
    now = datetime.now()
    with open("pep8_log.log", "a") as fp:
        fp.write(f"\n\t------------LOG ENTRY : {now.strftime('%B %d,%Y  %I:%M:%S %p')}------------\n")


def main():
    # To get input from user
    # path = input("Enter path : ")

    dir_path = ".\\"
    # file_path = ".\\script_string_letter_count.py"

    # If you want to clear previous logs
    # clear_previous_logs()

    add_new_logs_entry_time()
    check_pep8_standards(dir_path)
    print_logs()


if __name__ == '__main__':
    main()
