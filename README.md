Levyraati

Levyraati is a application for rating music albums.
- Registered users can add albums with their relevant information and an album cover image
- Registered users can rate and review albums added by users
- Registered users can rate individual songs on albums

Välipalautus 2.
Unfortunately I got sick, which hindered the programs development. Levyraati is not yet in Heroku.
New users can be registered, new albums can be added and viewed. Viewed albums can be sorted in different ways: date, alphapetica, artist name, album name and grade. Sort by grade doesn't workd unfortunately.
Apparently the second "Välipalautus" was yesterday. As an update I am still sick. Album cover images are displayed when viewing a specific album. 
Heroku is in working order.

Välipalautus 3.
At the moment of writing this /album doesn't work properly. It is due to some error in querying an album's information by its ID. In other ways the webpage should work as intended. Admin tools are not done.
Hopefully these get done fairly fast so that I can get to fixing known secondary bugs, polishing, adding smaller features and better visuals.

Loppupalautus
The Front page /home displays the 10 newest albums added to the site.
In /register users can register a new account and also have the option to become an admin. In /addalbum a registered user can add an album with its artist, album name, genre, year of release, a cover image and its review with grade to the site. In /album users can review and grade other users and their own albums.
In /admin as an admin a user can promote and demote other users to and from admin status. In /album an admin can hide specific songs from normal users view.
In /albums users can view all albums sorted by album name, date added, artist name and grade that, all can also be displayed in descending order.
Choosing an artist in /album takes the user to /artist where they can view all albums that are related to the artist.
Users can logout from their account.

I wanted to add a feature where songs could be graded by giving them a "thumbs up" but unfortunately this didn't get done in time. There was a problem where when "thumbing" a song the vote was given to the wrong song. I also suspect the songs grade was displayed wrong.
As another feature I didn't have time to do was for the users to be able to edit albums added by other users. This lead to an admin tool to lock off a specific album from editing which wasn't finished either.
I could go on and on on the features I wanted to add but in the end just didn't have the time. All in all I think this project turned out fine. It has the core features that it needs to make it work. Most of the missing features were a sort of spinoff of an already implemented feature.

HEROKU: https://levyraati.herokuapp.com
