# Implement strStr() from LeetCode #

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
  if len(needle) == 0:
    return 0
  
  for i in range(len(haystack)-len(needle)+1):
    window = ''.join([haystack[j] for j in range(i, i+len(needle))])
    if window == needle:
      return i
  return -1

if __name__ == '__main__':
    print(strStr('hello', 'll'), 2)
    print(strStr('aaaaa', 'baa'), -1)