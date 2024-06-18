-- Select shows and their associated genre IDs
-- The output should be ordered by the shows title and genre ID
-- The tv_show_genres table has (show_id, genre_id)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
