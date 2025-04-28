import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import PredictionForm from "./PredictionForm";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PredictionForm />} />
      </Routes>
    </Router>
  );
}

export default App;
