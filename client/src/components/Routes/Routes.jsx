import { Route, Switch } from "react-router-dom";

import About from "../About";
import Home from "../Home";
import UserList from "../UserList";
import ProductList from "../ProductList";

const Routes = () => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/about" component={About} />
    <Route exact path="/users" component={UserList} />
    <Route exact path="/products" component={ProductList} />
  </Switch>
);

export default Routes;
