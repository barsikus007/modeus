import React from 'react';
import styled from 'styled-components';

import Navbar from './jsx_example';
import ProfessorsList from './professorsList';
import ProfessorProfile from './professorProfile';

const Row = styled.div`
  display:flex;
  flex-direction: row;
`;

function App() {
  return (
    <>
      <Navbar />
      <Row>
        <ProfessorsList />
        <ProfessorProfile />
      </Row>
    </>
  );
}

export default App;
