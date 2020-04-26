import React, {Component} from 'react';
import {getUsers} from './actions/users'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import LogIn from './components/pages/LogIn';
import Register from './components/pages/Register';
import TestRegister from './components/pages/TestRegister';

class App extends Component {
  componentDidMount() {
    console.log(this.props);
    getUsers();
  }
  
  render(){
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/register">Register</Link>
              </li>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/testregister">Register Test</Link>
              </li>
            </ul>
          </nav>

          <Switch>
            <Route path="/testregister">
              <TestRegister/>
            </Route>
            <Route path="/login">
              <LogIn/>
            </Route>
            <Route path="/register">
              <Register/>
            </Route>
            <Route path="/">
              <div>
                <h2>Home</h2>
              </div>
            </Route>
          </Switch>
        </div>
      </Router>
  );
}
}

export default App;
