"""
(Tasks)

1. simulate modified DFS algorithm using file path as Index

"""
from collections import defaultdict
import os

graph = defaultdict(list)
graph_ = defaultdict(list)
# Test data for directories and file path
graph["C:/"].append("Apps")
graph["C:/"].append("test1.py")
graph["C:/Apps"].append("dirFile")
graph["C:/Apps"].append("apptest.cpp")
graph["C:/Apps/dirFile"].append("word.dox")

# graph[2].append(10)

# visited = [False] * (max(graph)+1)


def testSrchFile(fname, srch_path):
    f = os.chdir(srch_path)
    delimiter = '/'
    # # joins path using '/' to create the path
    arry_result = os.listdir(f)
    # print(arry_result, "\n\n")
    trackPath = []
    trackPath.append(srch_path)
    # change idx to string type (use "C:/" as key for graph)
    dirIdx = srch_path
    # add srch_path argument to graph

    graph_[dirIdx] = arry_result
    print(graph_)
    # check if file is in the first srch_path run

    if fname in graph[dirIdx]:
        keys = graph_.keys()
        # assign the key path for path concatenation in next lines
        keyPath = srch_path if srch_path in keys else " "
        return keyPath + fname
    for f in arry_result:
        if f[0] != '$':
            if os.path.isdir(f):  # check
                pass
                # recurPath = srch_path + delimiter + f
                # testSrchFile(fname, recurPath)
                # graph[dirIdx]

                # os.chdir()


x = testSrchFile("server.py", "C:/")
print(x)

# v = "C:/Apps/dirFile"
# fname = "word.dox"
# keys = graph.keys()
# # assign the key path for path concatenation in next lines
# keyPath = v if v in keys else " "
# for i in graph[v]:
#     print(i)
#     # v = v+1
#     if fname in graph[v]:
#         print(v + "/" + fname)
#     else:
#         print("file not found")
