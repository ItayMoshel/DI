const allBooks = [
    {
      title: "Harry Potter",
      author: "J.K. Rowling",
      image: "https://example.com/harry_potter.jpg",
      alreadyRead: true
    },
    {
      title: "The Hobbit",
      author: "J.R.R. Tolkien",
      image: "https://example.com/the_hobbit.jpg",
      alreadyRead: false
    }
  ];
  
  const listBooksSection = document.querySelector(".listBooks");
  
  for (const book of allBooks) {
    const bookDiv = document.createElement("div");
    bookDiv.classList.add("book");
  
    const bookTitle = document.createElement("p");
    bookTitle.textContent = `${book.title} written by ${book.author}`;
    bookDiv.appendChild(bookTitle);
  
    const bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.style.width = "100px";
    bookDiv.appendChild(bookImage);
  
    if (book.alreadyRead) {
      bookTitle.style.color = "red";
    }
  
    listBooksSection.appendChild(bookDiv);
  }
  