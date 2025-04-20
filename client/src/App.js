import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from './Register';
import Login from './Login';
import Dashboard from './Dashboard';
import Detect from "./Detect";
import Convert from './Convert';
import HistoryPage from './HistoryPage';
import ImageToText from './ImageToText';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/detect" element={<Detect />} />
        <Route path="/convert" element={<Convert />} />
        <Route path="/history" element={<HistoryPage />} />
        <Route path="/image-to-text" element={<ImageToText />} />

      </Routes>
    </Router>
  );
}

export default App;
