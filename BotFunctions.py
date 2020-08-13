import os
import subprocess
import glob
import re
import functools
import operator
from pathlib import Path
from collections import defaultdict


class BotCommands:
    def __init__(self):
        self._graph = defaultdict(list)

    def commandControl(self, cmd):
        cmd = str(cmd)
        output = subprocess.check_output(cmd, shell=True)
        print(str(output))

    def _reverseDel(self, arr, dir):
        try:
            if arr[len(arr)-1] != dir:
                del(arr[len(arr)-1])
                return self._reverseDel(arr, dir)
            return arr
        except:
            print("Unable to find directory")

    def _viewFiles(self, listFiles):
        for file in listFiles:
            print(file)

    def _manipFiles(self, path,):
        files = glob.glob(path + "/*")
        newFiles = []
        for pt in files:
            r1 = re.findall(r"\\[\w+\.*\s*\-*\_*|\d+\.*\-*\_*\s*]+", pt)
            newFiles.append(r1)
        # Used to join nested list into one list [note]: good time-complexity
        fileManip = functools.reduce(operator.iconcat, newFiles, [])
        return fileManip

    # def search_file(self, directory=None, file=None):
    #     assert os.path.isdir(directory)
    #     for cur_path, directories, files in os.walk(directory):
    #         if file in files:
    #             return os.path.join(directory, cur_path, file)
    #     return None

    def search_file(self, directory=None, file=None):
        assert os.path.isdir(directory)
        current_path, directories, files = os.walk(directory)
        if file in files:
            return os.path.join(directory, file)
        elif directories == '':
            return None
        else:
            for new_directory in directories:
                result = self.search_file(directory=os.path.join(
                    directory, new_directory), file=file)
                if result:
                    return result
            return None

    def _fileFind(self, fname, srch_path):
        if fname in os.listdir(srch_path):
            return srch_path + fname

        print(srch_path)
        f = os.chdir(srch_path)

        print("Current directory files:", os.listdir(f), "\n\n")
        # curr_dir = os.getcwd()
        # stringifyPath = str(curr_dir)
        # # splits list by "//" character
        # splitPath = stringifyPath.split("\\")
        # # returns the directory path argument
        # arry_result = self._reverseDel(splitPath, srch_path)
        delimiter = '/'
        # # joins path using '/' to create the path
        arry_result = os.listdir(f)
        print(arry_result)
        trackPath = []
        trackPath.append(srch_path)
        for f in arry_result:
            if f[0] != '$':
                if os.path.isdir(f):

                    os.chdir()
        path = delimiter.join(arry_result)
        print(path)
        # assert os.path.isdir(path)

        # print(path)
        # os.chdir(path)
        # # checks if argument fname is in the directory of the argument path
        # checkFile = "true" if fname in os.listdir() else "false"
        # print(checkFile)
        # # formats file paths to "C:/file/file"
        # files = self._manipFiles(path)
        # # if "a"
        # print("\n")
        # print("files variable", files)

        # print("\n")
        # x = path + '/' + files[0][1:]
        # print("x variable: ", x)
        # print("\n")
        # isPath = "is Directory" if os.path.isdir(x) else "is not Directory"
        # os.chdir(x)
        # print("subfolder files: ", os.listdir(x))
        # print(isPath)
        # self._viewFiles(files)
        # print(x)

    def getFile(self, fname, srch_path='C:/'):
        # for root, dir, files in os.walk(srch_path):
        #     if fname in files:
        #         results.append(os.path.join(root, fname))
        #     print("root {0}, files {1}".format(root, files))
        # return results
        # paths = glob.glob(
        #     "C:/path/file/Documents/Programming/Python/scripts/*.py")
        if srch_path == 'C:/':  # traverses top-down order starting from the C: directory
            return self._fileFind(fname, srch_path)
        else:
            f = os.listdir()
            print("Current directory files:", f, "\n\n")
            curr_dir = os.getcwd()
            stringifyPath = str(curr_dir)
            # splits list by "//" character
            splitPath = stringifyPath.split("\\")
            # returns the directory path argument
            arry_result = self._reverseDel(splitPath, srch_path)
            delimiter = '/'
            # joins path using '/' to create the path
            path = delimiter.join(arry_result)
            assert os.path.isdir(path)

            print(path)
            os.chdir(path)
            # checks if argument fname is in the directory of the argument path
            checkFile = "true" if fname in os.listdir() else "false"
            print(checkFile)
            # formats file paths to "C:/file/file"
            files = self._manipFiles(path)
            # if "a"
            print("\n")
            print("files variable", files)

            print("\n")
            x = path + '/' + files[0][1:]
            print("x variable: ", x)
            print("\n")
            isPath = "is Directory" if os.path.isdir(x) else "is not Directory"
            os.chdir(x)
            print("subfolder files: ", os.listdir(x))
            print(isPath)
            self._viewFiles(files)
            print(x)
            return None
            # print(fileManip, "\n")
            # os.chdir(path)

            # infile = "true" if "Zoom" in dirList else "false" #shortand if statement in Python
            # print(infile)

            # use chdir to switch to dir to find files with path
            # print(os.listdir())

            # os.chdir("C:/Users/Kelchi/Documents/Programming/Python")
            # pt = os.path.abspath("Python/testbot.py")
            # pt = glob.glob("*.py")
            # pt = Path(".py").resolve()
            # print(pt)


bot = BotCommands()

#bot.commandControl("ping 127.0.0.1")

result = bot.getFile("scripts")
print(result)

# print()
# print()
# print()
# print()


# user = str(input("Enter text: "))
# cmd = '{0}'.format(user)

# cmd = str(cmd)
# print(type(cmd))

# output = subprocess.check_output(cmd, shell=True)
# print(str(output))
