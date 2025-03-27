import React, { useState } from "react";

const Sum = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [sum, setSum] = useState(null);

  const calculateSum = async () => {
    const response = await fetch("http://localhost:8000/api/sum/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ num1, num2 }),
    });
    const data = await response.json();
    setSum(data.sum);
  };

  return (
    <div>
      <h2>Sum of Two Numbers</h2>
      <input 
        type="number" 
        value={num1} 
        onChange={(e) => setNum1(Number(e.target.value))} 
        placeholder="Enter first number"
      />
      <input 
        type="number" 
        value={num2} 
        onChange={(e) => setNum2(Number(e.target.value))} 
        placeholder="Enter second number"
      />
      <button onClick={calculateSum}>Calculate Sum</button>
      {sum !== null && <h3>Sum: {sum}</h3>}
    </div>
  );
};

export default Sum;
