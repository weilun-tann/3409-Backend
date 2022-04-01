import './App.css';
import './SelectionPage'
import SelectionPage from "./SelectionPage";
import DiabetesPage from "./DiabetesPage";
import logo from "./logo.svg";
import {BrowserRouter as Router, Route, Link, Routes, useNavigate} from "react-router-dom";
import CoronaryPage from "./CoronaryPage";

function App() {
    let navigate = useNavigate();
    return (
        <div>
            {console.log('started')}
            <div className="App-logo" >
                <img src={logo} className="logo" alt="logo" onClick={()=>navigate('/')}/>
            </div>
            <div className='App'>
                <Routes>
                    <Route exact path="/" element={<SelectionPage/>} />
                    <Route path="/diabetes" element={<DiabetesPage/>} />
                    <Route path="/coronary" element={<CoronaryPage/>} />
                </Routes>

                {/*</Router>*/}
            </div>
        </div>
    );
}

export default App;
