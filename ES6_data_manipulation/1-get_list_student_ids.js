export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const arrayIds = students.map((studentlist) => studentlist.id);

  return arrayIds;
}
