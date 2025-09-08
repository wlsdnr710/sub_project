import { useState } from "react";
import Logo from "./layout/Logo";
import AuthButtons from "./auth/DAuthButtons";
import DAuthButtons from "./auth/DAuthButtons";

function Navbar() {
  const isAuthenticated = false;
  const [isOpen, setIsOpen] = useState(false);

  const onLoginClick = () => {
    setIsOpen(true);
    alert("로그인");
  };

  const onSignupClick = () => {
    alert("회원가입");
  };

  const onLogoutClick = () => {
    alert("로그아웃");
  };
  return (
    <nav className="bg-purple-500">
      <div className="max-w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-14 md:h-20">
          <div className="flex items-center flex-1">
            <Logo />
            <DAuthButtons
              isAuthenticated={isAuthenticated}
              isOpen={isOpen}
              setIsOpen={setIsOpen}
              onLogoutClick={onLogoutClick}
              onLoginClick={onLoginClick}
              onSignupClick={onSignupClick}
            />
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
