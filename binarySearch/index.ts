const search = (nums: number[], target: number): number => {
  if (nums.length === 0 || (nums.length === 1 && nums[0] !== target)) return -1
  const mid = Math.floor(nums.length / 2)
  const midVal = nums[mid]
  if (target === midVal) return mid
  else if (target > midVal) {
    const searched = search(nums.slice(mid), target)
    return searched === -1 ? -1 : searched + mid
  } else {
    return search(nums.slice(0, mid), target)
  }
}

const inputSample = [-1, 0, 3, 5, 9, 12]
const targetSample = 9
console.log(search(inputSample, targetSample))
const inputSample2 = [-1, 0, 3, 5, 9, 12]
const targetSample2 = 2
console.log(search(inputSample2, targetSample2))
