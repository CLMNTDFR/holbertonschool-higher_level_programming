-- Lists all shows from hbtn_0d_tvshows along with their genre IDs or NULL if no genre is linked
-- The output should be ordered by the shows title and genre ID
-- The tv_show_genres table has (show_id, genre_id)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
