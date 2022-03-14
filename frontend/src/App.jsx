import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';

import Common from 'pages/Common';
import Index from 'pages/Index';
import NotFound from 'pages/NotFound';
import ProfessorHome from 'components/ProfessorHome';
import Test from 'pages/Test';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Routes>
        <Route path="/" element={<Common />}>
          <Route path="professor" element={<ProfessorHome />} />
          <Route path="test" element={<Test />} />
          <Route path="*" element={<NotFound />} />
          <Route path="" element={<Index />} />
        </Route>
      </Routes>
      <ReactQueryDevtools position="bottom-right" />
    </QueryClientProvider>
  );
}

export default App;
