export default function bs_list(haystack: number[], needle: number): number {
  let lo = 0;
  let hi = haystack.length;

  do {
    const mid = Math.floor((lo + hi) / 2);
    const middle = haystack[mid];
    if (middle === needle) {
      return middle;
    } else if (middle < needle) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  } while (lo < hi)

  return -1;
}
