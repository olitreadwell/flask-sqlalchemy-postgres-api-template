import { NavLink } from "react-router-dom";

const navLinkStyles = {
  margin: "0.5rem",
};

const NavBar = () => (
  <nav>
    <NavLink exact style={navLinkStyles} to="/" activeClassName="active">
      Home
    </NavLink>
    <NavLink style={navLinkStyles} to="/about" activeClassName="active">
      About
    </NavLink>
    <NavLink style={navLinkStyles} to="/users" activeClassName="active">
      Users
    </NavLink>
    <NavLink style={navLinkStyles} to="/products" activeClassName="active">
      Products
    </NavLink>
  </nav>
);

export default NavBar;
