import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 현재 폴더명에서 시작해서 하위 폴더까지 탐색하는 함수
def search(folderName):
    global folderInfo, files, fileCnt

    files |= folderInfo[folderName]['files']
    fileCnt += folderInfo[folderName]['cnt']

    if not folderInfo[folderName]['folders']:
        return

    for childFolder in folderInfo[folderName]['folders']:
        search(childFolder)


if __name__ == '__main__':
    folderInfo = {
        'main': {'files': set(), 'folders': [], 'cnt' : 0}
    }
    files = set()
    fileCnt = 0

    N, M = map(int, input().split())

    for _ in range(N + M):
        parentFolder, name, type = input().strip().split()

        if parentFolder not in folderInfo: # 부모 폴더가 없으면 생성해줌
            folderInfo[parentFolder] = {'files': set(), 'folders': [], 'cnt' : 0}

        if type == '1':  # 폴더 일 때
            if name not in folderInfo: # 폴더명이 처음 입력으로 주어지면 생성해줌
                folderInfo[name] = {'files': set(), 'folders': [], 'cnt' : 0}
            folderInfo[parentFolder]['folders'].append(name)
        else:
            folderInfo[parentFolder]['files'].add(name)
            folderInfo[parentFolder]['cnt'] += 1

    Q = int(input())

    for _ in range(Q):
        folder = input().strip().split('/')[-1]
        search(folder)
        print(len(files), fileCnt)
        files.clear()
        fileCnt = 0