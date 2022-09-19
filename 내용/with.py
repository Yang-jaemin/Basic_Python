# with를 쓰면 파일 여닫기 더 편해

from multiprocessing.util import is_abstract_socket_namespace


import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file)) #close 안해도대
    
with open("study.txt","w", encoding = "utf8") as study_file:   #파일쓰기끝
    study_file.write("python")

with open("study.txt","r", encoding = "utf8") as study_file:   #파일 읽기 끝
    print(study_file.read())
