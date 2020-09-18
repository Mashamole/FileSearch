

from collections import defaultdict
import os


visited = defaultdict(bool)


pth = "C:/Apps/334CH/"
pth2 = "C:/Apps/334CH/test"

visited[pth] = True
visited[pth2] = True

if visited[pth + "test"] == True:
    print("true")
else:
    print("false")


print(os.path.isdir("C:/Apps/334CH/test"))


fls = ["apps", "handler", "jax", "dubs"]

f = [i for i in fls if i == "jax" or i == "apps"]
for j in [i for i in fls if i == "jax" or i == "apps"]:
    print(j)
