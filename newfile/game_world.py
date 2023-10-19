# 게임 월들 모듈

# 게임 월드 표현
# 레이어
world = [[], [], []]

# 게임 월드의 객체 담기
def add_object(o, depth0):
    world[depth0].append(o) # 지정된 깊이의 레이어에 추가

# 게임월드 객체들을 몽땅 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

# 게임월드 객체들을 몽땅 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()

# 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('존재하지 않는 걸 지우라고?')