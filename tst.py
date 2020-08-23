num = 16

ans = 2
step = 16000000
direct_0 = 1
count = 0
while num != ans ** 2:
	if num > ans ** 2:
		direct_1 = 1
	else:
		direct_1 = -1

	if direct_0 != direct_1:
		while ans <= step:
			step //= 2
		# step *= 2
		if step == 1:
			print('thats all')
			break

	ans += step * direct_1

	print(f'num {num}\tans {ans}\tans**2 {ans**2}\t\tstep {step}\tdirect {direct_1 == direct_0}')
	direct_0 = direct_1


	count += 1
	if count == 60: break