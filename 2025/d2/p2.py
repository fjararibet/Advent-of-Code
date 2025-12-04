import sys

input = open(sys.argv[1]).read().rstrip()

id_ranges = input.split(",")
result = 0
for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]
    for id in range(start, end+1):
        id_s = str(id)
        # print(id)
        for i in range(1, len(id_s)//2 + 1):
            invalid = True
            split_start = 0
            while split_start + i < len(id_s):
                if id_s[split_start:split_start+i] != id_s[split_start+i:split_start+i+i]:
                    # print("differ: ", id_s[split_start:split_start+i], id_s[split_start+i:split_start+i+i])
                    invalid = False
                    break
                split_start += i
            if invalid:
                result += id
                break
        # print()

print(result)
