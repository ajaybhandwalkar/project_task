import os


def check_pep8_standards(path):
    # if os.path.isfile(path):
    #     if str(path).endswith(".py"):
    #         print("\nfile", path)
    #         os.system("pycodestyle "+str(path))

    for path, subdirs, files in os.walk(path):
        for name in files:
            filepath = str(os.path.join(path, name))
            if name.endswith(".py"):
                print("\nfile", filepath)
                os.system("pycodestyle " + filepath)


def main():
    path = ".\\"
    check_pep8_standards(path)


if __name__ == '__main__':
    main()
