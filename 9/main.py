f = open("input.txt")
dat = f.read().strip()

ptr = 0
garbage_count = 0
score = 0
open_cb = 0
open_lt = 0
char_count = 0
while ptr < len(dat):
    if dat[ptr] == "!":
        ptr += 2
        continue
    elif dat[ptr] == '{' and open_lt == 0:
        open_cb += 1
        score += 1
    elif dat[ptr] == '}' and open_lt == 0:
        open_cb -= 1
        garbage_count += score
        score -= 1
    elif dat[ptr] == "<" and open_lt == 0:
        open_lt += 1
        char_count -= 1
    elif dat[ptr] == ">":
        open_lt -= 1

    if open_lt > 0 :
        char_count += 1

    ptr += 1


print(garbage_count)
print(char_count)