import React from 'react'

export default React.createClass({

    // Define initial value of state used for input field (empty string).
    getInitialState: function() {
        return {value: ''};
    },

    // Define function to update state of input value upon each change in the input field
    handleChange: function(event) {
        this.setState({value: event.target.value});
    },

    render() {
        return <div>
            <br />
            <h4>
                React.js 2-way binding ties the entered value to an underlying state. 
            </h4>
            <h4>
                This allows users to view a property as well as make changes to it. 

                This is commonly used in input fields, as seen in the example below:
        </h4>
        <br/>
        <div className="input-group input-group-lg">
            <span className="input-group-addon" style={{fontWeight:'bold',fontSize:30}}>Input 1</span>
            <input
            style={{textAlign:'center',fontSize:30,height:100}}
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
            placeholder="Enter something here"
          />
        </div>
        <br/>
        <div className="input-group input-group-lg">
            <span className="input-group-addon" style={{fontWeight:'bold',fontSize:30}}>Input 2</span>
            <input
            style={{textAlign:'center',fontSize:30,height:100}}
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
            placeholder="It will appear here"
          />
        </div>
        <br/>
        <h4><strong>Underlying property value: {this.state.value}</strong>
        </h4>
        <br/>
        <h4>
        These inputs are tied to the same underlying value and will mirror the same displayed value.
        </h4>
        <h4>
        The value can be overwritten from both input fields.
        </h4>
        </div>
    }
})
