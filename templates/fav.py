<!DOCTYPE html>
<html>
<head>
	<title>FAVORITES!!!</title>
</head>
<body>
	<h1>My Fave MEmes!</h1>
<a href="/."></a>
{%for m in MEmes%}

<h2 style="text-align:center">FAVE</h2>

<div class="card">
  <img src="{{p.picture_link}}" alt="chocolate candies" style="width:100%">
  <h1>{{p.name}}</h1>
  <p class="price">{{p.price}}</p>
  <p>{{p.description}}</p>
  <p><a href="{{url_for('add_to_cart',product_id=p.id)}}"><button>Add to Cart (you better)</button
    ></a></p>
</div>

{%endfor%}
</body>
</html>