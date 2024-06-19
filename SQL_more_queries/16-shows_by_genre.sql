-- Lists all shows and all genres linked to that show from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column.
-- Each record displays: tv_shows.title - tv_genres.name.
-- Results are sorted in ascending order by the show title and genre name.
SELECT 
    tv_shows.title, -- Select the show title
    tv_genres.name  -- Select the genre name
FROM 
    tv_shows
    -- Perform a LEFT JOIN to include shows without genres
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title ASC, -- Sort the results in ascending order by show title
    tv_genres.name ASC; -- Sort the results in ascending order by genre name
