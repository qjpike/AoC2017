import collections

with open("input.txt") as f:
    dat = [i.split() for i in f.readlines()]


prog_names = set(tuple([i[0] for i in dat]))
being_held = set()

for i in dat:
    if '->' in i:
        for j in i[i.index('->')+1:]:
            if ',' in j:
                being_held.add(j[:-1])
            else:
                being_held.add(j)

base = list(prog_names - being_held)[0]
print("1:",base)

class Program:
    def __init__(self,name,weight):
        self.name = name
        self.own_weight = weight
        self.tot_weight = -1

        self.holds = []
        self.holds_weights = []
    def find_weight(self,d):
        return

    def is_balanced(self):
        if len(self.holds) == 0:
            return True
        else:
            for i in self.holds_weights:
                if i != self.holds_weights[0]:
                    return False
            return True

    def get_weight(self):
        if len(self.holds) == 0:
            return self.own_weight
        else:

            q = collections.deque(self.holds)
            while len(q) > 0:
                n = q.popleft()
                n_weight = n.get_weight()
                self.holds_weights.append(n_weight)
        self.tot_weight = sum(self.holds_weights) + self.own_weight
        return self.tot_weight

    def add_holds(self,o):
        self.holds.append(o)



d = dict()

for i in dat:
    d[i[0]] = Program(i[0],int(i[1][1:-1]))

for i in dat:
    if '->' in i:
        for j in i[i.index('->')+1:]:
            if ',' in j:
                d[i[0]].add_holds(d[j[:-1]])
            else:
                d[i[0]].add_holds(d[j])


d[base].get_weight()

q = collections.deque([base])

last = ''
while len(q) > 0:
    n = q.popleft()
    # print(n, d[n].tot_weight)
    if not d[n].is_balanced():
        # print("unbalanced:",n)
        last = d[n].holds_weights
        l_diff = d[n].holds[last.index(max(last))].own_weight - max(last) + min(last)
        # last_own = d[n].holds[d[n].holds_weights.index(max(d[n].hold_weights))]
        for j in d[n].holds:
            q.append(j.name)

print("2:",l_diff)
