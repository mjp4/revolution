import React from 'react'
import NavLink from './NavLink'
import Hello from './Hello'
import { CSSTransitionGroup } from 'react-transition-group'
import Transition from 'react-motion-ui-pack'
import { spring } from 'react-motion'
import axios from 'axios'
import Revolution from 'revolution'


// Top-level App Component that holds router links and holds relevant route view.

export default React.createClass({
    // Set initial state values.
    getInitialState: function () {
        this.chargers = [
            { lat: 1, long: 5 },
            { lat: 2, long: 4 },
            { lat: 3, long: 3 },
            { lat: 4, long: 2 },
            { lat: 5, long: 1 }]
            ;
        return { state: 0, secondsElapsed: 0, api: new Revolution.AllApi(), username: "mark@perryman.org.uk", password: "password", to:"Edinburgh"};
    },
    nextState: function(){
        this.state.state++;
        this.setState({state:this.state.state});
    },
    tick: function () {
        this.setState({ secondsElapsed: this.state.secondsElapsed + 1 });

        if (this.state.secondsElapsed == 5) {
            this.state.secondsElapsed = 0
            axios.get('/distance', {
                param: 'mock'
            })
                .then(function (response) {
                    this.chargers = response;
                })
                .catch(function (error) {
                    console.log(error);
                });
        };
    },
    callback: function (error,data,response) {
        if (error) {
            console.error(error);
        } else {
            console.log('API called successfully. Returned data: ' + data);
        }
    },
    componentDidMount: function () {
        this.interval = setInterval(this.tick, 1000);
    },
    getChargers: function() {
        this.api.allInfo(this.state.username, this.state.password, this.callback(error, data, response));
        return this.callback.data;
    },


    Stage1 : function(){
        return (  <div>
                 <Transition
                    enter={{ opacity: 1, translateY: spring(0, { stiffness: 30, damping: 10 }) }}
                    leave={{ opacity: 0, translateY: 100 }}
                    component={false}
                    >
        {this.state.state==0 && <div key="button">
                <span>{this.Button()}</span> </div>}
                </Transition>
                <Transition
                enter={{ opacity: 0, translateY: spring(0, { stiffness: 30, damping: 10 }) }}
                leave={{ opacity: 0, translateY: 100 }}
                component={false}
                >
                {this.state.state==1 && <div key="button"> </div>}
            </Transition></div>
            ) 
    },
    Stage2: function () {
        return (<div>
            <Transition
                enter={{ opacity: 1, translateY: spring(0, { stiffness: 30, damping: 10 }) }}
                leave={{ opacity: 0, translateY: 100 }}
                component={false}
            >
                {this.state.state == 1 && <div key="button">
                    <span>{this.List()}</span> </div>}
            </Transition>
            <Transition
                enter={{ opacity: 1, translateY: spring(0, { stiffness: 30, damping: 10 }) }}
                leave={{ opacity: 0, translateY: 100 }}
                component={false}
            >
                {this.state.state == 2 && <div key="button">
                    <span style={{ zIndex: 10 }}>{this.List()}</span> </div>}
            </Transition></div>
        )
    },
    
        Button : function(){
            return ( <div>
                <h3 style={{ textAlign: 'center' }}>{this.password}{this.state.secondsElapsed}</h3>
                <form style={{ textAlign: 'center' }}>
                    <label>
                        Destination: 
                   <input type="text" value={this.state.to} />
                    </label>
                </form>
                <button className="btn btn-success" onClick={() => { this.nextState.bind(); this.getChargers() }} style={{margin:'auto', display:'block', marginTop:'5%'}}>GO</button>

        </div>  ) 
        },

        // Input Child Component that receives value from parent.
        ChildInput : function(){
            return(
                <div >  </div>)
    },

    List: function () {
        return (<div style={{ textAlign: 'center' , contentAlign:'center'}}>
            <h3 >List placeholder</h3>
                {this.chargers.map(function (listValue) {
                return (<div className="container" style={{
                    backgroundColor: listValue.lat > 3 ? 'pink' : 'lightgreen', borderRadius: '5px', padding:'5px', marginTop:'5px', width: '600px' }}>
                    <div style={{ width: '65%', padding: '5px' , float:'left' , textAlign:'left'}}><div style={{ padding: '5px' }}>Charger: {listValue.lat}</div><div style={{ padding: '5px' }}>Network: {listValue.long}</div></div>
                    <div style={{padding: '5px' }}><div>Distance: {listValue.lat}</div><div>Extra Time: {listValue.long}</div></div>
                        </div>);
                })}
            </div>
            )
    },

    render() {


        return (
            <div style={{ padding: '-10%'}}>
            
            <div className="container" style={{backgroundColor:'white', width:'110%', padding:0}}>
             <div className="container" style={{backgroundColor:'#0E3961',color: 'white', width:'110%',margin:0}}>
                        <h4 >&nbsp;&nbsp; rEVolution</h4></div>
            </div>
                
                {this.Stage1()}
                {this.Stage2()}
            </div>

            
             )
         }
})
