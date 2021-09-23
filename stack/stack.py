"""
Python List already have them implemented in it
"""


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item):
        # using python already provided us
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")

        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")

        return self.stack[len(self.stack) - 1]


# TODO can be moved to py test files

st = Stack()
st.push(1)

st.push(2)
st.push(3)
print(st.peek())
st.pop()
print(st.peek())
st.pop()
st.pop()

try:
    st.peek()
except Exception as exp:
    print(exp)

print(st.isEmpty())
