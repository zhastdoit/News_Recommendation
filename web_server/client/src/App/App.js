import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.min.js';

import React, { Component } from 'react';
import './App.css'; //Each Component can have its own css
import NewsPanel from '../NewsPanel/NewsPanel';
var logo = 'logo.png';

class App extends Component {
  render() {
    return (
      <div className="App">
        <img className='App-logo' src={logo} alt='logo'/>
        <div className='contianer'>
            <NewsPanel />
        </div>
      </div>
    );
  }
}

export default App;
