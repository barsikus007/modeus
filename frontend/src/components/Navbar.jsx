import React from 'react';
import styled from 'styled-components';

const Body = styled.body`
    background-color: #fcecea;
`;

const Navrow = styled.div`
    display: flex;
    flex-direction: row;

    justify-content: space-between;
    background-color: #ffffff;
`;

const Square = styled.div`
    height:18px;
    width:18px;
    background-color:black;
`;

const H5 = styled.h5`
    font-size: 18px;
    font-weight: bold;
    &:hover {
        color:green;
    }
`;

const Tabs = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    margin-left:8.5%;
    width: 50%;
`;

const NameBox = styled.div`
    display:flex;
    flex-direction:row;
    justify-content:space-around;
    align-items: flex-end;
    width:20%;
    
    margin-right:11%;
`;

function Navbar() {
  return (
    <Body>
      <Navrow>
        <Tabs>
          <Square />
          <Square />
          <Square />
          <H5>Main</H5>
          <H5>Courses</H5>
          <H5>Students</H5>
          <H5>Professors</H5>
        </Tabs>
        <NameBox>
          <H5>Name Surname</H5>
          <H5>log out</H5>
        </NameBox>
      </Navrow>
    </Body>
  );
}

export default Navbar;
