import React, { useState, useEffect } from "react";
import "./App.css";

export const App = ({}) => {
  const initialFormData = Object.freeze({
    consult: "",
    topk: "",
  });
  const [formData, updateFormData] = React.useState(initialFormData);
  const handleChange = (e) => {
    updateFormData({
      ...formData,

      // Trimming any whitespace
      [e.target.name]: e.target.value.trim(),
    });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    fetch("/api/create", {
      method: "POST",
      body: JSON.stringify({
        consult: formData.consult,
        topk: formData.topk,
      }),
    });
  };

  useEffect(() => {
    fetch("/api")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => console.log(data));
  }, []);

  return (
    <main className="container">
      <input
        name="consult"
        className="textarea__consult white"
        placeholder="Texto de la consulta"
        onChange={handleChange}
      ></input>
      <div className="container__block">
        <input
          name="topk"
          className="white"
          placeholder="Tok K"
          onChange={handleChange}
        />
        <button type="submit" className="white" onClick={handleSubmit}>
          Buscar
        </button>
      </div>
      <div className="container__block">
        <div className="container__top python">
          <h2>TopK - Python</h2>
          <div className="container__top-consult white"></div>
          <h3>Tiempo:</h3>
        </div>
        <div className="container__top postgresql">
          <h2>TopK - PostgreSQL</h2>
          <div className="container__top-consult white"></div>
          <div className="time">
            <h3>Tiempo:</h3>
          </div>
        </div>
      </div>
    </main>
  );
};

export default App;
