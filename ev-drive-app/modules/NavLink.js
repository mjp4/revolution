// modules/NavLink.js
import React from 'react'
import { Link } from 'react-router'

// Defines what gets rendered from a <NavLink/> element.
export default React.createClass({
  render() {
    return <Link {...this.props} activeClassName="active"/>
  }
})
