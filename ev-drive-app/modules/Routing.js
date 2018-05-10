import React from 'react'

// Extra info on routing.

export default React.createClass({

    render() {
        var message = "The navigation bar and router links were implemented with the use of a separate library called react-router.";
        return <div>
            <br/>
          <h4>
          {message}
          </h4>
            <br/>
            <h4>
            <a target="_blank" href="https://github.com/reactjs/react-router">More info.</a>
            </h4>
          </div>
    }
})
