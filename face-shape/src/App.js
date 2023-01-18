import logo from './logo.svg';
import './App.css';
import Result from './components/Result';

function App() {
  var faceShape = "heart";
  var recommendation = {'triangle': ['rectangle', 'browline', 'oval', 'aviators', 'geometric', 'wrap'],
                  'heart' : ['rectangle', 'aviators', 'geometric', 'wrap'],
                  'diamond' : ['oval', 'aviators', 'round', 'wrap'],
                  'round' : ['rectangle', 'square', 'aviators', 'wrap'],
                  'oblong' : ['classic wayframe', 'browline', 'oval', 'aviators', 'round', 'geometric', 'wrap'],
                  'oval' : ['rectangle', 'square', 'classic wayframe', 'browline', 'aviators', 'geometric', 'wrap'],
                  'square' : ['classic wayframe', 'browline', 'oval', 'aviators', 'round', 'wrap']
                  }
  const specs = recommendation[faceShape];
  const list = [];

  specs.forEach((spec) => {
    list.push(<Result type={spec}></Result>)
  })
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Your face shape is {faceShape}.
          <br /> The frames recommended for your face shape are...
          {list}
        </p>
      </header>
    </div>
  );
}

export default App;
