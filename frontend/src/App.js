import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import {MainPage} from "./pages/MainPage";
import {LoginPage} from "./pages/LoginPage";

function App() {
    return (
        <div className="App">
            <Router>
                <Switch>
                    <Route exact path="/" forcerefresh={true} component={MainPage}/>
                    <Route path="/login" component={LoginPage}/>
                </Switch>
            </Router>
        </div>
    );
}

export default App;
