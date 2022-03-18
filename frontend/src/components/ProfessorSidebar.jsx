import styled from 'styled-components';

const ProfBar = styled.div`
    background-color:#ffffff;
    display:flex;
    flex-direction:column;
    margin-left:10%;
    width:255px;
    margin-top: 0.5%;
    align-items:flex-start;
    padding-left:0.5%;
    padding-right:0.5%;
    min-height: 100vh;
`;

const SearchBar = styled.input`
    width:100%;
    height:30px;
    align-self:center;
    background-color:#f7f7f9;
    color:#969DA3;
    border:none;
    font-size:14px;
`;

const ToolsRow = styled.div`
    display:flex;
    flex-direction:row;
    height:30px;
    width:100%;
    align-items:flex-start;
    justify-content: space-between;
    margin-top:3%;
`;

const Sort = styled.select`
    width:30%;
    margin-top:0;
    border:none;
    color:#969DA3;
    font-size:14px;
`;

const H6 = styled.h6`
    font-size:14px;
    margin-top:0;
    color:#969DA3;
`;

const AddButton = styled.h5`
    color:#969DA3;
    margin-top:0;
    font-size:14px;
`;

const Ul = styled.ul`
    list-style-type: none;

    padding-left: 0;
    margin-top:0;
`;

const Li = styled.li`
    margin-bottom: 20%;
    font-weight:bold;
    font-size:14px;
`;

function ProfessorSidebar() {
  return (
    <ProfBar>
      <SearchBar type="search" placeholder="Search" />
      <ToolsRow>
        <Sort>
          <option>Sort</option>
          <option>option_1</option>
          <option>option_2</option>
          <option>option_3</option>
        </Sort>
        <H6>Filter</H6>
      </ToolsRow>
      <AddButton>Add professor</AddButton>
      <Ul>
        <Li>Name Surname</Li>
        <Li>Name Surname</Li>
        <Li>Name Surname</Li>
      </Ul>
    </ProfBar>
  );
}

export default ProfessorSidebar;
