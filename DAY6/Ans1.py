def diStringMatch(s):
        i, n = 0, len(s)
        ans = []
        for c in s:
            if c == 'I': 
                ans.append(i)
                i+=1
            else:
                ans.append(n)
                n-=1
        ans.append(i)
        return ans

# Test example
s = "IDID"
output = diStringMatch(s)
print(output)  # Output: [0, 4, 1, 3, 2]


