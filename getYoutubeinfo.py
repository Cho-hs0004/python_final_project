# 유튜브 URL을 입력받으면 해당 영상의 제목과 카테고리를 설정한 .txt파일에 저장하는 프로그램이다.

from py_youtube import Data
import os.path

#  정보를 저장할 .txt파일의 이름을 입력받는다.
filename = input("Enter Your file name : ")

# 위에서 이름만 입력받으면 파일의 경로와 형식자를 지정해준다.
textfile = "/home/chs/Desktop/" + filename + ".txt"

count = 1

while True:
    # 유튜브 영상의 URL을 입력받는다.
    videoURL = input("Enter Youtube Video URL(Enter [X] to exit program) : ")
    
    # x or X를 입력하면 프로그램 종료
    if videoURL == 'x' or videoURL == 'X':
        print("exit program")
        break

    # URL이 잘못되었으면 루프문의 처음으로 이동
    if not("youtube.com" in videoURL):
        print("URL is wrong..")
        continue

    #  유튜브 영상의 제목과 카테고리를 받아온다.
    dataName = Data(videoURL).title()
    dataCategory = Data(videoURL).category();
    
    # 저장하고자 하는 파일에 지금까지 몇개의 영상정보가 들어있는지 확인 후 count를 설정한다.
    if os.path.isfile(textfile):
        with open(textfile, 'r') as file:
            count = (int)(len(file.readlines())/4) + 1
    
    # 파일에 영상 정보들을 입력한다.
    with open(textfile, 'a', encoding='utf-8') as file:
        file.write(str(count) + ". \n")
        file.write(dataName + '\n')
        file.write(dataCategory + '\n')
        file.write(videoURL + '\n')
