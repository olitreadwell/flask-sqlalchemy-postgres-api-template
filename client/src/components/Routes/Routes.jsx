import { Route, Switch } from "react-router-dom";

import About from "../About";
import Home from "../Home";
import Users from "../Users";
import Products from "../Products";

const Routes = () => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/about" component={About} />
    <Route exact path="/users" component={Users} />
    <Route exact path="/products" component={Products} />
  </Switch>
);

export default Routes;
