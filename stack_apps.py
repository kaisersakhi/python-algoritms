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


def getPrecedence(char):
    table = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    x = None
    try:
        x = table[char]
    except:
        x = 0
        pass
    return x


class Postfix:

    pass
