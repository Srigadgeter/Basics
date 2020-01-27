# >>>>> Files & Directories <<<<<
from pathlib import Path

##
# Two types of paths
# 1 Absolute Path - path of any file/directory in our hard disk
# 2 Relative Path - path inside project's root folder
##

path1 = Path('email')

if path1.exists():
    path1.rmdir()
else:
    path1.mkdir()

path2 = Path()  # Without any arguments which represents the Current Project's Root Directory
files = path2.glob('*.py')  # searching files endswith '.py' extension inside the root directory

for file in files:
    print(file)

print('*' * 10)

files2 = path2.glob('*')  # searching all files & folders inside the root directory

for file in files2:
    print(file)
# =========================================
