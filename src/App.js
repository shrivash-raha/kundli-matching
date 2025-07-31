import { useState } from "react";
import InputForm from "./components/InputForm";
import axios from "axios";

function App() {
  const [submittedData, setSubmittedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFormSubmit = async (data) => {
    setSubmittedData(data);
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post("http://150.230.142.32:5001/api/match", data);
      setResult(response.data);
    } catch (err) {
      setError("Something went wrong. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Kundli Matching</h1>
      <InputForm onSubmit={handleFormSubmit} />

      {loading && <p>Loading... Please wait.</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div>
          <h2>Match Result</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
