import React from 'react';
import './Actor.css';

const liStyl = {
   border: '1px solid black',
   backgroundColor: '#f2f2f2'
 };

const Actor = (props) => {
   return (
      <div className='card'>
         {props.actors.map(actor => (
            <ul key={actor.id}>
               <h2 className='title'><li style={liStyl}>First name: {actor.firstName}</li></h2>
               <li style={liStyl}>Last name: {actor.lastName}</li>
               <li style={liStyl}><img src={actor.imageUrl} alt={`${actor.firstName} ${actor.lastName}`} style={{ width: '225px', height: '275px' }} /></li>
            </ul>
         ))}
      </div>
   );

}

export default Actor;