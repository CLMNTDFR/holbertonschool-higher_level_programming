-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- This query joins the tv_shows, tv_show_genres, and tv_genres tables to find and list
-- all shows associated with the genre "Comedy".
SELECT 
    tv_shows.title -- Select the show title
FROM 
    tv_shows
    -- Join the tv_show_genres table with the tv_shows table on the show_id
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Join the tv_show_genres table with the tv_genres table on the genre_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE 
    tv_genres.name = 'Comedy' -- Filter the results to include only the genre named "Comedy"
ORDER BY 
    tv_shows.title ASC; -- Sort the results in ascending order by the show title
