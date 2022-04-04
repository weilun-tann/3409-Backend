import './App.css';
import './SelectionPage'
import logo from "./logo.png";
import {BrowserRouter as Router, Route, Link, Routes, useNavigate} from "react-router-dom";
import SelectionPage from "./SelectionPage";
import DiabetesPage from "./DiabetesPage";
import CoronaryPage from "./CoronaryPage";
import CataractsPage from "./CataractsPage"
import PneumoniaPage from "./PneumoniaPage";
import StrokePage from "./StrokePage";
import ResultsPage from "./ResultsPage";

function App() {
    let navigate = useNavigate();
    return (
        <div>
            <div className="App-logo" >
                <img src={logo} className="logo" alt="logo" onClick={()=>navigate('/')}/>
            </div>
            <div className='App'>
                <Routes>
                    <Route exact path="/" element={<SelectionPage/>} />
                    <Route path="/diabetes" element={<DiabetesPage/>} />
                    <Route path="/stroke" element={<StrokePage/>} />
                    <Route path="/coronary" element={<CoronaryPage/>} />
                    <Route path="/cataracts" element={<CataractsPage/>} />
                    <Route path="/pneumonia" element={<PneumoniaPage/>} />
                    <Route path="/results" element={<ResultsPage/>} />
                    {/*<Route path="/imageUploader"  />*/}
                </Routes>

                {/*</Router>*/}
            </div>
        </div>
    );
}

export default App;
