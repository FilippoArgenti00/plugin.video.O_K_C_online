# -*- coding: utf-8 -*-

movie_genres_image = "images/genres.png"
tvshow_genres_image = "images/genres_tvshow.png"
movie_highly_rated_image = "images/highly-rated.png"
tvshow_highly_rated_image = "images/highly-rated_tvshow.png"
movie_most_popular_image = "images/most-popular.png"
tvshow_most_popular_image = "images/most-popular_tvshow.png"
movie_most_voted_image = "images/most-voted.png"
tvshow_most_voted_image = "images/most-voted_tvshow.png"
movie_image = "images/movies.png"
search_movie_image = "images/search_movie.png"
movie_search_people_image = "images/search_people.png"
tvshow_search_people_image = "images/search_people_tvshow.png"
search_tvshow_image = "images/search_tvshow.png"
tvshow_image = "images/tvshows.png"
movie_years_image = "images/years.png"
tvshow_years_image = "images/years_tvshow.png"
next_image = "images/next.png"
movieDB_api_key = "8804be4f30f706e9e0ec40c32d961635"

menu_items = [
	("[B][COLOR lime]Film[/COLOR][/B]", movie_image),
	("[B][COLOR lime]Serie TV[/COLOR][/B]", tvshow_image),
]

film_menu_items = [
	("[B][COLOR lime]Ricerca film[/COLOR][/B]", search_movie_image),
	("[B][COLOR lime]Ricerca persona film[/COLOR][/B]", movie_search_people_image),
	("[B][COLOR lime]Film i piu popolari[/COLOR][/B]", movie_most_popular_image),
# -*- coding: utf-8 -*-

movie_genres_image = "images/genres.png"
tvshow_genres_image = "images/genres_tvshow.png"
movie_highly_rated_image = "images/highly-rated.png"
tvshow_highly_rated_image = "images/highly-rated_tvshow.png"
movie_most_popular_image = "images/most-popular.png"
tvshow_most_popular_image = "images/most-popular_tvshow.png"
movie_most_voted_image = "images/most-voted.png"
tvshow_most_voted_image = "images/most-voted_tvshow.png"
movie_image = "images/movies.png"
search_movie_image = "images/search_movie.png"
movie_search_people_image = "images/search_people.png"
tvshow_search_people_image = "images/search_people_tvshow.png"
search_tvshow_image = "images/search_tvshow.png"
tvshow_image = "images/tvshows.png"
movie_years_image = "images/years.png"
tvshow_years_image = "images/years_tvshow.png"
next_image = "images/next.png"
movieDB_api_key = "8804be4f30f706e9e0ec40c32d961635"

menu_items = [
	("[B][COLOR aqua]Film[/COLOR][/B]", movie_image),
	("[B][COLOR gold]Serie TV[/COLOR][/B]", tvshow_image),
]

film_menu_items = [
	("[B][COLOR red]Ricerca film[/COLOR][/B]", search_movie_image),
	("[B][COLOR blue]Ricerca persona film[/COLOR][/B]", movie_search_people_image),
	("[B][COLOR grey]Film i piu popolari[/COLOR][/B]", movie_most_popular_image),
	("[B][COLOR orange]Film i piu votati[/COLOR][/B]", movie_most_voted_image),
	("[B][COLOR aqua]Film Altamente valutati[/COLOR][/B]", movie_highly_rated_image),
	("[B][COLOR white]Film dell'anno[/COLOR][/B]", movie_years_image),
	("[B][COLOR green]Film per genere[/COLOR][/B]", movie_genres_image)
]

tvshow_menu_items = [
	("[B][COLOR gold]Ricerca serie TV[/COLOR][/B]", search_tvshow_image),
	("[B][COLOR aqua]Ricerca persona serie TV[/COLOR][/B]", tvshow_search_people_image),
	("[B][COLOR red]Serie TV famosi[/COLOR][/B]", tvshow_most_popular_image),
	("[B][COLOR grey]Serie TV le piu votate[/COLOR][/B]", tvshow_most_voted_image),
	("[B][COLOR lime]Serie TV Altamente valutate[/COLOR][/B]", tvshow_highly_rated_image),
	("[B][COLOR orange]Serie TV dell'anno[/COLOR][/B]", tvshow_years_image),
	("[B][COLOR white]Serie TV per genere[/COLOR][/B]", tvshow_genres_image)
]

messages = {
	"start_search": {
		"title": "[B][COLOR aqua]In Lavorazione[/COLOR][/B]",
		"text": "[B][COLOR gold]Inizio ricerca...[/COLOR][/B]"
	},

	"movie": {
		"popular": "[B][COLOR red]Ricerca film famosi in corso...[/COLOR][/B]",
		"top_rated": "[B][COLOR aqua]Ricerca film più votati in corso...[/COLOR][/B]",
		"discover": "[B][COLOR lime]Sto scoprendo nuovi film...[/COLOR][/B]",
		"genre": "[B][COLOR blue]Ricerca film per genere in corso...[/COLOR][/B]",
		"year": "[B][COLOR orange]Ricerca film per anno in corso...[/COLOR][/B]",
		"default": "[B][COLOR grey]Sto cercando film con questo titolo[/COLOR][/B]"
	},

	"tvshow": {
		"popular": "[B][COLOR aqua]Ricerca serie tv famosi in corso...[/COLOR][/B]",
		"top_rated": "[B][COLOR gold]Ricerca serie tv più votati in corso...[/COLOR][/B]",
		"discover": "[B][COLOR red]Sto scoprendo nuove serie tv...[/COLOR][/B]",
		"genre": "[B][COLOR white]Ricerca serie tv per genere in corso...[/COLOR][/B]",
		"year": "[B][COLOR orange]Ricerca serie tv per anno in corso...[/COLOR][/B]",
		"default": "[B][COLOR lime]Sto cercando serie tv con questo titolo[/COLOR][/B]"
	},

	"stream": {
		"error_stream_title": "[B][COLOR red]ERRORE TITOLO STREAM[/COLOR][/B]",
		"error_stream_text": "[B][COLOR red]ERRORE TESTO STREAM[/COLOR][/B]"
	},

	"person": "[B][COLOR orange]Persone[/COLOR][/B]",
	"movie_list": "[B][COLOR lime]Lista Film[/COLOR][/B]",
	"tvshow_list": "[B][COLOR red]Lista Serie Tv[/COLOR][/B]",
	"episode": "[B][COLOR aqua]episodi[/COLOR][/B]",
	"playing": "[B][COLOR green]buona visione[/COLOR][/B]"
}
