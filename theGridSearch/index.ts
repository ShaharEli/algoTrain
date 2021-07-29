// https://www.hackerrank.com/challenges/the-grid-search/problem

const gridSearch = (G: string[], P: string[]): string => {
  const input = G.map((row) => row.split(""));
  const pattern = P.map((row) => row.split(""));
  const firstLetterToSearch = pattern[0][0];
  const patternRowLength = pattern[0].length;
  const patternColLength = pattern.length;
  const inputRowLength = input[0].length;
  const inputColLength = input.length;

  for (let i = 0; i < inputRowLength * inputColLength; i++) {
    const rowNum = i % inputRowLength;
    const colNum = Math.floor(i / inputRowLength);
    if (
      inputRowLength - rowNum < patternRowLength ||
      inputColLength - colNum < patternColLength
    ) {
      continue; //not possible to fit the pattern
    }
    const currentPointOnGrid = input[colNum][rowNum];
    if (currentPointOnGrid === firstLetterToSearch) {
      let checker = true;
      for (let j = 0; j < patternRowLength * patternColLength; j++) {
        const patternRowNum = j % patternRowLength;
        const patternColNum = Math.floor(j / patternRowLength);
        const gridRowNum = rowNum + patternRowNum;
        const gridColNum = colNum + patternColNum;

        if (
          input[gridColNum][gridRowNum] !==
          pattern[patternColNum][patternRowNum]
        ) {
          checker = false;
          break;
        }
      }
      if (checker) return "YES";
    }
  }

  return "NO";
};

const sampleInputG = [
  "7283455864",
  "6731158619",
  "8988242643",
  "3830589324",
  "2229505813",
  "5633845374",
  "6473530293",
  "7053106601",
  "0834282956",
  "4607924137",
];

const sampleInputP = ["9505", "3845", "3530"];

// expected YES
console.log(gridSearch(sampleInputG, sampleInputP));
