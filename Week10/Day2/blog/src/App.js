import Actor from './Actor';

const App = () => {
  const listActors = [
    {
      id: 1,
      firstName: "Al",
      lastName: "Pacino",
      imageUrl: "https://pyxis.nymag.com/v1/imgs/bc9/ccb/936534d0b82b77cf0ffbac92010ee38ea3-06-al-pacino.2x.rvertical.w512.jpg",
    },
    {
      id: 2,
      firstName: "Robert",
      lastName: "De Niro",
      imageUrl: "https://m.media-amazon.com/images/M/MV5BMjAwNDU3MzcyOV5BMl5BanBnXkFtZTcwMjc0MTIxMw@@._V1_FMjpg_UX1000_.jpg",
    },
    {
      id: 3,
      firstName: "Joe",
      lastName: "Pesci",
      imageUrl: "https://americadomani.com/wp-content/uploads/2023/06/062223_joe-pesci_article-scaled.jpg",
    },
  ]

  return (
    <div className='box'>
      <h1>This is App.js</h1>
      <Actor actors={listActors}/>
    </div>
  );
};

export default App;