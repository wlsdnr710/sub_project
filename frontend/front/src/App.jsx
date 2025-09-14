import React, { useState } from "react";
import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import Navbar from "./Components/Navbar";
import LoginModal from "./Components/Modal/LoginModal";
import { AuthProvider, useAuth } from "./hooks/useAuth";
import SignupModal from "./Components/Modal/SignupModal";
import Main from "./Pages/Main";
import Createpost from "./Pages/Createpost";
import Swal from "sweetalert2";
import { Navigate } from "react-router-dom";
import Membership from "./Pages/Membership";

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
      </div>
    );
  }

  if (!isAuthenticated) {
    Swal.fire({
      icon: "warning",
      title: "로그인 필요",
      text: "로그인이 필요한 서비스입니다. 로그인 후 이용해주세요.",
      confirmButtonColor: "#10B981",
    });
    return <Navigate to="/" replace />;
  }

  return children;
};

const LootLayout = () => {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [isSignupOpen, setIsSignupOpen] = useState(false);

  const onLoginClick = () => {
    setIsSignupOpen(false);
    setIsLoginOpen(true);
  };

  const onSignupClick = () => {
    setIsLoginOpen(false);
    setIsSignupOpen(true);
  };

  const handleCloseModals = () => {
    setIsLoginOpen(false);
    setIsSignupOpen(false);
  };

  return (
    <AuthProvider>
      <Navbar onLoginClick={onLoginClick} onSignupClick={onSignupClick} />
      <main className="flex-grow container mx-auto px-4 py-8">
        <Outlet />
      </main>
      <LoginModal
        isOpen={isLoginOpen}
        onClose={handleCloseModals}
        onSignupClick={onSignupClick}
      />

      <SignupModal
        isOpen={isSignupOpen}
        onClose={handleCloseModals}
        onLoginClick={onLoginClick}
      />
    </AuthProvider>
  );
};
const router = createBrowserRouter([
  {
    path: "/",
    element: <LootLayout />,
    children: [
      { index: true, element: <Main /> },
      {
        element: (
          <ProtectedRoute>
            <Outlet />
          </ProtectedRoute>
        ),
        children: [
          { path: "create-post", element: <Createpost /> },
          { path: "membership", element: <Membership /> },
        ],
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
