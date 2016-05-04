<?php ?>
<html lang="en">
<head>
  <meta charset="utf-8"> <!--setting forth charcter type -->
  <title>JofD Corpus</title> <!--title (this will be on the tab on the browser) -->
  <meta name="description" content="Journal of Discources"> <!--From what I understand this would help someone search this page -->

      <!-- Adding bootstrap to the file -->
      <!-- Latest compiled and minified CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
      <!-- Optional theme -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
</head>

  <!--This styling affects the navbar-->
  <style>
  body{
    padding-top:40px;
  }
  </style>
<!--beginnning of the body -->

<body>
  <!-- Navbar, navbar-inverse makes it black, navbar fixed top makes it stay at as you scroll-->
  <nav class="navbar navbar-inverse navbar-fixed-top" id="my-navbar">
    <div class="container"> <!--beginning of container -->
      <div class="navbar-header">
        <!--What this does is when you put the screen as smaller it does the thing in the corner, making it more compatible with other devices -->
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <!--put website-->
        <a href="http://jod.mrm.org/1" class="navbar-brand">JofD</a>
      </div> <!-- Ending of Navbar Header -->

      <!--Make sure the you identify the id matches what you want-->
      <div class="collapse navbar-collapse" id="navbar-collapse">

      <a href="http://104.236.83.120/jofd/Volume.txt" target="_blank" class="btn btn-warning navbar-btn navbar-right">Download JofD</a>

        <!--creating list of all the different links in the top bar -->
        <ul class="nav navbar-nav">
            <li><a href="#quotes">Quotes</a>
            <li><a href="#gallery">Gallery</a>
        </ul>
      </div>
    </div><!--End of Container -->
  </nav><!--End of Nabvar-->

  <!-- Creating the Jumpbotron-->
  <div class="jumbotron">
      <div class="container text-center">
      <!--Adding style -->
      <style>
        h1 {
          font-family: courier;
        }
      </style>

      <!--this will be the main header of the website -->
      <h1>Journal of Discourses</h1>
        <p>Ever wanted to search early-Church conference talks? Here's your chance.</p>

      <div class="btn-group"> <!--these are some other tabs that can be added-->
        <a href="https://www.lds.org/topics/journal-of-discourses?lang=eng" class="btn btn-lg btn-warning">Official Church Statement</a>
        <a href="http://pythex.org/" class="btn btn-lg btn-default">Regex Practice</a>
        <a href="https://archive.org/" class="btn btn-lg btn-warning">Other Documents</a>
      </div><!--End of btn-group-->
    </div><!--Close container-->
    <!--call to action-->

          <div class="containter text-center ">
            <!--description of this part of the page -->
            <h3>Search the Journal of Discoures</h3>
            <p>Enter your regular expression</p>
            <!--setting this forth as a 'post'. The php code will look for this post, so don't mess this up!-->
            <!--Below is all of the design concerning the enduser interaction.-->
            <form action="index.php" method="post" class = "form-inline">
              <div class="form-group">
                <label for="search_regex">Search</label>
                <input type="text" name="search_regex" class="form-control" id="search_regex" placeholder="Your Search">
              </div>
              <button type="submit" class="btn btn-warning">Search</button>
              <hr>
            </form>
            <!--end of enduser interaction design-->
            <p><?php
            //This is php code. Make sure that you don't type html here without quotaiton marks.
            $length = strlen($_POST['search_regex']); //checking to see if the HTML has POSTed anything
            if ($length != 0){ //Checking length of code. Just in case the page is refereshed without enduser interaction
              $criteria = $_POST['search_regex']; //defining the criteria needed
              echo shell_exec("python script.py $criteria"); //this sends the code to the script.py Make
            }

            ?></p>
          </div> <!--end of container-->

  </div><!--end of jumptotron-->



    <div class="container">
    <section>
      <div class="page-header" id="quotes">
        <h2>quotes.<small> Therefore whoever read that understand, for the Spirit manifests the truth;
          <br><br> - Doctrine and Covenants 91:4-5</small><h2>
      </div>
      <div class="row">
        <!--needs to add up to twelve. ie. 4 x3-->
        <div class="col-lg-4">
          <blockquote>
              <p>The nations do not know anything about the blessings of Abraham;.. they do not know what is in the future,
                nor what blessings they are depriving themselves of, because of the traditions of their fathers;
                 they do not know that a man's posterity, in the eternal worlds, are to constitute his glory,
                  his kingdom, and dominion.
               </p>
            <footer>Orson Pratt</footer>
          </blockquote>
        </div>
        <div class="col-lg-4">
          <blockquote>
              <p>Is there anything that passes with the children of men that the Lord does not control to his glory?
                 That is what the Lord wants every man and woman to understand. If there is good, the Lord is there to dictate it.
                  If there is power, has he not power over all the power there is upon the face of the earth? If there is evil,
                  if there is sorrow, if there is trouble, if there are trials for his people, is he not there to dictate those
                  sorrows and troubles?</p>
            <footer>Brigham Young</footer>
          </blockquote>
        </div>
        <div class="col-lg-4">
          <blockquote>
              <p>He [Abraham] therefore was necessitated to come up by degrees, receive an experience, be tried and proved. And when he had been
                 sufficiently proved according to the flesh, the Lord manifested to him the election before exercised towards
                 him in the eternal world. He then renewed that election and covenant, and blessed him, and his seed after him.  </p>
            <footer>Parley P. Pratt</footer>
          </blockquote>
        </div>
      </div><!--End of row-->
  </div><!--End of Container-->

  <!--Gallery-->
  <div class="container">
    <section>
      <div class="page-header" id="gallery">
        <h2>Gallery. <small> Mormon's Heritage </small><h2>
      </div>

      <div class="carousel slide" id="screenshot-carousel" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#screenshot-carousel" data-silde-to="0" class="active"></li>
          <li data-target="#screenshot-carousel" data-silde-to="1"></li>
          <li data-target="#screenshot-carousel" data-silde-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="item active">
            <img src="young-brothers-big.jpg" height="900" width="1200" >
            <div class="carousel-caption">
              <h3>Young Brothers</h3>
            </div>
          </div>
          <div class="item">
            <img src="tabernacle.jpg" height="900" width="1200" >
            <div class="carousel-caption">
              <h3>Mormon Tabernacle</h3> <!--creating header-->
            </div>
          </div>
          <div class="item">
            <img src="crossing.jpg" height="900" width="1200">
            <div class="carousel-caption">
              <h3>Exodus to SLC</h3>
            </div>
          </div>
        </div><!--end of inner-->
        <!--Adding the arrows -->
        <a href="#screenshot-carousel" class="left carousel-control" data-slide="prev">
          <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a href="#screenshot-carousel" class="right carousel-control" data-slide="next">
          <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
      </div> <!--end of carousel-->
    </section>
  </div>

  <script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
</body>

</html>
