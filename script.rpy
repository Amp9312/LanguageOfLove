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
 "You decide to stick around a campus building, see who comes out of class when the bell rings. After about five minutes and 9 rings of the bell, you see a gothy looking girl complaining away, eating a lollipop. A disinterested but listening younger"
 "looking girl with a cat ear headband is following her."
 "Which one do you approach?"

menu:
##this is the c sharp path
 "Approach the gothy looking one":
  jump csharpchoice
##this is the scratch route  
 "See if you can get the cat ear girls attention":
  jump scratchchoice

label csharpchoice:
 "You walk up to the girl with the lollipop. You've got three options to pick from"
menu:
 "*Accidentally bump into her*":
  jump bumpinto
 "Say Hey":
  jump SayHey
 "Ask her what that mouth do":
  jump disgusted

label bumpinto:
 "You bump into her, seeing her drop her lollipop"
 ##Show annoyed face
 "MY FRICKING LOLLIPOP"

##This branch still needs finished

 jump finished
label SayHey:
 "S'up?" 
 "You stand there for a minute, thinking of what to say"
 "To break the silence, you bring up one of the following:"
menu:
 "I see you're coming from Calculus. I'm new so, do you know what the class is like?":
  jump convo
 "I really like your hair!":
  jump hair

label convo:
 "If you like lots of homework and pop quizzes, it's a hoot. You'll love it. If you're like me,"
 "you're gonna be a bit behind."

##This branch still needs finished

label hair:
 "Oh, thank you! I did it myself. It's not the best but I like it."

menu:
 "You did a great job!":
  jump greatjob
 "Could use some work here and there but it isn't bad for an amatuer. **wink**":
  jump tease

label greatjob:
 "Aw thanks, you ever think about dying your hair?"

menu:
 "That's kinda gay if I'm being honest":
  jump gay
 "I have, I don't know what color though":
  jump yesdye

label gay:
 "It's...not gay. And it's rude of you to think so, if I'm being honest."
 "C# walks away unamused"
 jump finished

label yesdye:
 "Anyone can pull off any color, but for you I could see some warmer tones."
 "*She winks at you*"

menu:
 "Yeah? I might go see a stylist then":
  jump stylist
 "Yeah? Do you dye other people's hair?":
  jump herdye

label stylist:
 "Looking around, she realizes how much time has passed and decides to leave."
 "Cool! Haha I have to go now. I'll see you around."

label herdye:
 "I have before, and if you'd like I can do yours. I rarely work with shorter hair, so it would be easy."
 "She smiles, and hands you her card. It's a professionally made one by a salon."
 "Here's my number, think about what you'd like and I'll see if I can't make it happen."
jump finished

label tease:
 "She's clearly annoyed by that"
 "And you're some kind of professional?"

menu:
 "As  matter of fact yes":
  jump yes
 "Well, um...no":
  jump no

label yes:
 "With that scruffy hairdo I didn't think so. But thanks for insulting me." 
 "C# walks away with a bad taste in her mouth"
 jump finished

label no:
 "Exactly, so maybe don' go criticizing my hair when yours looks like a nest."
 "C# walks away with a bad taste in her mouth"
 jump finished 
label scratchchoice:

label finished:
 "End of Act One"
