/* eslint-disable no-unused-vars */
const apiPath = '/api/v1';

// eslint-disable-next-line import/prefer-default-export
export async function getStudents({ offset, limit }) {
  // TODO path params
  const res = await fetch(`${apiPath}/students`);
  const data = await res.json();
  if (!res.ok) return Promise.reject(data);
  return data;
}
