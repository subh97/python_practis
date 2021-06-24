def palindromes_string(input, j, k):
  count = 0
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    print(input[j: k + 1])
    count += 1

    j -= 1
    k += 1

  return count


def all_palindrome_strings(input):
  count = 0
  for i in range(0, len(input)):
    count += palindromes_string(input, i - 1, i + 1)
    count += palindromes_string(input, i, i + 1)

  return count


s = "aabbbaa"
print("Total palindrome substrings: ", all_palindrome_strings(s))