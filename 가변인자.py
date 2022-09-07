#가변인자

#def profile (name, age, lang1, lang2, lang3):
#    print("이름 {0}, 나이: {1}, 언어1 : {2}, 언어2 : {3}".format(name,age,lang1,lang2),end=" ") # end = " " 이걸 써주면 줄바꿈을 안하고 다음 문장으로 넘어감
    
#profile("유재석",20,"py","java","c")

#profile("유재석",20,"","","")
def profile(name, age, *language): #넣고싶은 만큼 넣을수 있음
    print("이름 {0}, 나이: {1}".format(name,age),end=" ")
    for lang in language:
        print(lang, end =" ")
    print()

profile("유재석",20,"py","java","c","sd","Sd","qwe") #서로 다른 갯수의 값을 넣을때 가변인자를 사용하면 좋아용

profile("양재민",20,"py","java")