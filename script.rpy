##dialogue names
define s = Character('unknown lady', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

##START OF GAME
label start:
 stop music fadeout 1.0
 scene wallpaper_house
 with fade

 "This the the neighborhood that I'm used to, every day I swear is a repeat of the last. When will things start to brighten up around  here? Who knows." 
 "Here's hoping that attending a new University called GUI University of Information accepted my application. This might mean a fresh new start to my college life. New places, new people. I should try to make some friends."

 "**Looking around, you notice that without even thinking you've already arrived on campus. As if your legs brought you there of their own accord. Where do you go from here?**"


menu:
##this is the C++ / lua route
 "Walk around aimlessly":
  scene wallpaper_meshel_i_think
  with dissolve
  jump wander

##this is the python/java route
 "Go to Library":
  scene wallpaper_is_smoke_free_baby
  with dissolve
  jump library

##this is the javascript/ruby route
 "Go to local cafe":
  scene wallpaper_funky_statue
  with dissolve
  jump cafe

##this is the c#/scratch route
 "Stand around the class building":
  scene wallpaper_stairs
  with dissolve
  jump standing


label wander:
 show cppneutral
 "You wander the campus with no direction, and find yourself in front of two girls. One with very vibrant blue hair but a stern posture, and another with royal purple hair that is operating more meekly."
  

label library:
 "Finding the library not so far away, you go in to find that all the tables have been taken. You ask a very sharply dressed young woman in a lab coat if you could sit with her and her friend. She accepts."  
  
label cafe:
 "Feeling drowsy you decide caffeine is the best idea right now. Making your way towards the cafe. But on your way, you bump into a very stressed looking young red head who immediately apologizes, despite the entire incident being your fault anyways." 
  
label standing:
 "You decide to stick around a campus building, see who comes out of class when the bell rings. After about five minutes and 9 rings of the bell, you see a gothy looking girl chirping away at a younger looking girl with a cat ear headband."
 "The latter catches your stare, and decides to stop her friend to come talk to you."
  


