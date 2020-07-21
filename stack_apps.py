from stack import Stack


class ParenthesisMatching:
    exp: str = None
    stack: Stack = None

    def __init__(self, exp):
        self.exp = exp
        self.stack = Stack()

    def match(self):
        xLen = len(self.exp)
        if xLen > 1:
            for x in range(xLen):
                if self.exp[x] == "(" or self.exp[x] == "{" or self.exp[x] == "[":
                    self.stack.push(self.exp[x])
                elif self.exp[x] == ")" or self.exp[x] == "}" or self.exp[x] == "]":
                    if not self.stack.isEmpty():
                        if self.exp[x] == ")":
                            if self.stack.topMost() == "(":
                                self.stack.pop()
                            else:
                                return False
                        if self.exp[x] == "}":
                            if self.stack.topMost() == "{":
                                self.stack.pop()
                            else:
                                return False
                        if self.exp[x] == "]":
                            if self.stack.topMost() == "[":
                                self.stack.pop()
                            else:
                                return False
                    else:
                        # when i wanna pop but stack is empty that means the brekets are'nt matching return false
                        return False
            # if after all stack is empty that means () are matching
            if self.stack.isEmpty():
                return True
        # if
        return False


class Postfix:
    expression = None
    isPostfix = None

    def __init__(self, exp):
        self.expression = exp
        self.isPostfix = False

    def fromInfix2Post(self):
        xprelen = len(self.expression)
        exp = self.expression
        stack = Stack()
        postfixExp = ""
        if xprelen > 0:
            for x in range(xprelen):
                if self.getPrecedence(exp[x]) == 0:
                    postfixExp = postfixExp + exp[x]
                else:
                    if stack.topMost() is None:
                        stack.push(exp[x])
                    elif self.getPrecedence(stack.topMost()) < self.getPrecedence(exp[x]):
                        stack.push(exp[x])
                    else:
                        while self.getPrecedence(stack.topMost()) >= self.getPrecedence(exp[x]):
                            postfixExp = postfixExp + stack.pop()
                        stack.push(exp[x])

            if stack.topMost() is not None:
                while stack.size > 0:
                    postfixExp = postfixExp + stack.pop()
        return postfixExp

    def eval(self):
        expLen = len(self.expression)
        exp = self.fromInfix2Post()
        stack = Stack()
        if expLen > 0:
            for x in range(expLen):
                if self.getPrecedence(exp[x]) == 0:
                    stack.push(exp[x])
                elif self.getPrecedence(exp[x]) != 0:
                    _sum = 0
                    x2 = float(stack.pop())
                    x1 = float(stack.pop())
                    if exp[x] == "+":
                        _sum = x1+x2
                    elif exp[x] == "-":
                        _sum = x1 - x2
                    elif exp[x] == "*":
                        _sum = x1 * x2
                    elif exp[x] == "/":
                        _sum = x1 / x2
                    stack.push(str(_sum))
        return stack.pop()




    @staticmethod
    def getPrecedence(char):
        table = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        x = None
        try:
            x = table[char]
        except IndexError:
            x = 0
        except Exception:
            x = 0
        return x
