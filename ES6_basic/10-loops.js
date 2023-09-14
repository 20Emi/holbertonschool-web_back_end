export default function appendToEachArrayValue(array, appendString) {
  const newarrays = [];
  for (const idx of array) {
    newarrays.push(appendString + idx);
  }

  return newarrays;
}
