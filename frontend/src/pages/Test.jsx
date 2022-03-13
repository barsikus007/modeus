/* eslint-disable   jsx-a11y/label-has-associated-control */
import React from 'react';
import { useMutation, useQuery, useQueryClient } from 'react-query';

import { getStudents } from 'queries/students';

function Test() {
  const queryClient = useQueryClient();

  const {
    isLoading, isError, data, error, refetch,
  } = useQuery('students', getStudents);

  const { mutate } = useMutation((event) => {
    event.preventDefault();
    const body = Object.fromEntries(new FormData(event.target).entries());

    return fetch('/api/v1/student', {
      method: 'POST',
      body: JSON.stringify(body),
      headers: new Headers({
        'content-type': 'application/json',
      }),
    });
  }, {
    onSuccess: () => {
      queryClient.invalidateQueries('students');
    },
  });

  return (
    <>
      Test page for testing purpuses
      <br />
      (Open network tab (F12 in Edge/Chrome))
      <br />
      Query example:
      <form onSubmit={mutate}>
        <label>
          name
          <input name="name" value="Канеки Кен" />
        </label>
        <br />
        <label>
          year
          <input name="year" value="993" />
        </label>
        <br />
        <label>
          major_id
          <input name="major_id" value="1" />
        </label>
        <br />
        <button type="submit">CREATE</button>
      </form>
      <br />
      Students list
      <br />
      <button type="button" onClick={refetch}>REFRESH</button>
      <br />
      {isLoading ?? 'LOADING'}
      <br />
      {isError ?? 'ERROR'}
      <br />
      {(data || []).map((student) => (
        <div key={student.id}>
          {student.name}
          :
          {' '}
          {student.year}
        </div>
      ))}
      <br />
      {`${error}` ?? 'error'}
    </>
  );
}

export default Test;
