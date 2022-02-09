class combParenthesis(object):
	def Parenthesis_1(str, n):
		L = []
		str.Parenthesis_2(n,n,"",L)
		return L
	def Parenthesis_2(str, left, right, temp, L):
		if left == 0 and right == 0:
			L.append(temp)
			return
		if left > 0:
			str.Parenthesis_2(left-1, right, temp +"(" , L)
		if right > left:
			str.Parenthesis_2(left, right-1, temp + ")" , L)
P = combParenthesis()
print(P.Parenthesis_1(int(input("Enter Your Number:\n"))))