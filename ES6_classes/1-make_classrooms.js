import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const instanceA = new ClassRoom(19);
  const instanceB = new ClassRoom(20);
  const instanceC = new ClassRoom(34);
  const obj = [instanceA, instanceB, instanceC];
  return obj;
}
