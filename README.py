# A.-Spy-Detected-
t = int(input())
for _ in range(t):
	n = int(input())
	lst = list(map(int, input().split()))
	if lst[0] == lst[1]:
		x = lst[0]
		for i in range(n):
			if lst[i] != x:
				print(i + 1)
				break
	else:
		if lst[0] == lst[2]:
			print(2)
		else:
			print(1)
		
