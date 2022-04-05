import './App.css';
import './SelectionPage'
import logo from "./logo.png";
import {BrowserRouter as Router, Route, Link, Routes, useNavigate, useLocation, Switch} from "react-router-dom";
import SelectionPage from "./SelectionPage";
import DiabetesPage from "./DiabetesPage";
import CoronaryPage from "./CoronaryPage";
import CataractsPage from "./CataractsPage"
import PneumoniaPage from "./PneumoniaPage";
import StrokePage from "./StrokePage";
import ResultsPage from "./ResultsPage";
import {TransitionGroup, CSSTransition, SwitchTransition} from "react-transition-group";

function App() {
    let navigate = useNavigate();
    let location = useLocation();
    return (
        <div className='hideScroll'>
            <div className="App-logo" >
                <img src={logo} className="logo" alt="logo" onClick={()=>navigate('/')}/>
            </div>
            <div className='App'>
                <SwitchTransition>
                    <CSSTransition
                        key={location.pathname}
                        classNames="transition"
                        timeout={500}
                    >
                        <Routes location={location}>
                            <Route exact path="/" element={<SelectionPage/>} />
                            <Route path="/diabetes" element={<DiabetesPage/>} />
                            <Route path="/stroke" element={<StrokePage/>} />
                            <Route path="/coronary" element={<CoronaryPage/>} />
                            <Route path="/cataracts" element={<CataractsPage/>} />
                            <Route path="/pneumonia" element={<PneumoniaPage/>} />
                            <Route path="/results" element={<ResultsPage/>} />
                            {/*<Route path="/imageUploader"  />*/}
                        </Routes>
                    </CSSTransition>
                </SwitchTransition>


                {/*</Router>*/}
            </div>
        </div>
    );
}

export default App;
