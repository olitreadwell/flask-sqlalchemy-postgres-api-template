import { Route, Switch } from "react-router-dom";

import About from "../About";
import Home from "../Home";

const Routes = () => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/about" component={About} />
  </Switch>
);

export default Routes;
