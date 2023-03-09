import git
from git import Repo
import os
from datetime import datetime
import shutil


def main(current_path):
    datestr = datetime.now().strftime("%Y-%m-%d")

    if os.path.isdir(current_path):
        try:
            # if the current_path repository is not a git repository throws git.exc.InvalidGitRepositoryError
            _ = git.Repo(current_path).git_dir

            repository = Repo(current_path)
            untracked_files = repository.untracked_files

            # It will fetch the modified/changed files from the directory
            modified_files = [item.a_path for item in repository.index.diff(None)]

            if modified_files: print("The modified files are : \n", "\n".join(modified_files))
            if untracked_files: print("\n\nThe untracked files are : \n", "\n".join(untracked_files))
            untracked_modified_files_list = [untracked_files, modified_files]

            untracked_modified_files_path = []

            project_name = ""
            for i in reversed(current_path.split("\\")):
                project_name = i
                break

            for k in ["\\untracked_files", "\\modified_files"]:
                # This is to create and break down the path in list format
                files_folder_list = [os.getcwd() + "\\" + project_name,
                                     "\\" + str(repository.active_branch) + "_" + datestr, k]
                files_folder_name = ""
                for i in files_folder_list:
                    files_folder_name += i

                    if os.path.exists(files_folder_name):
                        continue

                    make_directory(files_folder_name)

                untracked_modified_files_path.append(files_folder_name)

            # I will iterate over two lists simultaneously
            for (a, b) in zip(untracked_modified_files_list, untracked_modified_files_path):
                replicate_untracked_files(a, b, current_path)
                replicate_untracked_files(a, b, current_path)

            print("Files have been copied")
        except git.exc.InvalidGitRepositoryError:
            print("Not a git directory")


        except Exception as e:

            print("Error occurred : ", e)


def make_directory(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass


def replicate_untracked_files(untracked_files, dest_folder_path, current_path):
    for file_name in untracked_files:
        if '/' in file_name:
            new_file_name = ""
            new_curr_path = current_path
            new_dest_path = dest_folder_path
            temp = file_name.split("/")

            for i in temp:
                if os.path.isdir(new_curr_path + "\\" + i):
                    new_curr_path = new_curr_path + "\\" + i
                    new_dest_path = new_dest_path + "\\" + i

                    if os.path.exists(new_dest_path):
                        continue

                    make_directory(new_dest_path)

                else:
                    new_file_name = i

            # Copies the file from source to destination
            shutil.copyfile(new_curr_path + "\\" + new_file_name, new_dest_path + "\\" + new_file_name)

        elif os.path.isfile(current_path + "\\" + file_name):
            shutil.copyfile(current_path + "\\" + file_name, dest_folder_path + "\\" + file_name)


if __name__ == '__main__':
    # Input : Takes path of the git repository.....
    current_path = input("Enter Repository Path : ")
    main(current_path)

# project_name/branch_name+todays_date/modified_files/file structure for changed or modified files
# project_name/branch_name+todays_date/untracked_files/file structure for untracked files

# C:\Users\ajaybhan\Desktop\e-pizza-app
