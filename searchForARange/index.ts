// https://www.interviewbit.com/problems/search-for-a-range/
type Maybe<T> = T | undefined
const searchRange = (
  nums: number[],
  target: number,
  offset: number = 0,
  dir?: Maybe<string>
): [number, number] | number => {
  const mid = Math.floor(nums.length / 2)
  const midVal = nums[mid]

  if (nums.length === 0) return -1
  if (nums.length === 1) return -1

  let startVal =
    midVal === target
      ? nums[mid - 1] !== target
        ? mid + offset
        : undefined
      : undefined

  let endVal =
    midVal === target
      ? nums[mid + 1] !== target
        ? mid + offset
        : undefined
      : undefined

  if (dir) {
    if (dir === 'start') {
      if (startVal) {
        return startVal
      } else {
        return searchRange(nums.slice(mid), target, offset + mid, 'start')
      }
    } else {
      if (endVal) {
        return endVal
      } else {
        return searchRange(nums.slice(mid), target, offset + mid, 'end')
      }
    }
  }

  if (startVal !== undefined && endVal !== undefined) {
    return [startVal, endVal]
  }

  if (startVal !== undefined && endVal !== undefined) {
    return [startVal, endVal]
  } else if (startVal !== undefined) {
    return [
      startVal,
      searchRange(nums.slice(mid), target, mid + offset, 'end') as number,
    ]
  } else if (endVal) {
    return [
      searchRange(nums.slice(0, mid), target, 0, 'start') as number,
      endVal,
    ]
  } else {
    return [
      searchRange(nums.slice(0, mid), target, 0, 'start') as number,
      searchRange(nums.slice(mid), target, mid, 'end') as number,
    ]
  }
}
// [start, end]
const A = [5, 17, 3, 100, 111]
const B = 3
console.log(searchRange(A, B))
