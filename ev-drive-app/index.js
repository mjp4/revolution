import React from 'react'
import { render } from 'react-dom'
import { Router, Route, hashHistory } from 'react-router'
import App from './modules/App'
import Hello from './modules/Hello'
import ForIf from './modules/ForIf'
import Input from './modules/Input'
import Parent from './modules/Parent'
import Routing from './modules/Routing'

render((
  <Router history={hashHistory}>
    <Route path="/" component={App}>
      <Route path="/forIf" component={ForIf}/>
      <Route path="/hello" component={Hello}/>
      <Route path="/input" component={Input}/>
      <Route path="/parent" component={Parent}/>
      <Route path="/routing" component={Routing}/>
    </Route>
  </Router>
), document.getElementById('app'))
