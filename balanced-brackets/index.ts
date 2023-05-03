// https://www.hackerrank.com/challenges/balanced-brackets/problem

const isBalanced = (s: string): string => {
  const len = s.length
  if (len % 2 !== 0) return 'NO'
  const BRACKETS = {
    '{': 1,
    '[': 1,
    '(': 1,
    '}': -1,
    ']': -1,
    ')': -1,
  }
  const BRACKETS2 = {
    '{': '}',
    '[': ']',
    '(': ')',
  }
  const counter = {} as Record<keyof typeof BRACKETS, number>
  let total = 0
  for (let i = 0; i < len; i++) {
    total += BRACKETS[s[i] as keyof typeof BRACKETS]
    if (!counter[s[i] as keyof typeof BRACKETS]) {
      counter[s[i] as keyof typeof BRACKETS] = 1
    } else {
      counter[s[i] as keyof typeof BRACKETS]++
    }
    if (total < 0) {
      return 'NO'
    }
  }
  const failed = Object.keys(BRACKETS2).some(
    (k) =>
      counter[k as keyof typeof BRACKETS] !==
      counter[BRACKETS2[k as keyof typeof BRACKETS2] as keyof typeof BRACKETS]
  )
  if (failed) return 'NO'
  if (total !== 0) return 'NO'
  return 'YES'
}

export {}
