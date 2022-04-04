# from collections import Counter
#
# def solution(str1, str2):
#     i = 0
#     arr1 = []
#     while i < len(str1):
#         if str1[i:i + 2].isalpha() and len(str1[i:i + 2]) == 2:
#             arr1.append(str1[i:i + 2].lower())
#         i += 1
#
#     j = 0
#     arr2 = []
#     while j < len(str2):
#         if str2[j:j + 2].isalpha() and len(str2[j:j + 2]) == 2:
#             arr2.append(str2[j:j + 2].lower())
#         j += 1
#
#     if len(arr1) == 0 and len(arr2) == 0:
#         jab = 1
#     else:
#         set1 = set(arr1)
#         set2 = set(arr2)
#         counter1 = Counter(arr1)
#         counter2 = Counter(arr2)
#         n = set1 & set2
#         u = set1 | set2
#         ja = 0
#         jb = 0
#
#         for i in n:
#             ja += min(counter1[i], counter2[i])
#         for i in u:
#             jb += max(counter1[i], counter2[i])
#
#         jab = ja / jb
#     answer = int(jab * 65536)
#     return answer

