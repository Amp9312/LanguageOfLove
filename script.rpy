##dialogue names
define s = Character('Cassandra', color="#c8ffc8")
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
##this is the csharp/scratch route
 "Stand around the class building":
  scene wallpaper_stairs
  with dissolve
  jump standing


label wander:


 "You wander the campus with no direction, and find yourself in front of two girls. One with very vibrant blue hair but a stern posture, and another with dark blue hair that is operating more meekly. They are both looking at you."
 "Which one do you talk to?"
 
menu:
 "Vibrant blue hair":
  jump cppchoose
 "Dark Blue hair":
   jump luachoose

##c++ path
label cppchoose:
 show cppneutral
 s "Goodmorning, My name is Cassandra. You're new here right?"
##Are you new here?
menu:
 "Is it that obvious?":
  jump obvious
 "Yeah, I have no idea where I'm going":
  jump lost
 "*Ignore her, keep walking past*":
  jump ignore

#conversation A
label obvious:
 s "Very. You keep looking around as if it's the first time you are seeing this place"
##
menu:
 "Ha, i bet i look like an idiot.":
  jump idiot
 "I just like to take in the scenery.":
  jump scenery

label idiot:
s "Ha, you're not wrong."

menu:
 "do you often talk to idiots like me?":
  jump idiots_like_me
 "Well that makes two of us":
  jump rude

label idiots_like_me:
s "only if i think they could use my help."

menu:
 "Well, I am lost. So I could use your help.":
  jump help
 "you assume i need help, why so you can feel better about yourself?":
  jump rude2

label help:
s "of course you do and I have just the thing, a map of the campus. Take this and you'll never get lost again. Good luck!"
#add map to inventory
"Cassandra leaves, happy to help"
jump finished



label rude2:
s "hey! What's that supposed to mean? Never mind, I was going to help you but if you're going to be rude you can stay lost."
"Cassandra leaves, very annoyed."
jump finished


label rude:
s "Excuse me?? Are you calling me an idiot?"

menu:
 "No, I said you looked like one.":
  jump mean
 "That was a bad joke, I'm sorry.":
  jump sorry

label mean:
s "Hmp!"
"You made Cassandra mad, she storms off."
jump finished

label sorry:
s "Don't get on my bad side, you wont like it."
"Cassandra walks away annoyed."
jump finished


jump finished

label scenery:
s "well, not everyone has time to stop and smell the roses, especially in college."

menu:
 "you can always make time, maybe with me?":
   jump flirt

 "well of course, your valedictorian. When do you have time to do anything?":
  jump of_course

label flirt:
s "Yes let me add that to my schedule of things to do ‘smell roses with stranger’. Can't wait!"

menu:
 "Had to shoot my shot, could you blame a me?":
  jump shoot
 "Sarcasm will get you everywhere.":
  jump sarcasm

label shoot:
s "yes, I can. Look, do you know where you're going or do you want this map of the campus?"
"Cassandra hands you a map and leaves with no interest in you."
jump finished

label sarcasm:
s "And bad pickup lines will get you nowhere. Here, goodluck."
"Cassandra hands you a map and leaves with no interest in you."
jump finished

label of_course:
s "it's not like all i do is study and do homework, i have my fun just like everybody else"

menu:
 "oh really? What's your version of having fun then?":
  jump really
 "is that why you're talking to me?":
  jump talking

label really:

s "“well, i guess my main hobby would be fencing. I've been taking classes since I was 13, I'm practically a master."

menu:
 "Bad ass, remind me never to get on your bad side":
  jump bad_ass
 "Ooo, i like a girl that could kill me":
  jump kill_me

label bad_ass:
 s "blush* “hahaha, will do. So do you know where you're going?"

menu:
 "No idea, could you show me the way?":
  jump no_idea
 "Yes i do actually, but i'd love it if you walked me anyways":
  jump yes2

label no_idea:
s "well you haven't gotten on my nerves yet, so i suppose i could. This way,"
"Cassanda walks you to class"
jump finished

label yes2:
s "hahaha, you’re something else. Sure, why not."
"Cassandra happily walks you to class"

jump finished

label kill_me:
s "I will if you’re not careful. I have somewhere to be, take this map. It should help you around the campus"
"Cassanda hands you a map and with you in mind"
jump finished

label talking:
s "No! You just looked lost, thought you could use some direction. Look here just take this map of the campus. Good luck."
"cassandra hands you a map and walks away slightly annoyed."
jump finished


jump finished

#conversation B
label lost:
s "Most new students don't, as valedictorian of my class I know this school inside and out."

menu:
 "valedictorian huh, must be stressful to keep up that image.":
  jump val
 "so you can show me where to go then?":
  jump show_me

label val:
s "Ha! It's like second nature. I've always been top of my class."

menu:
 "smart, i like it. tell me more.":
  jump smart
 "its second nature for me to not know where the hell i'm going, think you could help me out?":
  jump second
label smart:
s "hmp. Love to, but i have somewhere to be. take this, it should help. I'll see you around."
"Cassandra hands you a map, and is uninterested in you."
jump finished


label second:
s "hahaha, you know what i think i have a minute. Where are you headed?"
"Cassandra finds you amusing and walks you to class"

jump finished

label show_me:
s "Take this map, it should help you get to where you need to go."
"Cassandra hands you a map and leaves"
jump finished

jump finished
label ignore:
s "*scoffs* Rude."
"you walk passed cassandra, shes way too intimdating."
##jump to new path later
hide cppneutral
jump finished
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
