// https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

const climbingTheLeaderboard = (
  ranked: number[],
  player: number[]
): number[] => {
  const set = Array.from(new Set(ranked.reverse()));
  return player.map((score: number) => {
    if (score < set[0]) return set.length + 1;
    for (let i = 0; i < set.length; i++) {
      if (score === set[i] || (set[i] < score && set?.[i + 1] > score)) {
        return set.length - i;
      }
    }
    return 1;
  });
};

const sampleInputRanked = [100, 100, 50, 40, 40, 20, 10];
const sampleInputPlayer = [5, 25, 50, 120];
//expecting: 6 4 2 1
console.log(climbingTheLeaderboard(sampleInputRanked, sampleInputPlayer));

const sampleInputRanked2 = [100, 90, 90, 80, 75, 60];
const sampleInputPlayer2 = [50, 65, 77, 90, 102];
// expecting: 6 5 4 2 1
console.log(climbingTheLeaderboard(sampleInputRanked2, sampleInputPlayer2));
