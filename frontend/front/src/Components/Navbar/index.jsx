import { useState } from "react";
import Logo from "./layout/Logo";
import AuthButtons from "./auth/DAuthButtons";
import DAuthButtons from "./auth/DAuthButtons";
import MobileMenu from "./layout/MobileMenu";
import MobileAuthButtons from "./auth/MobileAuthButtons";
import MobileToggleButton from "./layout/MobileToggleButton";
import Categories from "./layout/Categories";
import SearchMenu from "./layout/SearchMenu";
import { useAuth } from "../../hooks/useAuth";

function Navbar({ onLoginClick, onSignupClick }) {
  const [isOpen, setIsOpen] = useState(false);
  const { logout, isAuthenticated } = useAuth();

  const onLogoutClick = () => {
    logout();
  };

  const onCategoryClick = (category) => {
    alert(category);
  };
  return (
    <nav className="bg-purple-300">
      <div className="max-w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-14 md:h-20">
          <div className="flex items-center flex-1">
            <Logo />
            <SearchMenu />
          </div>
          <MobileToggleButton isOpen={isOpen} setIsOpen={setIsOpen} />
          <DAuthButtons
            isAuthenticated={isAuthenticated}
            isOpen={isOpen}
            setIsOpen={setIsOpen}
            onLogoutClick={onLogoutClick}
            onLoginClick={onLoginClick}
            onSignupClick={onSignupClick}
          />
        </div>
        <MobileMenu
          isOpen={isOpen}
          setIsOpen={setIsOpen}
          isAuthenticated={isAuthenticated}
          onLoginClick={onLoginClick}
          onLogoutClick={onLogoutClick}
          onSignupClick={onSignupClick}
        />
      </div>

      <Categories onClick={onCategoryClick} />
    </nav>
  );
}

export default Navbar;
