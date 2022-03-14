import React from 'react';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

const Navrow = styled.nav`
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

const StyledNavLink = styled(NavLink)`
  color: black;
  text-decoration: none;
  &:hover {
    color: green;
  }
  &.active {
    color: red;
    &:hover {
      color: red;
    }
  }
`;

const H5 = styled.h5`
    font-size: 18px;
    font-weight: bold;
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
    <Navrow>
      <Tabs>
        <Square />
        <Square />
        <Square />
        <StyledNavLink to="/"><H5>Main</H5></StyledNavLink>
        <StyledNavLink to="/course"><H5>Courses</H5></StyledNavLink>
        <StyledNavLink to="/student"><H5>Students</H5></StyledNavLink>
        <StyledNavLink to="/professor"><H5>Professors</H5></StyledNavLink>
      </Tabs>
      <NameBox>
        <H5>Name Surname</H5>
        <H5>log out</H5>
      </NameBox>
    </Navrow>
  );
}

export default Navbar;
