import React from "react";
import Navbar from "./components/Navbar";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navbar />, // '/'경로로 들어갈때 Navbar 컴포넌트 렌더링
  },
]);

const App = () => {
  //라우터 객체를 앱에 공급하는 역할
  return <RouterProvider router={router} />;
};

export default App;
