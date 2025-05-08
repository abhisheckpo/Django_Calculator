import React, { useState } from "react";

const Calculator = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [operation, setOperation] = useState("+");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [latestRecord, setLatestRecord] = useState(null);

  const calculate = async () => {
    setError("");
    setLatestRecord(null); // Clear previous latest record

    try {
      const response = await fetch("http://localhost:8000/api/calculate/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ num1, num2, operation }),
      });

      const data = await response.json();
      if (data.error) {
        setError(data.error);
        setResult(null);
      } else {
        setResult(data.result);
      }
    } catch (err) {
      setError("Server error");
    }
  };

  const fetchLatestRecord = async () => {
    setError("");
    setResult(null); // Clear current result

    try {
      const response = await fetch("http://localhost:8000/api/latest/");
      const data = await response.json();

      if (data.error) {
        setLatestRecord(null);
        setError(data.error);
      } else {
        setLatestRecord(data);
      }
    } catch (err) {
      setError("Error fetching latest record");
    }
  };

  return (
    <div>
      <input
        type="number"
        value={num1}
        onChange={(e) => setNum1(Number(e.target.value))}
        placeholder="Enter first number"
      />
      <select value={operation} onChange={(e) => setOperation(e.target.value)}>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input
        type="number"
        value={num2}
        onChange={(e) => setNum2(Number(e.target.value))}
        placeholder="Enter second number"
      />
      <button onClick={calculate}>Calculate</button>
      <button onClick={fetchLatestRecord} style={{ marginLeft: "10px" }}>
        Fetch Latest Calculation
      </button>

      {error && <h3 style={{ color: "red" }}>{error}</h3>}
      {result !== null && !error && <h3>Result: {result}</h3>}

      {latestRecord && (
        <div style={{ marginTop: "20px" }}>
          <h3>Latest Record:</h3>
          <p>
            {latestRecord.num1} {latestRecord.operation} {latestRecord.num2} ={" "}
            {latestRecord.result}
          </p>
        </div>
      )}
    </div>
  );
};

export default Calculator;
