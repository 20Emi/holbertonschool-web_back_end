export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array of string');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(NewName) {
    if (typeof NewName !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = NewName;
    }
  }

  get length() {
    return this._length;
  }

  set length(NewLength) {
    if (typeof NewLength !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = NewLength;
    }
  }

  get students() {
    return this._students;
  }

  set students(NewStudents) {
    if (!Array.isArray(NewStudents)) {
      throw TypeError('students must be a array of Strings');
    } else {
      this._students = NewStudents;
    }
  }
}
