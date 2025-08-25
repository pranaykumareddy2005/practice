graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Following is the breadth-first search")
bfs(visited,graph,'5')                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      PS C:\Users\User\Desktop\5A6-AI LAB>  & 'c:\Users\User\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\User\.vscode\extension0' '--' 'C:\Users\User\Desktop\5A6-AI LAB\DFS.py'
Following is the Depth-First Search:
5
PS C:\Users\User\Desktop\5A6-AI LAB>  c:; cd 'c:\Users\User\Desktop\5A6-AI LAB'; & 'PPPPPS C:\Users\User\Desktop\5A6-AI LAB>  c:; cd 'c:\Users\User\Desktop\5A6-AI LAB'; & 'c:\Users\User\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\User\.vscode\extensions\ms-python.debugpy-2024.14.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher' '50250' '--' 'c:\Users\User\Desktop\5A6-AI LAB\BFS.py'
Following is the breadth-first search
5 3 7 2 4 8
PS C:\Users\User\Desktop\5A6-AI LAB>