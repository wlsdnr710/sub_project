import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Navbar from "./components/Navbar";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navbar />, // "/ 경로로 들어갈때 Navbar 컴포넌트 렌더링"
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
