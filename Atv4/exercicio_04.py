MOD = 10**9 + 7

class Estado:
    def __init__(self):
        self.transitions = {}
        self.epsilon = []

def to_postfix(regex):
    output = []
    stack = []
    prec = {'*': 3, '.': 2, '|': 1}
    prev = None
    for token in regex:
        if token in 'ab':
            if prev and (prev in 'ab)*'):
                output.append('.')
            output.append(token)
        elif token == '(':
            if prev and (prev in 'ab)*'):
                output.append('.')
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif token in prec:
            while stack and stack[-1] in prec and prec[stack[-1]] >= prec[token]:
                output.append(stack.pop())
            stack.append(token)
        prev = token
    while stack:
        output.append(stack.pop())
    return ''.join(output)

def parse_regex(regex):
    stack = []
    for c in regex:
        if c == 'a' or c == 'b':
            start = Estado()
            end = Estado()
            start.transitions[c] = [end]
            stack.append((start, end))
        elif c == '*':
            nfa = stack.pop()
            start = Estado()
            end = Estado()
            start.epsilon.append(nfa[0])
            start.epsilon.append(end)
            nfa[1].epsilon.append(nfa[0])
            nfa[1].epsilon.append(end)
            stack.append((start, end))
        elif c == '|':
            right = stack.pop()
            left = stack.pop()
            start = Estado()
            end = Estado()
            start.epsilon.extend([left[0], right[0]])
            left[1].epsilon.append(end)
            right[1].epsilon.append(end)
            stack.append((start, end))
        elif c == '.':
            right = stack.pop()
            left = stack.pop()
            left[1].epsilon.append(right[0])
            stack.append((left[0], right[1]))
    return stack[-1]

def countRecognizedStrings(R, L):
    from collections import deque, defaultdict

    postfix = to_postfix(R)
    start, end = parse_regex(postfix)

    def enumerate_states(start):
        id_map = {}
        queue = deque([start])
        counter = 0
        while queue:
            node = queue.popleft()
            if node in id_map:
                continue
            id_map[node] = counter
            counter += 1
            for lst in node.transitions.values():
                for st in lst:
                    queue.append(st)
            for st in node.epsilon:
                queue.append(st)
        return id_map

    id_map = enumerate_states(start)
    n = len(id_map)
    trans = [defaultdict(set) for _ in range(n)]

    for node, i in id_map.items():
        for sym, lst in node.transitions.items():
            for dest in lst:
                trans[i][sym].add(id_map[dest])
        for e in node.epsilon:
            trans[i][''].add(id_map[e])

    def epsilon_closure(states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for dest in trans[state].get('', []):
                if dest not in closure:
                    closure.add(dest)
                    stack.append(dest)
        return closure

    start_states = epsilon_closure([id_map[start]])
    accept = id_map[end]
    dp = [0] * n
    for s in start_states:
        dp[s] = 1

    for _ in range(L):
        new_dp = [0] * n
        for i in range(n):
            for sym in 'ab':
                for j in trans[i].get(sym, []):
                    for dest in epsilon_closure([j]):
                        new_dp[dest] = (new_dp[dest] + dp[i]) % MOD
        dp = new_dp

    return dp[accept]


def main():
    T = 3
    casos = [
        ("((ab)|(ba))", 2),
        ("((a|b)*)", 5),
        ("((a*)(b(a*)))", 100)
    ]
    for R, L in casos:
        print(f"Expressão: {R}, Tamanho: {L}")
        resultado = countRecognizedStrings(R, L)
        print("Reconhecidas:", resultado)
    