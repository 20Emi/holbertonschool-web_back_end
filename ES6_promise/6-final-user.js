import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  const uploadPhoto1 = uploadPhoto(fileName);
  const signUpUser1 = signUpUser(firstName, lastName);

  return Promise.allSettled([uploadPhoto1, signUpUser1])
    .then((results) => results.map((res) => ({ status: res.status, value: res.value })));
}
