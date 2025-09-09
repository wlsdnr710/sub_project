import { useState } from "react";
import Logo from "./layout/Logo";
import DAuthButtons from "./auth/DAuthButtons";
import MobileAuthButtons from "./auth/MobileAuthButtons";
import MobileMenu from "./layout/MobileMenu";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const isAuthenticated = false;

  const onLoginClick = () => {
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
          </div>
          <DAuthButtons
            isAuthenticated={isAuthenticated}
            isOpen={isOpen}
            setIsOpen={setIsOpen}
            onLogoutClick={onLogoutClick}
            onLoginClick={onLoginClick}
            onSignupClick={onSignupClick}
          />
          <MobileMenu />
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
