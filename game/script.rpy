# 이 파일에 게임 스크립트를 입력합니다.

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

    jeck "여기서 0.5초 기다리고{w=0.5} 여기서는 누를 때 까지 기다릴거야 {w}됐당"

    jeck "자동으로 여기까지 진입 {nw}"

    jeck "자동으로 여기까지 진입 후에{fast} 이런 글을 남길거임"

    jeck "대사록 체크용 더미"

    return
