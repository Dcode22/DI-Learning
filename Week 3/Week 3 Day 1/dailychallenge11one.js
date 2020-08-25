var allBooks = {
book1: {
	title: "Harry Potter",
	author: "J. K. Rowling",
	image: "https://d1w7fb2mkkr3kw.cloudfront.net/assets/images/book/lrg/9780/5903/9780590353427.jpg",
	alreadyRead: true,
},
book2: { 
	title: "Notes From Underground",
  author: "Fyodor Dostoyevsky",
  image: "https://m.media-amazon.com/images/I/51+iWhNRmYL._SX35_.jpg",
  alreadyRead: true,
}}

  var bdy = document.getElementsByTagName("body")[0];
  var tbl = document.createElement("div");
  tbl.style.display = "flex";
  tbl.style.backgroundColor = "blue";
  bdy.appendChild(tbl);
  tbl.style.width = "70%";
  tbl.style.justifyContent = "center";
  tbl.style.margin = "auto";
  

 for (let key in allBooks) {
 	book = document.createElement("div");
 	book.innerHTML = "<h1>"+allBooks[key].title+"</h1>"+"<br>"+"<p> written by "+allBooks[key].author+"</p>" + "<br> <img style = 'width: 100px' src='"+allBooks[key].image+"'</img>"
 	book.style.border = "3px solid green";
 	book.style.margin = "5px";
 	book.style.textAlign = "center";
 	tbl.appendChild(book);
	if (allBooks[key].alreadyRead === true) {
		book.style.backgroundColor = "red";
	}
	
 }
  
