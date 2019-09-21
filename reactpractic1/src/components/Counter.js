import React from 'react'

export default class Counter extends React.Component {
        
    constructor(props) {
          super(props);
          this.state = {
            count: 0
          };
        }

        a() { this.setState({ count: this.state.count + 1 }) }
        b(){ this.setState({ count : this.state.count - 1})  }
        c(){ this.setState({ count : 0})  }

        render() {
          return (
         <div>
          <button onClick = {(e) => this.a(e)}>+</button>
          <button onClick = {(e) => this.b(e)}>+</button>
          <button onClick = {(e) => this.c(e)}>@</button>
          <h1>{this.state.count}</h1>
        </div>
          );
        }
          
}


