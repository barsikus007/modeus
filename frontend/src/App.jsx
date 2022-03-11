import './App.css';
import styled from 'styled-components';
import Navbar from "./jsx_example.jsx";
import ProfessorsList from "./professorsList.jsx";
import ProfessorProfile from "./professorProfile.jsx";

const Row = styled.div `
  display:flex;
  flex-direction: row;
`

function App() {
  return (
    <div className="App" >
      
              <Navbar/>
              <Row>
              <ProfessorsList /> 
              <ProfessorProfile></ProfessorProfile>
              </Row>
    </div>
  );
}

export default App;
