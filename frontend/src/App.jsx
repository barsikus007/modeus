import React from 'react';
import styled from 'styled-components';

import Navbar from './components/Navbar';
import ProfessorSidebar from './components/professorSidebar.jsx';
import ProfessorProfile from './components/professorProfile.jsx';

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
