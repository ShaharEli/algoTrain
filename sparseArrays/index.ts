// https://www.hackerrank.com/challenges/sparse-arrays/problem
const matchingStrings = (strings: string[], queries: string[]): number[] =>
  queries.map((query) => strings.filter((string) => string === query).length);

const stringsSample = ["aba", "baba", "aba", "xzxb"];
const queriesSample = ["aba", "xzxb", "ab"];

//expected [2, 1, 0]
console.log(matchingStrings(stringsSample, queriesSample));
