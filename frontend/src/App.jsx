import React from 'react';
import { Route, Routes } from 'react-router-dom';

import ProfessorHome from './components/ProfessorHome';

function App() {
  return (
    <Routes>
      <Route path="/" element={<ProfessorHome />} />
    </Routes>
  );
}

export default App;
