import streamlit as st
from typing import List

st.title('✅ To-do APP ✅')

# 1. todo 입력칸 제공
# 2. todos(session_state)에 새 todo 저장
# 3. todos 목록화
# 4. 완료한 todo는 checkbox를 통해 완료 처리

class Todo:
    def __init__(self, task: str, done: bool=False) -> None:
        self.task = task
        self.done = done

    # 리스트가 __str__말고 __repr__을 호출하기 때문
    def __repr__(self):
        return f'Todo(task={self.task}, done={self.done}'


def add_todo():
    new_task = st.session_state['new_task']
    print(f'add_todo: new_task = {new_task}')
    if new_task:
        new_todo = Todo(new_task)
        st.session_state['todos'].append(new_todo)
        st.session_state['new_task'] = ''

def togle_done(index: int):
    todo = st.session_state['todos'][index]
    todo.done = not todo.done

# todo 초기화
if 'todos' not in st.session_state:
    st.session_state.todos: List[Todo] = [] #Todo 라는 타입의리스트


# 입력창
# - key 매개변수는 session_state 자동등록 및 관리
# - on_change 콜백함수는 사용자 입력 후 엔터를 누르면 지정한 함수를 자동호출
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo)

# 목록
print(f'todos = {st.session_state['todos']}')
# session_state['todos'], session_state.todos 둘 다 가능
if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        # columns(2) -> 2개 , columns([0.2, 0.8]) -> 비율
        col1, col2 = st.columns([0.2, 0.8])
        # args=(i, ) -> on_change 함수에 전달할 인자 -> (i, ) 라고 써야함!!
        col1.checkbox('', value=todo.done, key=f'done_{i}', on_change=togle_done, args=(i, ))
        col2.markdown(f'~~{todo.task}~~' if todo.done else todo.task)
else:
    st.info('할 일을 추가해보세요.✍️')



