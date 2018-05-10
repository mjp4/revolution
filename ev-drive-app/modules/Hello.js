import React from 'react'
import { CSSTransitionGroup } from 'react-transition-group'

// Demo for simple component with one-way property binding.

export default React.createClass({

    render() {
        // Define message value to be referred to by property binding
        var message = "Hello World!";

        return <div>
            <h3 style={{textAlign:'center'}}>Hit the button to get started!</h3>
        <CSSTransitionGroup
transitionName="example"
transitionAppear={true}
transitionAppearTimeout={500}
transitionEnter={false}
transitionLeave={false}>
<button className="btn btn-warning btn-go"  style={{margin:'auto', display:'block', marginTop:'5%'}}>Take a Break!!</button>
</CSSTransitionGroup>
</div>    
  }
})
