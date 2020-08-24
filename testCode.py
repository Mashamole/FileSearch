"""
(Tasks)

1. simulate modified DFS algorithm using file path as Index
    -implement backtracing file path (reverting back to previous path)

[note]
    - will have to find a way to add visited technique for dirs already visited
        in order to backtrack

"""
from collections import defaultdict
import os

graph = defaultdict(list)
graph_ = defaultdict(list)
visited = defaultdict(bool)
searched = defaultdict(bool)

# graph[2].append(10)

# visited = [False] * (max(graph)+1)


def testSrchFile(fname, srch_path):
    visit = defaultdict(bool)
    return testSrchFileUtil(fname, srch_path, visit)


def testSrchFileUtil(fname, srch_path, visited):
    f = os.chdir(srch_path)
    delimiter = '/'
    # # joins path using '/' to create the path
    arry_result = os.listdir(f)
    # print(arry_result, "\n\n")
    trackPath = []
    trackPath.append(srch_path)
    # change idx to string type (use "C:/" as key for graph)
    dirIdx = srch_path
    visited[dirIdx] = True  # graph for visited paths
    # add srch_path argument to graph
    graph_[dirIdx] = arry_result
    print(graph_[dirIdx])
    # check if file is in the first srch_path run

    if fname in graph_[dirIdx]:  # checks if file is in root directory
        print("file exist")
        keys = graph_.keys()
        # print(keys)
        # print(srch_path)
        # assign the key path for path concatenation in next lines
        keyPath = srch_path if srch_path in keys else " "
        print(keyPath)
        if keyPath[len(keyPath)-1] != '/':
            print("did run 1st return")
            print(keyPath + '/' + fname)
            return keyPath + '/' + fname
        else:
            print("did run 2nd return ")
            print(keyPath + fname)
            return keyPath + fname

    for f in arry_result:  # traverse through list of files in path
        if f[0] != '$':
            # check if file is a dir
            if os.path.isdir(f):
                # pass
                if srch_path[len(srch_path)-1] != '/':  # add delimiter for paths
                    recurPath = srch_path + delimiter + f
                else:
                    recurPath = srch_path + f
                print(recurPath)

                # find way to backtrack dirs
                return testSrchFileUtil(fname, recurPath, visited)

            if graph_[dirIdx] == [] or visited[dirIdx] != True:
                print("Checking f "+f)
                p = srch_path.split("/")
                p.pop()
                pth = delimiter.join(p)

                return testSrchFileUtil(fname, pth, visited)

                # graph[dirIdx]

                # os.chdir()


# pth = testSrchFile("AUMIDs", "C:/")
# print(type(pth))


def revertDir(pth):
    delim = "/"
    new_pth = pth.split("/")
    new_pth.pop()
    pth = delim.join(new_pth)
    print(pth)
    return pth


# Test data for directories and file path
graph["C:/"].append("Apps")
graph["C:/"].append("test1.py")
graph["C:/Apps"].append("334CH")
graph["C:/Apps"].append("7VDFT")
graph["C:/Apps/dirFile"].append("word.dox")
graph["C:/Apps/dirFile"].append("word2.dox")


v = "C:/Apps/'334CH'"
npth = ""
searched[v] = True
# v = "C:/Apps/de"
if searched[v] == True:
    x = revertDir(v)
os.chdir(x)
print(os.listdir())
if graph[v] == [] or searched[v] == True:
    print("file not found")
v = "C:/Apps/334CH/dell"


# searched[v] = False
# fname = "word.dox"
# keys = graph.keys()
# if searched[v] == False:
#     print("false")
# assign the key path for path concatenation in next lines
# keyPath = v if v in keys else " "
# for i in graph[v]:
#     print(i)
#     # v = v+1
#     if fname in graph[v]:
#         print(v + "/" + fname)
#     else:
#         print("file not found")
