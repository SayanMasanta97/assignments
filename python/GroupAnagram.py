class solution:
    def  An_Anagram(self, strs):
        L={}
        for i in strs:
            tempS = "".join(sorted(i))
            if tempS in L:
                L[tempS].append(i)
            else:
                L[tempS] = [i]
        result = []
        for item in L.values():
            result.append(item)
        return result
import ast
S=solution()
print(S.An_Anagram(ast.literal_eval(input("Enter your choice:"))))