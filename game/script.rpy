﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

define jeck = Character('젝', color="#FFFFFF")

image any normal = "Character/any.jpg"


# 여기에서부터 게임이 시작합니다.
label start:

    show any normal
    jeck "우왕"

    jeck "한번 클릭하면 이렇게도 할 수 있음"

    return
