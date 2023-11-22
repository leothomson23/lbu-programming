#!/usr/bin/env python3
if __name__ == "__main__":
    import shutil
    import sys
    def backup(file):
        backup = file + "_backup"
        shutil.copy(input_file, backup_file)
        print("Backup created at ", backup)

    input = sys.argv[1]
    backup(input)