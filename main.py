import time
import os
import shutil

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime



def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = input("Enter path: ")
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)
    
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleted_folders_count += 1
                break
            else:
                for folders in folders:
                    next_folder_path = os.path.join(root_folder, folders)

                    if seconds >= get_file_or_folder_age(next_folder_path):
                        remove_folder(next_folder_path)
                        deleted_folders_count += 1
                    
                for files in files:
                    next_file_path = os.path.join(root_folder, files)

                    if seconds >= get_file_or_folder_age(next_file_path):
                        remove_file(next_file_path)
                        deleted_files_count += 1
                    else:
                        if seconds >= get_file_or_folder_age(path):
                            remove_file(path)
                            deleted_files_count += 1
    else:
        print("path not found")
    
    print(str(deleted_files_count) + " is the number of files deleted")
    print(str(deleted_folders_count) + " is the number of folders deleted")
    



if __name__ == '__main__':
	main()

