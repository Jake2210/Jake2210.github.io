<!DOCTYPE html>
<html>
<head>
  .gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 10px;
}

.gallery img {
  width: 100%;
  height: auto;
}
  <title>My GitHub Page</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <header>
    <h1>Welcome to My GitHub Page!</h1>
  </header>

  <nav>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
  </nav>

  <main>
    <h2>Home</h2>
    <div class="gallery">
      <img src="image1.jpg" alt="Image 1">
      <img src="image2.jpg" alt="Image 2">
      <img src="image3.jpg" alt="Image 3">
      <img src="image4.jpg" alt="Image 4">
    </div>
  </main>

  <footer>
    <p>&copy; 2023 My GitHub Page. All rights reserved.</p>
  </footer>
</body>
</html>
