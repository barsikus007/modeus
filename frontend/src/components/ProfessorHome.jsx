import styled from 'styled-components';

import ProfessorSidebar from './ProfessorSidebar';
import ProfessorProfile from './ProfessorProfile';

const Row = styled.div`
    display:flex;
    flex-direction: row;
`;

function professorHome() {
  return (
    <Row>
      <ProfessorSidebar />
      <ProfessorProfile />
    </Row>
  );
}

export default professorHome;
