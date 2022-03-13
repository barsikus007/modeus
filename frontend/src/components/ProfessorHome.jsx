import React from 'react';
import styled from 'styled-components';

import Navbar from './Navbar';
import ProfessorSidebar from './ProfessorSidebar';
import ProfessorProfile from './ProfessorProfile';

const Row = styled.div`
    display:flex;
    flex-direction: row;
`;

function professorHome() {
  return (
    <>
      <Navbar />
      <Row>
        <ProfessorSidebar />
        <ProfessorProfile />
      </Row>
    </>
  );
}

export default professorHome;
