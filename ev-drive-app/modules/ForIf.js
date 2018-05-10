import React from 'react'

export default React.createClass({

    // Define external variables for easier referencing.
    btnArray:[],
    val:1,

    // Initialise state values that can be updated later.
    getInitialState: function() {
        return {btnArray:[],val:1};
    },

    // Function triggerred by clicking Generate button, which adds a new entry into the array that acts as the button data source.
    addButton: function() {
        this.btnArray.push(this.val);
        this.val++;
        this.setState({btnArray:this.btnArray});
    },

    // Function triggered by clicking Clear button, which empties button data array.
    clearAll : function() {
        this.btnArray=[];
        this.val = 1;
        this.setState({btnArray:this.btnArray});
    },
    
    // Function that returns a snippet of HTML / JSX if there are more than 4 elements in the button array
    ifMore: function() {
        if (this.val>4){
            return (
        <span>Clear the array and reset counter <span><button className="btn btn-danger" onClick={this.clearAll}>Clear!</button></span></span>
        )};
    },    

    render() {
        // Maps each element in the button array to a function that returns a snippet of HTML/JSX to form a button for each element in the array.
        var btnDisplay = this.state.btnArray.map(function(button){
            return (
            <div className="col-xs-3">
                <button className="btn btn-warning btn-block" style={{padding:5, marginTop:10}}>Button no.{button}</button>
            </div>
            )}
        );

      return <div>
          <br/>
          <h4>
                Generate adds new elements to an array <button onClick={this.addButton} className="btn btn-warning">Generate!</button> <br /><br />

                The array is used to populate the mock button grid below by using a JavaScript for loop<br /><br />

                The JavaScript if statement triggers if more than 4 buttons exist<br /><br />
                More than 4 buttons: {this.ifMore()}
            </h4>
            <br/>
            <span>{btnDisplay}</span>
            </div>
         }
})
