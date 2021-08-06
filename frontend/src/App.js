import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import {MainPage} from "./pages/MainPage";

function App() {
    return (
        <div className="App">
            <Router>
                <Switch>
                    <Route exact path="/" forcerefresh={true} component={MainPage}/>
                </Switch>
            </Router>
        </div>
    );
}

export default App;
