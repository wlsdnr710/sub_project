import { useState } from "react";
import Logo from "./layout/Logo";
import AuthButtons from "./auth/DAuthButtons";
import MobileMenu from './layout/MobileMenu';
import MobileToggleButton from "./layout/MobileToggleButton";
import Categories from "./layout/Categories";

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

  const onCategoryClick=(category)=>{
    alert(category);
  }

  return (
    <nav className="bg-purple-500">
      <div className="max-w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-14 md:h-20">
          <div className="flex items-center flex-1">
            <Logo />
          </div>

          <MobileToggleButton isOpen={isOpen} setIsOpen={setIsOpen}/>

          <AuthButtons
            isAuthenticated={isAuthenticated}
            isOpen={isOpen}
            setIsOpen={setIsOpen}
            onLogoutClick={onLogoutClick}
            onLoginClick={onLoginClick}
            onSignupClick={onSignupClick}
          />
        </div>

      <MobileMenu 
            isAuthenticated={isAuthenticated}
            isOpen={isOpen}
            setIsOpen={setIsOpen}
            onLogoutClick={onLogoutClick}
            onLoginClick={onLoginClick}
            onSignupClick={onSignupClick}
      />
      </div>

      <Categories onClick={onCategoryClick} />
    </nav>
  );
}

export default Navbar;
