import React from 'react';
import styled from 'styled-components';

const Profile = styled.div`
    margin-top:0.5%;
    margin-left:0.5%;
    background-color:#ffffff;
    min-height: 100vh;
    weight:800px;
`;

const MainRow = styled.div`
    display:flex;
    display-direction:row;
    justify-content:space-around;
`;

const Name = styled.h3`
    font-size: 36px;
    font-weight:bold;
    margin-left:10px;
    margin-top:10px;
    margin-bottom:0;
`;

const Type = styled.h6`
    margin-left:10px;
    font-size:14px;
    color:#969DA3;
`;

const Details = styled.h6`
    position: absolute;
    margin-left:10px;
    margin-top:0;

    font-size:14px;
    font-style:normal;
    font-weight:400;
`;

const ChangeStatusBtn = styled.button`
    border:none;
    font-size:14px;
    text-color:#969DA3;
    height:50px;
    weight:116px;
    margin-left: 500px;
`;

const Courses = styled.h5`
`;

const CoursesTable = styled.div`
`;

function ProfessorProfile() {
  return (
    <Profile>
      <MainRow>
        <Name>Name Surname</Name>
        <Type>visiting</Type>
        <ChangeStatusBtn>Change status</ChangeStatusBtn>

      </MainRow>-
      <Details>status: | n.surname.utmn.ru</Details>

    </Profile>
  );
}

export default ProfessorProfile;
