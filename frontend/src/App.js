import './App.css';
import './SelectionPage'
import SelectionPage from "./SelectionPage";
import DiabetesPage from "./DiabetesPage";
import logo from "./logo.svg";
import {BrowserRouter as Router, Route, Link, Routes} from "react-router-dom";

function App() {

  return (
    <Router>
        {console.log('started')}
        <div className="App-logo">
            <img src={logo} className="logo" alt="logo"/>
        </div>
        <div className='App'>
            <Routes>
                <Route exact path="/" element={<SelectionPage/>} />
                <Route path="/diabetes" element={<DiabetesPage/>} />
                <Route path="/topics" element={<DiabetesPage/>} />
            </Routes>

            {/*</Router>*/}
        </div>
    </Router>
  );
}

export default App;
