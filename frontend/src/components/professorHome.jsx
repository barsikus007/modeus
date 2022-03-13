import React from 'react';
import styled from 'styled-components';

import Navbar from './Navbar';
import ProfessorSidebar from './professorSidebar.jsx';
import ProfessorProfile from './professorProfile.jsx';

const Row = styled.div`
    display:flex;
    flex-direction: row;
`;

function professorHome () {
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

export default professorHome;
