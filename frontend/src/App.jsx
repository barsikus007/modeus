import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';

import ProfessorHome from 'components/ProfessorHome';
import Test from 'pages/Test';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Routes>
        <Route path="/" element={<ProfessorHome />} />
        <Route path="/test" element={<Test />} />
      </Routes>
      <ReactQueryDevtools position="bottom-right" />
    </QueryClientProvider>
  );
}

export default App;
