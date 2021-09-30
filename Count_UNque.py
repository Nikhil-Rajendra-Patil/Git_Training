def countDis(str):
    if len(str) == 0:
        print("-1")
    else:
	    s = set(str)
	    return len(s)

if __name__ == "__main__":
    n = int(input)
	S = input()
	print(countDis(S))

