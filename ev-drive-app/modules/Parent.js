import React from 'react'

// Demo for nested components and component interaction.

export default React.createClass({

    // Set initial state values.
    getInitialState: function() {
        return {parent:0,output:0,input:0};
    },

    // Function triggered on child output click. Sends new value to parent and updates other child's input with parent value.
    childOutput: function(){
        this.state.output=1;
        this.state.parent=this.state.parent+this.state.output;
        this.state.input=this.state.parent*2;
        this.setState({parent:this.state.parent,output:this.state.output,input:this.state.input});
    },

    // Function triggered on clear click. Clears child input value.
    clearInput: function(){
        this.state.input=0;
        this.setState({input:this.state.input})
    },

    // Parent Component that holds 2 child components and state.parent value.
    Parent : function(){
        return (
            <div className="container container-fluid" style={{backgroundColor:"white",borderRadius:5}}>
                     <h3>This is the Parent Component</h3>
                     <h4>This example makes use of nested functions to represent components. This can also be accomplished by different classes in different files.</h4>
                     <h4>Received Value: {this.state.output}</h4>
                     <h4>Total Value (Sent): {this.state.parent}</h4>
                     <span>{this.ChildOutput()}</span>
                     <span>{this.ChildInput()}</span>
                </div>)
    },
    
    // Output Child Component that sends values to parent.
    ChildOutput : function(){
        return(
            <div className="container container-fluid" style={{backgroundColor:"rgba(220, 220, 220, 0.90)",borderRadius:5,margin:10,padding:10}}>
                            <h4>Child Sends Output</h4>
                            <h5>This child component demonstrates sending information to the parent.</h5>
                            <h5>Child Output Value = 1</h5>
                            <button className="btn btn-warning" onClick={this.childOutput}>Send Value</button>
                </div>)
    },

    // Input Child Component that receives value from parent.
    ChildInput : function(){
        return(
            <div className="container container-fluid" style={{backgroundColor:"rgba(220, 220, 220, 0.90)",borderRadius:5,margin:10,padding:10}}>
                                <h4>Child Receives Input</h4>
                                <h5>This child component demonstrates sending information to the parent.</h5>
                                <h5>Received Total Value * 2 = {this.state.input}</h5>
                                <button className="btn btn-danger" onClick={this.clearInput}>Clear Value</button>
                </div>)
    },

    // Render View
    render() {
        return <div>
            <br/>
          <h4>
          React.js allows nested components. These components can interact each other via the passing of states and properties (props).
          </h4>
          <h4>
          React.js makes a clear distinction between states and props:
        </h4>
        <ul>
        <li>States can be updated and should only be kept as states in the components that are allowed to update them.</li>
        <li>Props should not be updated and function as a means to pass around data to components that can only read them.</li>
        </ul>
        <span>{this.Parent()}</span>
      </div>
    }
})
