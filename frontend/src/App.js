import "./App.css";

function App() {
  return (
    <main class="container">
      <textarea
        class="textarea__consult white"
        placeholder="Texto de la consulta"
      ></textarea>
      <div class="container__block">
        <input class="white" placeholder="Tok K" />
        <button type="submit" class="white">
          Buscar
        </button>
      </div>
      <div class="container__block">
        <div class="container__top python">
          <h2>TopK - Python</h2>
          <div class="container__top-consult white"></div>
          <h3>Tiempo:</h3>
        </div>
        <div class="container__top postgresql">
          <h2>TopK - PostgreSQL</h2>
          <div class="container__top-consult white"></div>
          <div class="time">
            <h3>Tiempo:</h3>
          </div>
        </div>
      </div>
    </main>
  );
}

export default App;
