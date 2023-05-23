from Stack import Liststack,Nodestack


def proc(l):
    s = Liststack(10)
#   s = Nodestack(10)
    for i in l:
        if i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            s.push(i)
        elif i in ['+', '-', '*', '/']:
            s2 = s.stackpop()
            s1 = s.stackpop()
            if i == '+':
                res = s1 + s2
            elif i == '-':
                res = s1 - s2
            elif i == '*':
                res = s1 * s2
            elif i == '/':
                res = s1 / s2
            s.push(res)
        elif i == '=':
            return s.stackpop()

# 6 2 / 3 - 4 2 * + =


L = [6, 2, '/', 3, '-', 4, 2, '*', '+', '=']
# print(proc(L))
# 2+9/3-5  293/+5-=
L = [2, 9, 3, '/', '+', 5, '-', '=']
# print(proc(L))

def in2post(expr):
    """ :param expr: 前缀表达式
        :return: 后缀表达式

        Example：
            "1+((2+3)×4)-5"
            "1 2 3 + 4 × + 5 -"
    """
    stack = Liststack(10)  # 存储栈
    post = Liststack(10)  # 后缀表达式存储
    for i in expr:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            post.push(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            ss = stack.stackpop()
            while ss != '(':
                post.push(ss)
                ss = stack.stackpop()
        elif i in ['+', '-']:
            ss = stack.stackpop()
            if ss in ['*', '/']:
                post.push(ss)
                ss = stack.stackpop()
                if ss:
                    post.push(ss)
                stack.push(i)
            elif ss in ['+', '-']:
                post.push(ss)
                stack.push(i)
            elif ss == '(':
                stack.push(ss)
                stack.push(i)
            else:
                stack.push(i)

        elif i in ['*', '/']:
            ss = stack.stackpop()
            if ss in ['*', '/']:
                post.push(ss)
                stack.push(i)
            elif ss in ['+', '-']:
                stack.push(ss)
                stack.push(i)
            elif ss == '(':
                stack.push(ss)
                stack.push(i)
            else:
                stack.push(i)
    ss = stack.stackpop()
    while ss:
        post.push(ss)
        ss = stack.stackpop()

    return post.s


if __name__ == '__main__':
    s = "1+((2+3)*4)-5"
    post = in2post(s)
    print('后缀表达式： ', post)
    s = "2+9/3-5"
    post = in2post(s)
    print('后缀表达式： ', post)

# 2+9/3-5=  293/+5-=
# 输出：

# 后缀表达式：  ['1', '2', '3', '+', '4', '×', '+', '5', '-']

