export default function createInt8TypedArray(length, position, value) {
  if (position < 0 && position >= length) {
    console.error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const dataview = new DataView(buffer);
  // 'setInt8' is used to set a signed 8-bit value at the specified position.
  dataview.setInt8(position, value);
  return dataview;
}
