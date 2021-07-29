// https://www.hackerrank.com/challenges/encryption/problem

const encryption = (s: string): string => {
  const stringWithoutSpaces = s.replace(/ /g, "");
  const sqrtLen = Math.sqrt(stringWithoutSpaces.length);
  const rowLength = Math.ceil(sqrtLen);

  const words: string[] = new Array(rowLength).fill("");
  for (let i = 0; i < stringWithoutSpaces.length; i++) {
    const colNum = i % rowLength;
    words[colNum] += stringWithoutSpaces[i];
  }
  return words.join(" ");
};

//expected hae and via ecy
console.log(encryption("haveaniceday"));
