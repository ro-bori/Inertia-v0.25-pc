



define i = Character("Inertia", color = "#ff0044")
define p = Character("[p]", color = "#ff0056")
define r = Character("Ryan", color = "#ff0000")
define t = Character("Tenika", color = "#0000FF")
define d = Character("Dylan", color = "ffa500")
define m = Character("Marcus", color = "#000000")
define j = Character("Jon", color = "#008000")
define je = Character("Jennifer", color = "#800080")
define ma = Character("Marty", color = "#c90014")
define b = Character("Ben", color = "0000ff")
define ja = Character("Jade", color = "#008000")
define s = Character("Stranger", color = "#FF0000")
define ad = Character("Adrian", color = "#8f3400")
define a = Character("Amy", color = "#9932CC")
define w = Character("Walter", color = "#FF9E00")
define mav = Character("Maverick", color = "#00D99E")
define l = Character("Lorenzo", color = "#008000")
define s = Character("Stranger", color = "#ff0000")


label splashscreen:
    $ renpy.movie_cutscene("dobintro.webm")
    scene warning with dissolve
    pause
    return



label start:
    stop music
    scene inertiaday1-1
    i "Heya!"
    scene inertiaday1-2
    i "It's a pleasure to meet you."
    i "My name is Inertia."
    i "Would you like to change my name?"
    menu:
        "Yes":
            $ p = renpy.input ("My new name is:", "", length=20,)
            if p == "":
                $ p = "Inertia"
                jump inertiadayname
        "No":
            $ p = "Inertia"
label intertiadayname:
    scene inertiaday1-2aa
    p "Down here, silly!"
    scene inertiaday1-2a
    p "I'm so glad you stopped by! I can't wait to begin my adventures with you."
    scene inertiaday1-2b
    p "Each day you will discover more about me and learn about my interests, fantasies and desires."
    scene inertiaday1-2c
    p "My life will have a lot of exciting events and many varied interactions with different characters. All outcomes are based on the choices you want me to make.​"
    scene inertiaday1-2d
    p "But please... be gentle."
    p "Anyway, now that we've got that out of the way..."
    scene inertiaday1-3
    p "My family owns this gym and I train here every day. As you might notice, it's pretty empty right now..."
    scene inertiaday1-4
    p "Come, follow me and we'll head upstairs to introduce you to everyone."
    "Would you like to skip the introduction?"
    menu:
        "Yes":
            jump begin01
        "No":
            jump introduction
label introduction:
    scene inertiaday1-5
    pause
    scene inertiaday1-6
    p "..."
    p "I'm watching you..."
    scene inertiaday1-7
    scene inertiaday1-7
    pause
    p "{i}This is my Dad's office, where all the administrative parts of running a gym take place. I almost never come in here."
    p "Hey, Dad."
    scene inertiaday1-8
    r "..."
    scene inertiaday1-8
    r "Hello, [p]. Did you get your workout in?"
    scene inertiaday1-10
    p "Yes sir. I trained my glutes and abs, just like you asked me to."
    scene inertiaday1-11
    r "Good girl."
    r "We're getting you fit, ready to look after yourself; ready to look after your siblings, too..."
    scene inertiaday1-12
    r "Speaking of which, can you go check on your brother and sister for me? They should be in the back room."
    scene inertiaday1-13
    p "No worries, I'll see what they're up to. See you later."
    scene inertiaday1-14
    p "I do love Dad, but he's ex-military, very strict, and he expects a lot from me."
    scene inertiaday1-15
    t "{i}Aieeeeeeeeeeeeee!!!{/i}"
    p "..."
    scene inertiaday1-16
    t "Dylaaan! LET ME GO!!"
    scene inertiaday1-17
    t "Get OFF of me! NOW!"
    scene inertiaday1-18
    t "I'M SERIOUS!"
    scene inertiaday1-18
    p "{i}This is my sister Tenika. She's an angel with a heart of gold and I'm super protective of her.{/i}"
    scene inertiaday1-19
    d "Or what? What you gonna do?"
    scene inertiaday1-20
    d "Cry about it!?"
    scene inertiaday1-20
    i "{i}And this... is my stepbrother, Dylan. Tenika and I don't get along with him. He's rude, arrogant and very 'inappropriate'.{/i}"
    scene inertiaday1-21
    t "My boob is nearly falling out of my top, get off!"
    scene inertiaday1-22
    d "That's a shame, isn't it..."
    t "STOP!"
    scene inertiaday1-23
    p "DYLAN, get off her! NOW!"
    scene inertiaday1-24
    p "Don't make me tell Dad..."
    scene inertiaday1-25
    d "..."
    scene inertiaday1-26
    d "Whatever. I'll see you losers back at home."
    scene inertiaday1-27
    d "Oh, and [p]..."
    scene inertiaday1-28
    pause
    scene inertiaday1-29
    pause
    scene inertiaday1-30
    p "..."
    scene inertiaday1-31
    d "Nice tits."
    scene inertiaday1-32
    p "I'm gonna kick your ass!"
    scene inertiaday1-33
    d "Hahaha, Losers!"
    scene inertiaday1-34
    p "What a fucking jerk."
    p "Are you alright Nika?"
    scene inertiaday1-35
    t "Yeah, I'm good. He's such a fucking dick, [p]."
    scene inertiaday1-36
    t "Thanks."
    p "I can't stand how he acts towards us... He'll learn, one way or another."
    scene inertiaday1-37
    p "Anyway, I'll see you back at home."
    scene inertiaday1-38
    p "{i}I love them both, but... god, he does my head in sometimes.{i}"
    p "{i}Fucking Dylan...{i}"
    scene inertiaday1-39
    pause
    scene inertiaday1-40
    pause
    scene inertiaday1-41
    m "Ay sis, what's going on."
    scene inertiaday1-42
    p "Marcus! What are you doing here?"
    scene inertiaday1-43
    m "Jon and I have decided to make some gains and join ya dad's gym."
    scene inertiaday1-44
    pause
    scene inertiaday1-45
    pause
    scene inertiaday1-46
    j "Hey [p], how are you?"
    scene inertiaday1-47
    pause
    p "Uhh..."
    scene inertiaday1-48
    p "Good... thanks."
    scene inertiaday1-49
    m "Do you know if Ryan is in the office? We're thinking of signing up."
    scene inertiaday1-50
    p "That's great! He's around. I was just there."
    scene inertiaday1-51
    m "Chur, we'll go sort that... and I'll catch up with {i}you{/i} later."
    scene inertiaday1-52
    pause
    scene inertiaday1-53
    j "Bye, [p]."
    scene inertiaday1-54
    p "Uh yeah, bye."
    scene inertiaday1-55
    p "{i}Bit of a weirdo..."
    scene inertiaday1-56
    p "{i}Marcus has been my best friend since childhood, over 12 years now."
    p "{i}Jon, on the other hand..."
    p "{i}He's Marcus' roommate, but I've always had strange vibes about him."
    scene inertiaday1-57
    pause
    scene inertiaday1-58
    p "Hey, Jen!"
    scene inertiaday1-59
    pause
    scene inertiaday1-60
    je "Hey, Babe! What's going on?"
    scene inertiaday1-60
    je "Look at you, lookin' all fit and stuff. Go on, chuck us a pose."
    scene inertiaday1-61
    pause
    scene inertiaday1-62
    je "Damn...! Show me them abs, girl!"
    scene inertiaday1-63
    pause
    scene inertiaday1-64
    je "Oooh... you're gonna kill when we go to the beach."
    je "Now get those clothes off!"
    scene inertiaday1-65
    p "..."
    p "Uhh..."
    scene inertiaday1-66
    je "Haha! I'm joking, silly, you're adorable."
    scene inertiaday1-67
    je " I'll see you later, babe."
    scene inertiaday1-68
    p "{i}Oh my god! She's such a cheeky bitch, she does this stuff all the time."
    scene inertiaday1-68
    p "{i}Although I'm not gonna lie, I do kinda like it...{/i}"
    scene inertiaday1-70
    p "Well, that's basically my friends and family. I guess it's time we begin my adventure."
    scene inertiaday1-71
    p "Try not to have too much fun with me!"


label begin01:
    scene inertiaday1-72
    play sound "alarmsound.ogg"
    pause
    stop sound
    scene inertiaday1-73
    pause
    scene inertiaday1-74
    pause
    scene inertiaday1-75
    p "I HATE waking up this early, but Dad always makes us."
    scene inertiaday1-76
    p "He says it {i}builds character{/i}, whatever that means."
    scene inertiaday1-77
    p "Today's a really big day for me; I'm meant to be looking for a job. Hopefully I'll be able to find something."
    scene inertiaday1-78
    p "Dad says I can't live at home anymore without paying my way, so... it looks like I'll have to figure something out fast."

    scene inertiaday1-79
    p "In the meantime, I'd better wake Tenika."
    scene inertiaday1-80
    pause
    p "..."
    scene inertiaday1-81
    pause
    scene inertiaday1-82
    pause
    scene inertiaday1-83
    pause
    scene inertiaday1-84
    pause
    scene inertiaday1-85
    pause
    d "{i}I could get used to this...{/i}"
    p "DYLAN!"
    scene inertiaday1-86
    "..."
    scene inertiaday1-87
    t "GET OUT, YOU FUCKING FREAK!"
    scene inertiaday1-88
    p "WHAT IS WRONG WITH YOU?"
    scene inertiaday1-89
    d "..."
    d "Blow me, bitch!"
    scene inertiaday1-90
    d "See ya, losers."
    scene inertiaday1-91
    p "Jesus, are you alright Tenika?"
    scene inertiaday1-92
    t "What the fuck is wrong with him...? Why does he do that shit? I'm so sick of him."
    scene inertiaday1-93
    p "Don't worry, karma will come that little perv's way... I'll make sure of it."
    scene inertiaday1-94
    p "{i}It's infuriating, but... I have to try and smile for Nika. She'll feel worse if she sees I'm really pissed."
    p "I'll see you later this afternoon for training, okay? Love you, Nika."
    scene inertiaday1-95
    p "{i} I need to think of a way to pay Dylan back for all his pervy antics! I'm so over the disrespect he shows this family.{/i}"
    p "{i}No one gets to treat my Nika like that. I don't care who they are.{/i}"
    scene inertiaday1-96
    p "Morning, Dad..."
    scene inertiaday1-97
    r "Morning [p]."
    scene inertiaday1-99
    r "Have you woken Tenika up?"
    scene inertiaday1-98
    p "Yep, though it was something of a team effort. Dylan... beat me there. She's awake and getting dressed."
    p "{i} If only I could tell him what else Dylan was 'beating'. But not now, Dad wouldn't take it well and it wouldn't solve anything."
    scene inertiaday1-100
    r "Good."
    scene inertiaday1-101
    r "You have a big day ahead."
    scene inertiaday1-104
    r "Job hunting. You're old enough now to start contributing to the household a bit."
    r "{i}With the way the gym is going, she might be supporting the house on her own soon..."
    scene inertiaday1-102
    p "Yes, Dad. I'll go have a shower, get changed and head into town."
    scene inertiaday1-103
    r "If you run into any trouble, let me know."
    scene inertiaday1-104
    r "Oh and [p]..."
    scene inertiaday1-106
    p "Yeah?"
    scene inertiaday1-107
    r "Put some pants on."
    scene inertiaday1-105
    p "..."
    scene inertiaday1-108
    p "I hope I can find some work today..."
    scene inertiaday1-109
    p "Oh, someone's in the shower."
    p "It's Jen."
    p "Should I enter?"
menu:
    "Yes.":
        jump choice_enter1
    "No, wait.":
        jump choice_dontenter1


label choice_dontenter1:
    scene inertiaday1-125
    p "{i}I'm super nervous about today, I'm hoping it all goes well.{/i}"
    scene inertiaday1-124
    p "{i}If I don't find a job, Dad's gonna kill me!{/i}"
    scene inertiaday1-126
    p "{i}He's always hassling me to get things done. I do love him, but sometimes he's too strict on us all.{/i}"
    p "{i}I guess I can understand why, considering...{/i}"
    scene inertiaday1-127
    p "{i}Anyway, the training regime is so draining, but I'm seeing great progress so I have him to thank for that.{/i}"
    p "{i}Jen, on the other hand, is like a best friend - she's always there to support me, and sometimes I feel this strange... attraction to her.{/i}"
    p "{i}Of course, I've never told her. Because yeah, that's pretty embarassing.{/i}"
    scene inertiaday1-127
    p "Right! I'm feeling all sparkly 'n clean, let's kickstart the day!"


    jump finish_shower1

label choice_enter1:
    scene inertiaday1-110
    p "..."
    scene inertiaday1-111
    p "Hey, Jen."
    scene inertiaday1-112
    p "Hey, babe! What's going on?"
    scene inertiaday1-113
    p "Not a lot, how about you?"
    scene inertiaday1-114
    je "..."
    je "Oh c'mon, you're acting like you've never seen a naked girl before."
    scene inertiaday1-115
    p "Haha, of course I have."
    scene inertiaday1-116
    je "..."
    scene inertiaday1-117
    je "You're adorable."
    je "By the way, I'm taking you to the beach tomorrow so... be ready."
    scene inertiaday1-118
    p "Okay, sounds good to me! I'm really excited."
    scene inertiaday1-119
    je "See ya tomorrow, babe."
    scene inertiaday1-120
    p "..."
    scene inertiaday1-121
    je "Oh and [p]..."
    scene inertiaday1-122
    je "Lookin' good."
    scene inertiaday1-123
    p "..."
    p "Thanks, you too!"
    scene inertiaday1-125
    p "..."
    p "{i}I have a strange attraction to Jennifer, she's dating Dad, but... I feel like she's always flirting with me...{/i}"
    scene inertiaday1-126
    p "{i}Maybe I'm overthinking things, but I've never really told anyone that I'm also attracted to girls. I guess no one would really know, considering I'm still a virgin."
    scene inertiaday1-124
    p "{i}I mean, in school I did have my fair share of makeout sessions and experimented a bit...{/i}"
    p "{i}But never with sex..."
    p "{i}I don't know why. I guess I'm still figuring myself out.{/i}"
    scene inertiaday1-127
    p "{i}The only person that knows I'm attracted to girls is...{/i}"
    p "{i}Dylan."
    scene inertiaday1-127
    p "Anyway, I don't really want to get into that."
    p "I should probably get going."

label finish_shower1:
    scene inertiaday1-128
    p "..."
    scene inertiaday1-129
    p "..."
    scene inertiaday1-130
    p "I think that's everything. I should probably say goodbye to Dad first."
    scene inertiaday1-131
    pause
    scene inertiaday1-132
    pause
    scene inertiaday1-133
    p "..."
    scene inertiaday1-134
    p "{i}Oh my god!{i}"
    scene inertiaday1-135
    je "The things I'm gonna do to you when you get home from work."
    scene inertiaday1-134
    p "{i} Dad never lets me see him and Jen like this. It's kinda...{i}"
    p "*cough*"
    scene inertiaday1-136
    r "..."
    r "I thought you left a while ago?"
    scene inertiaday1-137
    p "Uhh..."
    scene inertiaday1-138
    p "Yep, I'm heading off now."
    scene inertiaday1-139
    r "Good, let me know how job hunting goes. Give me a call if you need anything."
    scene inertiaday1-140
    je "Bye, babe. Good luck!"
    scene inertiaday1-141
    p "Bye, guys."
    scene inertiaday1-142
    p "{i}What a beautiful day, hopefully I can tan by the pool after job searching.{/i}"
    scene inertiaday1-143a
    ma "{i}Shit...! If I don't find someone soon, the boss will fire me."
    scene inertiaday1-142
    p "{i}There's so many shops and stores, I'm not sure where to start.{/i}"
    scene inertiaday1-143b
    ma "Look at that one over there! She's perfect!"
    scene inertiaday1-143c
    pause
    scene inertiaday1-143
    p "I guess I'll start... here."
    scene inertiaday1-144
    ma "HEY!"
    p "{i}Hmmm?"
    scene inertiaday1-145
    ma "Excuse me...!"
    scene inertiaday1-146
    p "Uh, hello?"
    scene inertiaday1-147
    ma "I'm so sorry... Listen, I know this is random, but I saw you across the street and just had to say hello."
    ma "You're absolutely {i}gorgeous{/i}."
    scene inertiaday1-148
    p "Um ... Thank you, ... I guess?"
    scene inertiaday1-149
    ma "My name's Marty. It's a pleasure to meet you."
    scene inertiaday1-151
    p "[p], it's... nice to meet you, too."
    scene inertiaday1-150
    ma "That's a lovely name."
    ma "What are you up to at the moment?"
    scene inertiaday1-154
    p "I'm currently looking for a job. I need to start supporting myself, so I'm out here trying to find anything I can."
    scene inertiaday1-152
    ma "Well, It's your lucky day! The reason I stopped you is because I think you're {i}amazingly{/i} beautiful. I own a photography studio down the road, and I'd love to take a few portrait shots of you."
    scene inertiaday1-153
    ma "I'm happy to pay you double, because I really love your look!"
    ma "{i}Not that she knows what the normal price is anyway...{i}"
    scene inertiaday1-154
    p "Oh wow!... that sounds great, but... I don't have any clothes with me... and I've never really modelled before..."
    scene inertiaday1-155
    ma "That's totally fine! We can shoot in what you're wearing. You have a great style and, with my direction, you'll have no trouble at all. It's for a fashion magazine and there could be a {i}lot{/i} more high paid work involved."
    scene inertiaday1-156
    p "Well..."
    scene inertiaday1-157
    p "OK, I guess! I do need the money, and I used to do cheerleading in high school not long ago. So, ... I guess that could help?"
    scene inertiaday1-158
    ma "Perfect! I guarantee it will. You won't regret this! Let's go."
    scene inertiaday1-159
    ma "My studio is just down the road."
    scene inertiaday1-160
    ma "Here we are! After you."
    scene inertiaday1-161
    ma "..."
    ma "So uhh... this is it."
    scene inertiaday1-162
    pause
    scene inertiaday1-163
    p "Well, it's a little small... but, at least you've got a backdrop."
    scene inertiaday1-164
    ma "Yeah... I'll be upgrading soon, but first I've got to prove to my boss how good I really am. Hopefully this shoot will help."
    scene inertiaday1-166
    p "I see..."
    scene inertiaday1-167
    p "So... how much are you going to be paying me?"
    scene inertiaday1-168
    ma "Haha, settle down. The more you listen and cooperate, the more I'll think about giving you."
    scene inertiaday1-169
    ma "But as I said earlier, I will be paying you double anyway... so keep that in mind as we shoot."
    ma "Alright, let's begin. If you could head over to the centre of the backdrop, please."
    scene inertiaday1-170
    p "..."
    ma "{i}Damn... she's smokin'! I can't wait to show the boss this one. This could set me up for a while{/i}."
    scene inertiaday1-171
    ma "Alright, ready to begin?"
    scene inertiaday1-172
    p "Where do you want me? I'm not really sure what to do."
    scene inertiaday1-173
    ma "{i}Where do I want her...? I can think of a few places..."
    ma "I'll direct you, don't worry, [p], you can stand still and I'll take some basic portait shots."
    scene inertiaday1-174
    p "Okay."
    scene inertiaday1-175
    play sound "shutter.ogg"
    pause
    ma "Amazing."
    ma "Now, one hand in your hair and the other down by your waist."
    scene inertiaday1-176
    play sound "shutter.ogg"
    pause
    ma "Perfect."
    ma "Now look off to the side."
    scene inertiaday1-177
    play sound "shutter.ogg"
    pause
    ma "{i}Beautiful,{/i} [p]."
    ma "Last pose, hand on your forehead and look at the lens."
    scene inertiaday1-178
    play sound "shutter.ogg"
    pause
    ma "Stunning!"
    scene inertiaday1-179
    p "Is this right?"
    scene inertiaday1-180
    ma "You're a natural."
    ma "{i}Of course! With my direction, I can make anyone look like a natural..."
    scene inertiaday1-181
    ma "Are you sure you haven't done this before?"
    scene inertiaday1-182
    p "Haha..."
    scene inertiaday1-183
    p "Nope. I guess it's the cheerleading experience from high school."
    scene inertiaday1-184
    ma "I can tell, your body is amazing! If I were you, I'd show it off as much as I could!"
    scene inertiaday1-185
    ma "Hmm.... how would you feel about pulling your top up a little bit so we can, ah... emphasise your abs?"
    scene inertiaday1-186
    p "Umm...I guess that's okay."
    scene inertiaday1-187
    pause
    scene inertiaday1-188
    pause
    scene inertiaday1-189
    p "Like this, Marty?"
    scene inertiaday1-190
    ma "That's {i}great{/i}, [p]."
    scene inertiaday1-191
    ma "Now, let's have you stand in a... normal pose and relax your shoulders."
    scene inertiaday1-192
    play sound "shutter.ogg"
    pause
    ma "Your body is so amazing!"
    ma "Now could you turn to the side and look at me please."
    scene inertiaday1-193
    play sound "shutter.ogg"
    pause
    scene inertiaday1-194
    pause
    ma "..."
    ma "{i}Look at that toned ass! She's so small, but she's amazingly tight and fit.{/i}"
    scene inertiaday1-195
    p "Everything okay, Marty?"
    scene inertiaday1-196
    ma "Yeah, everything's just fine..."
    ma "Let's mix things up a little bit now and have you sit on the ground with a pose of your choice."
    scene inertiaday1-197
    p "I have no idea what this pose is, and I don't know how you want me?"
    scene inertiaday1-198
    ma "{i}So many different ways{/i} *cough*"
    ma "I mean, really, do whatever you like. Have fun and I'll capture the moments."
    scene inertiaday1-199
    p "Alright, I'll try and be... spontaneous, then."
    scene inertiaday1-200
    play sound "shutter.ogg"
    pause
    ma "Very cute!"
    scene inertiaday1-201
    play sound "shutter.ogg"
    pause
    ma "I love that one!"
    scene inertiaday1-202
    play sound "shutter.ogg"
    pause
    ma "Ooh, exciting!"
    scene inertiaday1-203
    ma "{i}Her boobs are nearly falling out of her top...{/i}"
    scene inertiaday1-204
    ma "{i}Should I tell her?{/i}"
    menu:
        "Yes":
            jump yes1
        "No":
            jump no1

label yes1:
    scene inertiaday1-205
    ma "Hey, [p], you may wanna pull your top up."
    scene inertiaday1-206
    p "..."
    scene inertiaday1-207
    p "Oh, thanks!"
    p "{i}That was nice of him to let me know.{i}"
    p "{i}What a gentleman.{i}"
    scene inertiaday1-208
    ma "You're welcome. Let's do some standing poses with different emotions. Alright, hands up!"
    scene inertiaday1-209
    play sound "shutter.ogg"
    pause
    scene inertiaday1-210
    play sound "shutter.ogg"
    pause
    ma "I love it, now a determined pose!"
    scene inertiaday1-211
    play sound "shutter.ogg"
    pause
    scene inertiaday1-212
    play sound "shutter.ogg"
    pause
    ma "Amazing, you rock girl!"
    ma "Last pose, turn backwards and show me just how much of a rockstar you are!"
    scene inertiaday1-213
    play sound "shutter.ogg"
    pause
    scene inertiaday1-214
    play sound "shutter.ogg"
    pause
    scene inertiaday1-215
    ma "You did great, well done!"
    scene inertiaday1-216
    p "Yay, you really think so?"
    scene inertiaday1-217
    ma "I know so!"
    scene inertiaday1-242
    ma "To be completely honest, I've shot a lot of other amateur models and you've smoked them out of the water. Here's $250 for your efforts today and hopefully I'll see you soon."
    scene inertiaday1-243
    p "I had a lot of fun today! Thank you for your help."
    scene inertiaday1-241
    ma "Any time, I'll message you within the next few days with an update. Have a great day."
    scene inertiaday1-244
    p "See ya later, Marty."
    scene inertiaday1-245
    ma "Bye."
    jump home_1


label no1:
    scene inertiaday1-217
    ma "Hey, [p], let's try some more poses with a bit of... character. Can you take a step forward and I'll capture you in motion."
    scene inertiaday1-218
    p "Alright, I'll give it my best shot."
    scene inertiaday1-219
    play sound "shutter.ogg"
    pause
    scene inertiaday1-220
    play sound "shutter.ogg"
    pause
    ma "{i}She has no idea...{/i}"
    scene inertiaday1-221
    play sound "shutter.ogg"
    pause
    scene inertiaday1-222
    play sound "shutter.ogg"
    pause
    ma "{i}Holy shit, these photos are amazing! I'm going to ask her to try something...{/i}"
    scene inertiaday1-223
    ma "Hey, I just remembered how you said you used to do cheerleading - I'd love if we could capture a jumping shot. It'll be hard to do in your heels but I think you can handle it!"
    scene inertiaday1-224
    p "I'll give it a go, let's hope I don't break my ankles, haha!"
    pause
    scene inertiaday1-225
    play sound "shutter.ogg"
    pause
    scene inertiaday1-226
    play sound "shutter.ogg"
    pause
    scene inertiaday1-227
    p "How was that?"
    scene inertiaday1-228
    ma "{i}Look at those big, firm tits... I've never seen a better pair...{/i}"
    scene inertiaday1-229
    ma "You're a natural, [p]. One of my favourite models to work with, ever! Give me a smile please."
    scene inertiaday1-230
    p "{i}He's making me feel good, I just hope he's telling the truth.{/i}"
    scene inertiaday1-231
    play sound "shutter.ogg"
    pause
    scene inertiaday1-232
    play sound "shutter.ogg"
    pause
    ma "{i}The boss is going to love these...{/i}"
    scene inertiaday1-233
    play sound "shutter.ogg"
    pause
    scene inertiaday1-234
    pause
    p "..."
    scene inertiaday1-235
    p "Heyyyy!"
    scene inertiaday1-236
    p "What the hell! Why didn't you tell me my breasts were exposed..."
    scene inertiaday1-237
    ma "I, ah, didn't even notice, your beauty was the only thing I was focusing on. Trust me, even though a bit of nipple was showing, your natural beauty is like no other!"
    scene inertiaday1-238
    ma "As I said before, you've got amazing talent and great assets, don't stress about a little skin showing."
    scene inertiaday1-239
    p "Mmmm..."
    scene inertiaday1-240
    p "But my whole breasts were exposed... No one has ever seen them like that before..."
    scene inertiaday1-241
    ma "Believe me, the amount of people who do nude photography nowadays is unimaginable. Even though you weren't planning to do topless, you absolutely killed the shoot, the pictures won't go anywhere, I promise."
    scene inertiaday1-242
    ma "Here's $250 for your efforts today and again, we won't use those accidental photos."
    scene inertiaday1-243
    p "Okay, I trust you, thank you for the fun experience and the money today. Make sure you delete the topless photos, please."
    scene inertiaday1-244
    ma "Of {i}course{/i}, take care! I'll contact you soon."
    p "Bye."
    scene inertiaday1-245
    ma "{i}I know some people would pay a lot of money for these shots... but should I?{/i}"
    scene inertiaday1-246
    p "{i}I've never experienced a situation like that before. I mean I did earn $250...{/i}"
    p "{i}But I let a random photographer see my boobs! Although, he did say a lot of people do nude modelling... so I guess it must be somewhat normal...{/i}"
    scene inertiaday1-247
    p "..."
    p "{i}I'm just hoping those pictures get deleted.{/i}"
    p "{i}I really should've made sure.{/i}"
    p "{i}But I guess I'll trust him, for now...{/i}"
    scene inertiaday1-248
    p "{i}Time to head home.{/i}"

label home_1:
    scene inertiaday1-249
    p "{i}What an eventful day... at least I've got time to tan for a while.{i}"
    scene inertiaday1-250
    p "{i}Even better, it looks like no one's home{i}."
    scene inertiaday1-251
    pause
    scene inertiaday1-252
    pause
    scene inertiaday1-253
    pause
    p "{i}Let's go.{i}"
    scene inertiaday1-254
    pause
    scene inertiaday1-255
    pause
    scene inertiaday1-256
    p "{i}Ahhhhh... so good to relax... nothing better than some peace and quiet, and no one around.{/i}"
    scene inertiaday1-256
    pause
    scene inertiaday1-258
    pause
    scene inertiaday1-259
    pause
    scene inertiaday1-260
    pause
    scene inertiaday1-261
    b "Damn Bro..."
    b "... your sister is so hot."
    scene inertiaday1-262
    d "Yeah, whatever dickhead. Let me go grab the smokes, wait here."
    scene inertiaday1-263
    b "No worries."
    scene inertiaday1-264
    pause
    b "..."
    b "{i}I should probably say something. You don't get opportunities like this with a girl like that very often.{/i}"
    scene inertiaday1-264
    pause
    scene inertiaday1-265
    pause
    scene inertiaday1-266
    pause
    scene inertiaday1-267
    pause
    scene inertiaday1-271
    b "Uh... hi, [p]."
    scene inertiaday1-267
    pause
    scene inertiaday1-268
    pause
    scene inertiaday1-270
    p "Heyyy, uh, Ben... what are you doing here?"
    scene inertiaday1-271
    b "Just waiting for Dylan to grab something, what're you up to?"
    scene inertiaday1-272
    p "Tannin' my white ass, haha! I just finished up with a modelling shoot so I'm wanting to look my best for any future jobs."
    scene inertiaday1-273
    b "Wow, well you've definitely got the looks for modelling. I hope it turns out great for you."
    scene inertiaday1-274
    p "Thanks, Ben, I hope so too. Who knows, you may even see me featured in some magazines, haha!"
    scene inertiaday1-275
    b "I'm sure I will. And, good luck... just make sure you don't get sunburnt for any future shoots. haha!"
    scene inertiaday1-274
    p "I'll try my best, and uh, yep I'm being... very careful."
    scene inertiaday1-275
    b "..."
    b "{i}Hmmm..{/i}"
    scene inertiaday1-276
    b "Umm... so... do you maybe... need me to put some sunscreen on your back? It's umm... okay if you say no, I thought I'd ask anyway... so you look your best for any future shoots."
    scene inertiaday1-277
    p "Umm..."
    menu:
        "Sure":
            jump sunscreen1
        "No":
            jump nosunscreen1
label nosunscreen1:
    scene inertiaday1-278
    p "No thanks, Ben, but I appreciate the offer."
    jump end2
label sunscreen1:
    scene inertiaday1-278
    p "Sure, I guess that'd be okay."
    scene inertiaday1-279
    pause
    b "{i}She actually let me do it! Dylan would be so pissed if he saw this... oh well, ha ha!{/i}"
    scene inertiaday1-280
    pause
    scene inertiaday1-281
    pause
    scene inertiaday1-282
    pause
    scene inertiaday1-281
    pause
    scene inertiaday1-282
    pause
    b "Is this... okay?"
    scene inertiaday1-283
    p "That's fine, it's hard to reach those spots anyway."
    scene inertiaday1-281
    pause
    scene inertiaday1-282
    pause
    scene inertiaday1-281
    pause
    scene inertiaday1-282
    pause
    scene inertiaday1-284
    b "{i}Oh wow! Her skin feels so smooth...{/i}"
    scene inertiaday1-285
    b "Hey [p]... is it okay if I do your legs...?"
    scene inertiaday1-286
    p "Yeah, that should be alright."
    scene inertiaday1-287
    pause
    scene inertiaday1-288
    pause
    scene inertiaday1-289
    pause
    scene inertiaday1-288
    pause
    scene inertiaday1-289
    pause
    b "{i}Damn, what a great view!{/i}"
    scene inertiaday1-288
    pause
    scene inertiaday1-289
    pause
    scene inertiaday1-290
    pause
    b "{i}I can tell she works out... her ass and legs are really toned.{/i}"
    b "{i}I wonder If I can push my luck...?{/i}"
    scene inertiaday1-291
    pause
    scene inertiaday1-292
    pause
    scene inertiaday1-293
    pause
    scene inertiaday1-294
    p "..."
    p "{i}Why is he touching my ass!?{/i}"
    p "{i}I think maybe he's just trying to spread the sunscreen everywhere...?{/i}"
    scene inertiaday1-296
    pause
    scene inertiaday1-297
    pause
    scene inertiaday1-298
    p "Okay, that's all fine Ben, thank you!"
    jump end1
label end2:
    scene inertiaday1-299
    b "Oh... Umm... No worries [p], I better go."
    b "Have fun tanning and good luck with any of your future shoots."
    scene inertiaday1-300
    pause
    scene inertiaday1-301
    pause
    d "I got the shit, let's go, dickhead."
    scene inertiaday1-302
    b "No worries, ready when you are."
    scene inertiaday1-303
    pause
    p "..."
    p "{i}People are being very friendly today...{/i}"
    p "{i}First in the morning with Jen...{/i}"
    p "{i}The photoshoot with Marty...{/i}"
    p "{i}And now Dylan's best friend Ben...{/i}"
    jump finish1
label end1:
    scene inertiaday1-299
    b "..."
    b "Oh... No worries [p]... I better go."
    scene inertiaday1-300
    pause
    scene inertiaday1-301
    pause
    d "I got the shit, let's go dickhead."
    scene inertiaday1-302
    b "Awesome... uh, ready when you are."
    scene inertiaday1-303
    pause
    p "{i}What is coming over me...?{/i}"
    p "{i}First, in the morning with Jen...{/i}"
    p "{i}the photoshoot with Marty...{/i}"
    p "{i}and now letting Dylan's best friend nearly touch my... privates...{/i}"
    p "{i}Who knows if he saw anything...{/i}"
label finish1:
    scene inertiaday1-303
    p "{i}Could it be that I'm starting to enjoy this...? Or should I ignore what's happened and try to avoid similar situations...{/i}"
    p "{i}What a strange day.{/i}"
    "..."
    t "Heya!"
label v015:
    scene inertiaday1-305
    pause
    scene inertiaday1-304
    t "What's going on? 'Bout time you tanned your white ass."
    scene inertiaday1-307
    p "Haha! Shut up, you're one to talk."
    p "Ben and Dylan just dropped by to get something, do you know what they were doing? How was school by the way?"
    scene inertiaday1-308
    t "I just saw them on the way out. I'm pretty sure they are going to smoke again, haha... if only Dad knew."
    scene inertiaday1-309
    t "And school was okay, the bitches in the year above keep bullying me and saying some nasty shit..."
    scene inertiaday1-310
    p "What the hell? Are you serious, I thought they cut that crap out!"
    scene inertiaday1-311
    p "Who's ass do I need to kick?"
    scene inertiaday1-312
    t "Haha, don't worry about it [p], I can handle myself."
    scene inertiaday1-313
    p "Alright... but if they keep it up, I won't hesitate to come down there!"
    p "{i}I don't forget people who mistreat my little Nika!... They better hope I don't catch them treating her badly in front of me...{/i}"
    p "{i}It might be best not to say that to her though, it would only make her worry.{/i}"
    p "So, you wanna go get changed and we can do some yoga together?"
    scene inertiaday1-314
    t "Yeah let's do it, I really need to blow off some steam!"
    scene inertiaday1-315
    t "C'mon, Whitey!"
    scene inertiaday1-316
    p "Careful I don't kick your ass, too."
    scene inertiaday1-317
    t "Hehe."
    scene inertiaday1-318
    pause
    scene inertiaday1-319
    t "Alright, I'm gonna get changed. I'll meet you out on the balcony."
    scene inertiaday1-320
    p "No worries, I'll meet you there."
    scene inertiaday1-321
    pause
    scene inertiaday1-322
    pause
    scene inertiaday1-323
    pause
    scene inertiaday1-324
    p "{i}Ready!{/i}"
    play sound "shutter.ogg"
    scene inertiaday1-324
    pause
    scene inertiaday1-325
    p "..."
    scene inertiaday1-328
    play sound "shutter.ogg"
    pause
    scene inertiaday1-326
    play sound "shutter.ogg"
    pause
    play sound "shutter.ogg"
    scene inertiaday1-327
    pause
    scene inertiaday1-329
    t "OH MY GOD! I'M SO FUCKING UGLY!"
    scene inertiaday1-330
    p "Shut up you idiot, you're not ugly. What's wrong?"
    scene inertiaday1-331
    t "I'm trying to take a photo for someone I like, and I look like a... fucking potato!"
    scene inertiaday1-332
    p "Oh my god you do not. Here, let me help you."
    scene inertiaday1-333
    p "So who is this person you're trying to take a photo for?"
    scene inertiaday1-334
    t "Someone at school who I'm... sort of seeing...? Haha, I really like them."
    scene inertiaday1-335
    p "Do you trust this person?"
    scene inertiaday1-336
    t "Yeah, I do, completely... They're amazing."
    scene inertiaday1-337
    p "Alright then, sit back on the bed, get comfy and pull one of your legs underneath you."
    scene inertiaday1-338
    p "If you really want to impress them undo the buttons of your shirt... but don't show too much."
    scene inertiaday1-339
    t "Is this good?"
    p "{i}Well I like it...{i}"
    p "That's so cute, hold that pose!"
    scene inertiaday1-339
    play sound "shutter.ogg"
    pause
    scene inertiaday1-340
    p "I guess you don't look like too much of a potato in this one."
    scene inertiaday1-341
    t "Haha whatever, now let me see."
    scene inertiaday1-342
    pause
    scene inertiaday1-343
    pause
    scene inertiaday1-344
    t "Oh my god that's so good! Thanks, [p]!"
    scene inertiaday1-345
    p "You're talking to a {i}professional{/i} model, of course they're good. I'll help you any time, so don't be such a negative nancy."
    scene inertiaday1-346
    p "Let's get ready for yoga. I'll meet you on the balcony."
    scene inertiaday1-347
    p "{i}She's way too hard on herself, I'm sure she'll figure it out someday.{/i}"
    scene inertiaday1-348
    pause
    scene inertiaday1-349
    pause
    scene inertiaday1-350
    pause
    scene inertiaday1-351
    pause
    scene inertiaday1-352
    pause
    scene inertiaday1-353
    pause
    scene inertiaday1-354
    p "Next pose."
    scene inertiaday1-355
    pause
    scene inertiaday1-356
    pause
    scene inertiaday1-357
    pause
    t "..."
    scene inertiaday1-358
    t "{i}Maybe now is a good time to ask...{/i}"
    scene inertiaday1-359
    t "Hey [p], I know this is random but... why doesn't Mum want to see us anymore?"
    scene inertiaday1-360
    pause
    scene inertiaday1-361
    p "..."
    scene inertiaday1-362
    p "Don't worry about her, she's not worth thinking about if she won't try to make time for us."
    scene inertiaday1-363
    p "Remember what Dad said. She didn't want look after us anymore, so she got up and left without reason. That's pretty pathetic if you ask me."
    scene inertiaday1-364
    t "I guess you're right. It just sucks we can't see her, and it's strange she doesn't even try to contact us... I feel like there's more to it than that."
    scene inertiaday1-365
    t "But I trust you sis, we've made it this far without her and we've been more than fine."
    scene inertiaday1-366
    p "Uh-huh, that's right, next pose Nika."
    scene inertiaday1-367
    pause
    scene inertiaday1-368
    pause
    scene inertiaday1-369
    pause
    scene inertiaday1-370
    pause
    scene inertiaday1-371
    pause
    scene inertiaday1-372
    pause
    scene inertiaday1-373
    pause
    scene inertiaday1-374
    p "Next pose, slowpoke."
    scene inertiaday1-375
    pause
    scene inertiaday1-376
    pause
    scene inertiaday1-377
    pause
    scene inertiaday1-378
    pause
    scene inertiaday1-379
    pause
    scene inertiaday1-380
    t "This is fucked."
    scene inertiaday1-381
    p "Haha, I know! Just hold it a bit longer."
    scene inertiaday1-382
    pause
    scene inertiaday1-383
    p "Next."
    scene inertiaday1-384
    pause
    scene inertiaday1-385
    pause
    scene inertiaday1-386
    pause
    scene inertiaday1-387
    pause
    scene inertiaday1-388
    t "This is fun, but I'm so unflexible."
    scene inertiaday1-389
    p "Is there anything you don't complain about? Try this one then, grandma."
    scene inertiaday1-390
    pause
    scene inertiaday1-391
    pause
    scene inertiaday1-392
    p "Now arch your back."
    scene inertiaday1-393
    pause
    scene inertiaday1-394
    pause
    scene inertiaday1-395
    t "I bet this is Jen's favourite position."
    scene inertiaday1-396
    p "Haha! Shut up, you cheeky bitch."
    scene inertiaday1-397
    t "Hehe, am I wrong?"
    scene inertiaday1-398
    t "..."
    scene inertiaday1-399
    pause
    scene inertiaday1-400
    pause
    scene inertiaday1-401
    j "Hi girls... is Ryan home? I'm here for training."
    scene inertiaday1-402
    p "Uh... no, I think he's still out."
    scene inertiaday1-403
    j "Okay, I'll just wait for him then."
    scene inertiaday1-404
    pause
    scene inertiaday1-405
    pause
    scene inertiaday1-406
    pause
    scene inertiaday1-407
    pause
    scene inertiaday1-408
    pause
    scene inertiaday1-409
    t "..."
    scene inertiaday1-410
    t "I think he's staring at our asses..."
    scene inertiaday1-411
    p "Yeah, I think so too..."
    menu:
        "Tell him to wait inside.":
            jump ignore01
        "Tease him first.":
            jump teasehim01
label ignore01:
    scene inertiaday1-412
    p "You can go wait for Dad inside, Jon..."
    scene inertiaday1-413
    p "I'm sure he'll be back soon."
    scene inertiaday1-414
    t "Yeah, I'm sure he will!"
    scene inertiaday1-415
    pause
    scene inertiaday1-416
    pause
    scene inertiaday1-417
    pause
    scene inertiaday1-418
    pause
    scene inertiaday1-419
    t "What a weirdo."
    scene inertiaday1-420
    p "Haha, yeah, he's a bit of a strange one."
    scene inertiaday1-421
    t "Anyway, I had a wonderful session, let's do it again soon."
    scene inertiaday1-422
    p "Of course, Nika. You did great today... and I'll be sure to bring you a walker for next time, grandma."
    scene inertiaday1-423
    t "Haha, fuck off. Anyway, I could use a shower, I'm all hot and sweaty! Did you want to join? I need to talk to you about something actually."
    scene inertiaday1-424
    p "Sure thing, I'll go get my clothes and meet you there."
    scene inertiaday1-425
    t "See ya soon."
    jump bedroom015toy
    scene inertiaday1-427
    p "{i}I really need to talk to Marcus about Jon, he's honestly been acting a bit strange around Tenika and I...{/i}"
    scene inertiaday1-428
label teasehim01:
    p "Don't worry about him, he's harmless."
    scene inertiaday1-429
    t "If you say so..."
    scene inertiaday1-430
    pause
    scene inertiaday1-431
    t "{i}I can tell he's staring at our asses, I guess a little teasing wouldn't hurt.{/i}"
    scene inertiaday1-432
    pause
    scene inertiaday1-430
    pause
    scene inertiaday1-433
    pause
    scene inertiaday1-434
    pause
    scene inertiaday1-435
    j "..."
    scene inertiaday1-434
    pause
    scene inertiaday1-437
    pause
    scene inertiaday1-438
    pause
    scene inertiaday1-439
    p "All done!"
    jump ignore01
label bedroom015toy:
    scene inertiaday1-441
    pause
    scene inertiaday1-442
    pause
    scene inertiaday1-443
    pause
    scene inertiaday1-444
    pause
    scene inertiaday1-445
    p "Huh...?"
    scene inertiaday1-446
    pause
    scene inertiaday1-447
    p "{i}Oh...{/i}"
    scene inertiaday1-448
    p "{i}Really...!{i}"
    scene inertiaday1-456
    pause
    p "{i}An anal plug?"
    scene inertiaday1-457
    p "{i}Who the hell would buy me this?{/i}"
    scene inertiaday1-458
    p "{i}I mean, at least the colour is nice... but I've never tried using one before.{/i}"
    scene inertiaday1-459
    p "{i}Bit strange, but whatever. I should hide this.{/i}"
    scene inertiaday1-460
    p "{i}I better hurry up, Nika's waiting."
    scene inertiaday1-461
    pause
    scene inertiaday1-462
    p "{i}Anyway, Nika is probably waiting for me by now; it sounded important.{/i}"
    scene inertiaday1-463
    pause
    scene inertiaday1-464
    pause
    scene inertiaday1-465
    pause
    scene inertiaday1-466
    pause
    scene inertiaday1-467
    pause
    scene inertiaday1-468
    pause
    scene inertiaday1-469
    p "{i}Hmmm...{/i}"
    scene inertiaday1-470
    p "{i}Where's Nika?{/i}"
    scene inertiaday1-471
    p "{i}Maybe she's in the other bathroom?{/i}"
    scene inertiaday1-472
    t "{font=arial.ttf}{i}♫ I get a little bit nervous... around you. Get a little bit stressed out... when I think about you... ♫{i}{/font}"
    scene inertiaday1-473
    t "{font=arial.ttf}{i}♫ Get a little excited. Baby, when I think about youuu, yeah! ♫{i}{i}{/font}"
    p "{i}How cute, she's singing, interesting song choice though..."
    scene inertiaday1-474
    p "Nika, why are you using Dad's bathroom?"
    scene inertiaday1-475
    t "The stupid hot water won't work over that side of the house, there's no way I'm having a cold shower!"
    scene inertiaday1-476
    p "First world problems, huh?"
    scene inertiaday1-478
    t "I don't see {i}you{/i} using the other one."
    scene inertiaday1-477
    p "Yeah, whatever, so what did you want to talk about?"
    scene inertiaday1-479
    t "Uhh..."
    scene inertiaday1-480
    pause
    scene inertiaday1-481
    pause
    scene inertiaday1-482
    p "C'mon, Nika, you can tell me anything."
    scene inertiaday1-483
    t "Fine... well about that you photo you helped me with."
    scene inertiaday1-484
    t "That might've been for a girl..."
    scene inertiaday1-485
    p "Ha, interesting..."
    p "{i}She's so cute, acting all nervous..."
    scene inertiaday1-486
    t "You're not weirded out, are you?"
    scene inertiaday1-487
    p "Not at all."
    scene inertiaday1-488
    p "I'm a little relieved actually."
    scene inertiaday1-489
    p "Thought I might've been the black sheep in the family."
    scene inertiaday1-490
    t "Huh, really!"
    scene inertiaday1-491
    t "Here I was thinking the same."
    scene inertiaday1-492
    pause
    scene inertiaday1-493
    pause
    scene inertiaday1-494
    p "Now scoot over a bit."
    scene inertiaday1-495
    p "So... do I know this girl?"
    scene inertiaday1-496
    t "Do you remember my friend Amy from school?"
    scene inertiaday1-498
    p "Uhh, was she the... blonde one?"
    p "{i}Nika has always had a lot of friends, and I've never quite been able to remember them all."
    scene inertiaday1-497
    t "Noooo, silly, the brunette one."
    scene inertiaday1-499
    p "Ohhh... that Amy, right, she's a cutie."
    scene inertiaday1-500
    t "Trust me, I know."
    scene inertiaday1-501
    t "And I'm sure you'll be reminded later."
    scene inertiaday1-502
    p "What's that supposed to mean?"
    scene inertiaday1-503
    p "{i}Wasn't expecting that...{/i}"
    scene inertiaday1-504
    p "{i}Gotta admit though, I'm proud of Nika! That couldn't have been easy.{/i}"
    scene inertiaday1-505
    p "{i}Amy is stunning from what I can remember, I wouldn't mind someone like that...{/i}"
    scene inertiaday1-506
    p "{i}Especially right about now...{/i}"
    scene inertiaday1-507
    pause
    scene inertiaday1-508
    pause
    scene inertiaday1-509
    pause
    scene inertiaday1-510
    p "Mmmm..."
    $ renpy.movie_cutscene("play01.webm", loops=-1)
    scene inertiaday1-511
    p "Ah... fuck..."
    scene inertiaday1-512
    p "..."
    scene inertiaday1-513
    p "This feels so good..."
    scene inertiaday1-514
    p "I'm close..."
    scene inertiaday1-515
    play sound "dooropen.ogg"
    pause
    scene inertiaday1-516
    p "Huh...?"
    scene inertiaday1-517
    je "..."
    scene inertiaday1-518
    je "Putting your Dad's bathroom to good use I see."
    scene inertiaday1-519
    p "{i}Shit... this is so awkward.{/i}"
    scene inertiaday1-520
    p "It's not what it looks like..."
    scene inertiaday1-521
    je "Really?"
    scene inertiaday1-522
    je "'Cause to me it looks like you might be a bit weak at the knees."
    scene inertiaday1-523
    pause
    scene inertiaday1-524
    pause
    scene inertiaday1-525
    je "Trust me."
    scene inertiaday1-526
    je "We've all been there before."
    scene inertiaday1-527
    je "Haven't we?"
    scene inertiaday1-528
    p "Mmm..."
    p "{i}Trust Jen to know...{/i}"
    scene inertiaday1-529
    je "You may want to look into finding something to release that tension."
    menu:
        "Flirt with [p]":
            jump jenflirt01
        "Say goodbye to [p]":
            jump jennoflirt01
label jennoflirt01:
    scene inertiaday1-530
    je "Anyway, have fun..."
    je "See you later, [p]."
    scene inertiaday1-531
    p "Bye, Jen..."
    scene inertiaday1-532
    scene
    scene inertiaday1-533
    scene
    scene inertiaday1-534
    p "Well, that was awkward..."
    jump leavebathroom01
label jenflirt01:
    je "Or possibly..."
    scene inertiaday1-536
    je "...someone."
    scene inertiaday1-537
    je "Let me know if you ever need a hand..."
    je "or... something else."
    scene inertiaday1-538
    p "Thanks for the offer Jen, I'll, ah... have to think about it!"
    scene inertiaday1-530
    je "Enjoy yourself..."
    je "See you later, [p]."
    scene inertiaday1-534
    p "Well, that was awkward..."
    scene inertiaday1-535
    p "Gotta admit though I'm... kinda turned on."
label leavebathroom01:
    scene inertiaday1-539
    pause
    scene inertiaday1-540
    pause
    scene inertiaday1-541
    pause
    scene inertiaday1-542
    pause
    scene inertiaday1-543
    pause
    scene inertiaday1-544
    pause
    scene inertiaday1-545
    pause
    scene inertiaday1-546
    pause
    scene inertiaday1-547
    pause
    scene inertiaday1-548
    pause
    scene inertiaday1-549
    pause
    scene inertiaday1-550
    scene inertiaday1-551
    scene inertiaday1-552
    scene inertiaday1-553
    pause
    scene inertiaday1-554
    pause
    scene inertiaday1-555
    play sound "ringtone.ogg"
    pause
    scene inertiaday1-556
    pause
    stop sound
    scene inertiaday1-557
    m "Hello, Alabama circumcision centre, Marcus speaking."
    scene inertiaday1-558
    m "You flop it, we chop it!"
    scene inertiaday1-568
    p "You're such an idiot, I swear."
    scene inertiaday1-569
    p "What ya up to?"
    scene inertiaday1-559
    m "Oh you know..."
    scene inertiaday1-560
    m "Working hard, answering calls, another day in the office really..."
    scene inertiaday1-570
    p "You're in your Jacuzzi again, aren't you?"
    scene inertiaday1-561
    m "Uhh..."
    scene inertiaday1-562
    m "Maybe."
    scene inertiaday1-571
    p "Typical Marcus, always focused on himself, never considering customer satisfaction."
    scene inertiaday1-563
    m "Don't be like that! Usually my customers are the ones cut."
    scene inertiaday1-564
    m "Get it, cut?"
    scene inertiaday1-572
    p "You're so hilarious."
    scene inertiaday1-573
    p "Ever thought about doing stand up?"
    scene inertiaday1-566
    m "My job's more of a sit-down type deal."
    scene inertiaday1-567
    m "You know what I'm saying?"
    scene inertiaday1-576
    p "I don't even know why I talk to you sometimes..."
    scene inertiaday1-566
    m "'Cause I'm the best person ever! What do you mean!?"
    scene inertiaday1-565
    m "Anyway... what'd you want to talk about?"
    scene inertiaday1-574
    p "I'm so friggin' bored at the moment."
    scene inertiaday1-575
    p "Did you want to catch up and do something?"
    scene inertiaday1-560
    m "I thought you'd never ask."
    scene inertiaday1-559
    m "I've just got some fresh wheels, want to take her for a test drive?"
    scene inertiaday1-579
    p "Oh, heck yeah!"
    scene inertiaday1-578
    p "Where should we go though?"
    scene inertiaday1-561
    m "How long's it been since you've gone to the Den?"
    scene inertiaday1-579
    p "I haven't been there in {i}ages{/i}! Last time would've been... in high school."

    scene inertiaday1-567
    m "Sounds good, I'll pick you up from your back alley in... half an hour?"
    scene inertiaday1-575
    p "Alright! I'm not dressing up though, I'm feeling kinda lazy, but I'll see you in my back alley soon!"
    scene inertiaday1-567
    m "{i}{b}*sniggers*"
    scene inertiaday1-580
    pause
    scene inertiaday1-581
    m "I bet you've been waiting to see my big black beast in your back alley for ages, haven't you?"
    scene inertiaday1-582
    p "Uh yeah..."
    scene inertiaday1-583
    p "Oh, wait a second..."
    p "You think you're funny don't ya?"
    scene inertiaday1-585
    pause
    scene inertiaday1-584
    m "Well I thought it was funny."
    scene inertiaday1-586
    m "And here I was, ready to let you drive, but now but now that you've insulted my humor I don't think I'll let you."
    scene inertiaday1-587
    p "Haha! Shut up, I don't have my license anyway, idiot."
    scene inertiaday1-588
    p "Where'd you get it?"
    scene inertiaday1-589
    m "Uh... yeah, about that..."
    scene inertiaday1-590
    m "I'll uh... tell you later."
    m "Let's kick it."
    scene inertiaday1-591
    pause
    scene inertiaday1-592
    m "You'll have to 'cum' in the front door, this time."
    scene inertiaday1-593
    p "Damn, I was really excited to try your back door."
    scene inertiaday1-594
    pause
    scene inertiaday1-595
    pause
    scene inertiaday1-596
    m "Take a ticket, my back door's by appointment only!"
    scene inertiaday1-597
    p "You're an idiot."
    scene inertiaday1-598
    pause
    scene inertiaday1-599
    pause
    scene inertiaday1-600
    pause
    scene inertiaday1-601
    pause
    scene inertiaday1-602
    pause
    scene inertiaday1-603
    p "I'm excited to see what the Den looks like, it's been so long! I hope it hasn't changed much."
    scene inertiaday1-604
    m "Apparently there's a lot of underground events and people doing recreational drugs, now."
    scene inertiaday1-605
    m "Hehe, pingas."
    scene inertiaday1-606
    p "Are you taking me to a druggie den Marcus?"
    scene inertiaday1-607
    m "No..."
    scene inertiaday1-608
    m "That's just what I've heard."
    scene inertiaday1-609
    m "Hopefully there's no crackheads around."
    scene inertiaday1-610
    p "Yeah yeah, well c'mon then... show me what this car can really do!"
    $ renpy.movie_cutscene("car.webm", loops=-0)
    scene inertiaday1-611
    pause
    scene inertiaday1-612
    m "I remember when we used to ditch school to come here and smoke up."
    m "I'm not gonna lie though..."
    scene inertiaday1-613
    m "It smells kinda... funky down here."
    scene inertiaday1-614
    p "Yeah, I wonder what that is?"
    scene inertiaday1-615
    m "Aside from the smell, it looks better than it used to."
    scene inertiaday1-616
    m "Brings back a lot of memories, do you remember wh-"
    scene inertiaday1-617
    "{i}MmmmmmMMMMM...{/i}"
    scene inertiaday1-618
    pause
    scene inertiaday1-617
    "{i}UH Uhh UHHhhhhhh...{/i}"
    scene inertiaday1-618
    pause
    m "What the hell was that?"
    scene inertiaday1-619
    p "Ergh..."
    scene inertiaday1-620
    m "Come on, let's check it out."
    scene inertiaday1-621
    pause
    scene inertiaday1-622
    pause
    scene inertiaday1-623
    m "...Holy shit..."
    scene inertiaday1-624
    pause
    scene inertiaday1-625
    m "Psst, c'mere..."
    scene inertiaday1-626
    p "Ooh, what is it, what is it? I'm so scared!"
    scene inertiaday1-627
    m "{i}This girl...{/i}"
    m "I'm serious, look."
    scene inertiaday1-628
    pause
    scene inertiaday1-629
    p "..."
    scene inertiaday1-630
    p "Oh my god!"
    scene inertiaday1-638
    pause
    scene inertiaday1-639
    pause
    scene inertiaday1-630
    menu:
        "Kinky response":
            jump kinky01
        "Sarcastic Response":
            jump sarcastic01
label kinky01:
    scene inertiaday1-631
    p "That's actually kinda kinky..."
    p "Sooooo... not just a {i}druggie den{/i}, huh?"
    scene inertiaday1-632
    jump Marcusresponse01
label sarcastic01:
    p "Sooooo... just a {i}druggie den{/i}, huh?"
    scene inertiaday1-633
label Marcusresponse01:
    m "I swear I had no idea."
    scene inertiaday1-634
    play sound "ringtone.ogg"
    pause
    scene inertiaday1-635
    pause
    scene inertiaday1-636
    pause
    scene inertiaday1-637
    pause
    scene inertiaday1-640
    pause
    scene inertiaday1-641
    "..."
    stop sound
    scene inertiaday1-642
    p "RUN!"
    m "TO THE BACK DOOR!"
    scene inertiaday1-643
    m "I knew we'd get to the back door sometime tonight."
    scene inertiaday1-644
    p "You've always been obsessed with my back door, haven't ya?"
    scene inertiaday1-645
    m "Ever since {i}that{/i} cheerleading practice."
    scene inertiaday1-644
    p "Oh my god, you still remember that, I almost died of embarassment."
    scene inertiaday1-645
    m "The pattern on those undies is burned into my memory, haha! Let's get out of here."
    scene inertiaday1-646
    pause
    m "Considering that didn't go as planned, wanna grab a coffee?"
    p "Yeah, your shout though; surely that job of yours gives you a good cut."
    m "Haha, it sure does..."
    scene inertiaday1-647
    pause
    scene inertiaday1-648
    pause
    scene inertiaday1-649
    pause
    scene inertiaday1-650
    pause
    scene inertiaday1-651
    pause
    scene inertiaday1-652
    pause
    scene inertiaday1-653
    p "Hey Jade!"
    scene inertiaday1-654
    ja "Hey guys! You're out later than usual!"
    scene inertiaday1-655
    ja "What'ya been up to?"
    scene inertiaday1-656
    m "Remember the Den we used to go to when we were younger?"
    scene inertiaday1-657
    m "Let's just say it's not the Den we once knew..."
    scene inertiaday1-659
    ja "Ah, you guys only just found out about that, huh?"
    scene inertiaday1-658
    p "We had a first class viewing to say the least..."
    scene inertiaday1-660
    p "Can we please grab 2 large cappuccinos, 1 with an extra shot, 1 sugar and the other flat."
    scene inertiaday1-661
    ja "Sure, I'll fix that up for you, take a seat anywhere you like."
    scene inertiaday1-662
    pause
    scene inertiaday1-663
    pause
    m "Look at you, remembering my order! We could definitely use someone like you around the office."
    scene inertiaday1-664
    p "You be careful, or you'll be the next one on the chopping block!"
    scene inertiaday1-665
    m "Oh no! Not the chopping block!"
    scene inertiaday1-666
    m "Who's to say I haven't already been?"
    scene inertiaday1-667
    p "Like I needed to know that!"
    scene inertiaday1-668
    p "Anyway, I need to use the bathroom, I'll be back in a minute."
    scene inertiaday1-669
    m "First Dad left for milk, now you're leaving for the bathroom..."
    scene inertiaday1-670
    p "Haha, shut up you idiot! I won't be long."
    scene inertiaday1-671
    m "Hehe, see ya soon."
    scene inertiaday1-672
    pause
    scene inertiaday1-673
    p "Hey Jade!"
    scene inertiaday1-674
    ja "Oh!"
    scene inertiaday1-675
    ja "You startled me, what's up!"
    scene inertiaday1-676
    p "Haha, sorry."
    scene inertiaday1-677
    p "Is the cafe bathroom still broken?"
    scene inertiaday1-678
    ja "Yeah... we're still waiting on a plumber, so you'll have to use the one down the street. Sorry!"
    scene inertiaday1-679
    p "That's all good, thanks."
    scene inertiaday1-680
    pause
    scene inertiaday1-681
    pause
    scene inertiaday1-682
    pause
    scene inertiaday1-683
    pause
    scene inertiaday1-684
    p "{i}What a crazy night! I wasn't expecting any of this.{/i}"
    scene inertiaday1-685
    p "{i}Especially seeing that girl... restrained...{/i}"
    scene inertiaday1-686
    p "{i}I wonder why people would want to do it out there in the first place.{/i}"
    scene inertiaday1-687
    p "{i}I'm so glad Marcus asked me out tonight. He's always been so much fun, I don't know what I'd do without him.{/i}"
    scene inertiaday1-688
    pause
    scene inertiaday1-689
    p "Ahhh!"
    scene inertiaday1-690
    p "What the fuck!"
    scene inertiaday1-691
    p "{i}Who the hell put a glory hole here...?{/i}"
    scene inertiaday1-692
    p "{i}This is so awkward! What do I do!?{/i}"
    menu:
        "Touch it":
            jump handy01
        "Teach him a lesson":
            jump nohandy01
label nohandy01:
    scene inertiaday1-693
    p "..."
    scene inertiaday1-694
    p "{i}I'll show this perv.{/i}"
    scene inertiaday1-695
    p "Give me one second... let me take these pants off..."
    scene inertiaday1-696
    pause
    scene inertiaday1-697
    pause
    scene inertiaday1-698
    s "ARGHHH! MY COCK! YOU BITCH!"
    scene inertiaday1-699
    p "Oh, what?"
    scene inertiaday1-700
    p "Is that not how you give a foot job?"
    scene inertiaday1-701
    p "Fucking pervert!"
    scene inertiaday1-702
    p "Hope that didn't put a kink in your plans?"
    jump walkbacktocafe01
    scene inertiaday1-692
label handy01:
    p "{i}Holy shit, that's huge...{/i}"
    scene inertiaday1-703
    p "{i}Maybe a little touch wouldn't hurt...{/i}"
    scene inertiaday1-704
    p "{i}He's so hard at the moment.{/i}"
    scene inertiaday1-705
    p "{i}I probably shouldn't be touching a stranger's cock.{/i}"
    p "{i}On the other hand... what's the worst that could happen?{/i}"
    scene inertiaday1-706
    pause
    scene inertiaday1-707
    pause
    scene inertiaday1-708
    pause
    scene inertiaday1-709
    pause
    scene inertiaday1-710
    pause
    scene inertiaday1-711
    pause
    scene inertiaday1-712
    p "{i}Oh my god...!{i}"
    scene inertiaday1-713
    p "{i}He came so quickly.{i}"
    scene inertiaday1-714
    p "{i}I wasn't expecting that, but..."
    p "{i}...I'm kinda turned on...{i}"
    p "{i}I should probably get out of here.{i}"
label walkbacktocafe01:
    scene inertiaday1-715
    pause
    scene inertiaday1-716
    pause
    scene inertiaday1-717
    pause
    scene inertiaday1-718
    pause
    scene inertiaday1-719
    pause
    scene inertiaday1-720
    p "Thanks for that, Jade! Hopefully the toilets are fixed soon."
    scene inertiaday1-721
    p "Are you ready to head off, Marcus?"
    scene inertiaday1-722
    p "After tonight, I've gotta admit I'm pretty exhausted."
    scene inertiaday1-723
    m "Too much excitement for one night I see, ready to go when you are."
    scene inertiaday1-724
    m "Here's your coffee."
    scene inertiaday1-725
    p "Thanks, Marcus."
    scene inertiaday1-726
    p "Good luck with the rest of your shift and thanks for the coffee, Jade. We'll have to catch up some time soon."
    scene inertiaday1-727
    ja "No problem, great to see you two again! You're welcome back any time."
    scene inertiaday1-728
    ja "And I'll definitely take you up on that offer, see you guys around."
    scene inertiaday1-729
    pause
    scene inertiaday1-730
    ad "Oi, big tits!"
    scene inertiaday1-731
    ad "Give us a show, yeah!?"
    scene inertiaday1-733
    pause
    scene inertiaday1-734
    pause
    scene inertiaday1-733
    pause
    scene inertiaday1-735
    m "Cheers, lads! Glad you've noticed I've been workin' out."
    scene inertiaday1-736
    p "Where'd you get the sunnies from?"
    scene inertiaday1-737
    m "The glovebox."
    scene inertiaday1-738
    p "Uh-huh..."
    scene inertiaday1-739
    pause
    scene inertiaday1-740
    pause
    scene inertiaday1-731
    pause
    scene inertiaday1-732
    pause
    scene inertiaday1-741
    ad "Very funny, smartass."
    scene inertiaday1-742
    ad "That shirt won't be the only thing you're losing tonight! Gimme ya fucking keys!"
    scene inertiaday1-745
    m "Settle down, saddle club. Here, I'll get them for ya."
    scene inertiaday1-746
    m "I'm sure they're in my pocket... somewhere..."
    scene inertiaday1-747
    m "Just give me a sec, lads."
    scene inertiaday1-748
    m "Feels like they're just... down... here..."
    scene inertiaday1-743
    ad "Hurry up, dickhead! You've got five seconds!"
    scene inertiaday1-749
    m "Calm down, Gimpy, I've got them right here. Three, two, one and..."
    scene inertiaday1-750
    m "Here you go, sit on this!"
    scene inertiaday1-744
    ad "That's it!"
    scene inertiaday1-751
    ad "You're fuckin' dead!"
    scene inertiaday1-751
    play sound "guncock.ogg"
    pause
    scene inertiaday1-752
    pause
    stop sound
    scene inertiaday1-753
    ja "I suggest you boys get away from my store!"
    ja "..."
    scene inertiaday1-754
    ja "NOW!"
    scene inertiaday1-755
    ad "...hmph."
    scene inertiaday1-756
    ad "Let's get out of here, Brodie."
    scene inertiaday1-757
    ja "Yeah, that's right! You just {i}keep on walkin'{/i}."
    scene inertiaday1-758
    ad "Fucking bitch, we'll be back."
    scene inertiaday1-759
    ja "Go on and try it! Next time, I won't let you off so easily."
    scene inertiaday1-760
    pause
    p "Damn, Jade! That was so fucking {i}BADASS!{/i}"
    scene inertiaday1-761
    ja "Those assholes are always harassing people and making business tough."
    scene inertiaday1-762
    ja "You guys seemed to handle them alright though."
    scene inertiaday1-763
    p "Uhh... I wouldn't say handled... more {i}annoyed{/i}."
    scene inertiaday1-764
    m "Look, I had it fully under control. I was an absolute gentleman."
    scene inertiaday1-765
    ja "Yeah, you sure about that one, chief?"
    scene inertiaday1-766
    m "Look, I can't help that I'm such a natural people pleaser."
    scene inertiaday1-767
    m "Have a lovely night, Jade!"
    scene inertiaday1-768
    p "Seriously, thanks again for that. Who knows what would've happened if you weren't here."
    scene inertiaday1-769
    ja "Any time, be sure to stop by again soon; It's always great seeing you. I'll be working all week."
    scene inertiaday1-770
    p "No worries Jade, I'll try and stop by."
    scene inertiaday1-771
    pause
    m "Do you think he meant what he said about my tits, or was he just saying that?"
    scene inertiaday1-772
    p "Shut up, moron. You're such an idiot, you know. You could've got yourself hurt."
    $ renpy.movie_cutscene("awhile.webm", loops=-0)
    scene inertiaday1-773
    pause
    scene inertiaday1-774
    p "Thanks for taking me home... I had a great night to say the least."
    scene inertiaday1-775
    m "I gotta admit it was a bit more {i}eventful{/i} than I was expecting."
    scene inertiaday1-776
    m "To say the least..."
    scene inertiaday1-777
    p "You're an idiot!"
    scene inertiaday1-778
    m "That's why you love me."
    scene inertiaday1-779
    m "Anyway, it's getting late. I should probably get back home."
    scene inertiaday1-780
    p "Yeah, me too, Dad'll kill me if I'm out any later."
    menu:
        "Kiss":
            jump kiss
        "Don't kiss":
            jump dontkiss
    scene inertiaday1-781
label dontkiss:
    p "See ya later, Marcus."
    scene inertiaday1-782
    m "Rock on, sis."
    scene inertiaday1-783
    m "We'll have to do this again, sometime."
    scene inertiaday1-784
    p "I'm so down for that. Good night."
    jump backhome01
label kiss:
    scene inertiaday1-780
    p "{i}Tonight was amazing and it was kinda ...{plain}hot{/plain}... how Marcus handled the whole thing too.{/i}"
    scene inertiaday1-785
    p "{i}I wonder if he's thinking the same thing...?{/i}"
    scene inertiaday1-786
    i "{i}Fuck it, why not.{/i}"
    scene inertiaday1-787
    pause
    scene inertiaday1-788
    pause
    scene inertiaday1-789
    m "Woah...! What was that for?"
    scene inertiaday1-790
    p "I just had a lot of fun tonight. You got a problem with that?"
    scene inertiaday1-791
    m "Not at all! That was definitely a great way to finish off the night."
    scene inertiaday1-792
    p "And now..."
    p "... you can go finish yourself off!"
    scene inertiaday1-793
    p "Bye, Marcus."
    m "Cheeky bitch! See ya soon, [p]."
label backhome01:
    scene inertiaday1-794
    pause
    scene inertiaday1-795
    pause
    scene inertiaday1-796
    p "{i}Finally home. I can't wait to hop into bed.{/i}"
    scene inertiaday1-797
    t "WOOOOOO!"
    scene inertiaday1-798
    t "YEEEEEEHAWWWW!"
    scene inertiaday1-799
    t "RIDE 'EM, COWBOY!"
    scene inertiaday1-800
    a "Hahahaha!"
    scene inertiaday1-801
    p "What on {i}Earth{/i} are you two doing?"
    scene inertiaday1-802
    p "Oh, Hi Amy... it's been a while."
    scene inertiaday1-803
    pause
    scene inertiaday1-804
    pause
    scene inertiaday1-805
    a "I knowwww, right? It's been WAY too long! You look incredible, by the way, [p]!"
    scene inertiaday1-806
    p "Likewise Amy. But... what's with the outfits?"
    scene inertiaday1-807
    t "Don't tell me you've forgot the costume party..."
    scene inertiaday1-808
    p "OH DAMN! That's tomorrow, isn't it!"
    scene inertiaday1-809
    t "Ha ha! Nice one, idiot!"
    scene inertiaday1-811
    p "I'm a dumbass..."
    scene inertiaday1-810
    a "I've got some spare outfits, why don't you drop by the store tomorrow and try them out."
    scene inertiaday1-812
    p "Honestly, if you wouldn't mind... that'd be awesome! Thanks Amy."
    scene inertiaday1-814
    a "It's no problem at all, it'd be my pleasure."
    t "See? Isn't she great?"
    scene inertiaday1-813
    p "Indeed she is. Anyway, I'll leave you girls to it... try not to make too much noise."
    scene inertiaday1-814
    t "Night night!"
    a "Great seeing you, [p]. Good night."
    scene inertiaday1-815
    pause
    scene inertiaday1-816
    pause
    scene inertiaday1-817
    pause
    t "Gotcha!"
    scene inertiaday1-818
    p "{i}They seem great for each other.{/i}"
    scene inertiaday1-819
    pause
    scene inertiaday1-821
    pause
    scene inertiaday1-822
    p "{i}Wow... what a day..."
    scene inertiaday1-823
    p "{i}I don't think I've had one full of so many surprises in a long time."
    scene inertiaday1-824
    p "{i}Not to mention Amy, she sure has {i}matured...{/i}"
    scene inertiaday1-825
    p "{i}And maybe Jen was right, I do need to find something to release that tension..."
    scene inertiaday1-826
    pause
    scene inertiaday1-827
    pause
    scene inertiaday1-828
    pause
    scene inertiaday1-829
    pause
    scene inertiaday1-830
    p "{i}..."
    scene inertiaday1-831
    p "{i}Hmm..."
    scene inertiaday1-832
    p "{i}Actually..."
    scene inertiaday1-833
    pause
    scene inertiaday1-834
    pause
    scene inertiaday1-835
    p "{i}I may as well give it a shot."
    p "{i}I mean, no harm in trying... right?"
    scene inertiaday1-836
    pause
    scene inertiaday1-837
    pause
    scene inertiaday1-838
    pause
    scene inertiaday1-839
    p "{i}I have no idea how this is even going to fit..."
    scene inertiaday1-840
    p "I wonder if it'll feel good?"
    scene inertiaday1-841
    pause
    scene inertiaday1-842
    p "{i}There's no way..."
    scene inertiaday1-843
    pause
    scene inertiaday1-844
    p "{i}Ok [p], just relax..."
    scene inertiaday1-845
    $ renpy.movie_cutscene("assplay01.webm", loops=-1)
    scene inertiaday1-846
    p "{i}I can feel it going deeper. It hurts a little, though..."
    scene inertiaday1-847
    p "{i}Maybe I should try a different position..."
    scene inertiaday1-848
    pause
    $ renpy.movie_cutscene("assplay02.webm", loops=-1)
    scene inertiaday1-849
    p "{i}This is already starting to feel a bit easier..."
    p "{i}I didn't expect it to feel {i}nice{/i}, too."
    scene inertiaday1-850
    pause
    scene inertiaday1-851
    pause
    scene inertiaday1-850
    pause
    scene inertiaday1-851
    r "[p]!"
    scene inertiaday1-852
    pause
    scene inertiaday1-853
    p "Ahh..."
    scene inertiaday1-854
    p "{i}Oh my god..."
    p "{i}Wait, my door!"
    scene inertiaday1-859
    r "I just set up the new gym! Quick, come take a look!"
    scene inertiaday1-855
    pause
    scene inertiaday1-860
    r "Are you... alright?"
    scene inertiaday1-856
    p "Yep!"
    scene inertiaday1-857
    p "I'm fiiine."
    scene inertiaday1-858
    pause
    scene inertiaday1-861
    r "Great, I can't {i}wait{/i} to show you what I've been working on all day."
    scene inertiaday1-862
    pause
    scene inertiaday1-863
    r "Are you coming... or what?"
    scene inertiaday1-864
    p "Yeah, just... give me a minute."
    scene inertiaday1-865
    r "*sigh* Hurry up, [p], I've got work in the morning."
    scene inertiaday1-866
    p "Okay..."
    scene inertiaday1-867
    pause
    scene inertiaday1-868
    p "{i}No way this is happening...{/i}"
    scene inertiaday1-869
    pause
    scene inertiaday1-870
    r "So... what do you think?"
    scene inertiaday1-871
    r "Not bad, huh!"
    scene inertiaday1-872
    p "All day... just for this?"
    scene inertiaday1-873
    r "Oh, c'mon... it was hard work setting this up, now you and Tenika can work out from home."
    scene inertiaday1-874
    p "Didn't expect a tough guy like you to be complaining over a bit of hard work."
    scene inertiaday1-875
    r "Alright smartass, you can set the next one up then!"
    scene inertiaday1-876
    r "I even bought the exercise balls you wanted! C'mon, try them out!"
    scene inertiaday1-877
    p "Uhh..."
    scene inertiaday1-878
    p "I'm not feeling so great, maybe in the morning...?"
    scene inertiaday1-880
    r "[p]... you know better than to try that with me."
    r "Now, grab the exercise ball."
    scene inertiaday1-879
    p "{i}Ah shit...{/i}"
    scene inertiaday1-881
    pause
    scene inertiaday1-882
    pause
    scene inertiaday1-883
    pause
    scene inertiaday1-884
    pause
    scene inertiaday1-885
    p "These feel great, thanks Dad."
    scene inertiaday1-886
    r "There's a reason it's called an {i}exercise{/i} ball, now try it out!"
    scene inertiaday1-887
    p "{i}This couldn't get any worse...{/i}"
    scene inertiaday1-888
    p "Okay..."
    scene inertiaday1-889
    pause
    scene inertiaday1-890
    r "See, I knew you'd like them!"
    r "And you said you weren't feeling so great either."
    scene inertiaday1-891
    p "Stretching out must've helped I guess..."
    scene inertiaday1-892
    r "Great, seeing as that helped out so much, that means you can do one more exercise."
    scene inertiaday1-893
    r "Wouldn't want you going to bed feeling sick, would we?"
    scene inertiaday1-894
    p "Uhh..."
    scene inertiaday1-895
    p "I guess not..."
    scene inertiaday1-896
    r "Now the question is... what can we do...?"
    scene inertiaday1-898
    pause
    scene inertiaday1-899
    p "What the..."
    scene inertiaday1-900
    r "Haha, I know just the thing!"
    scene inertiaday1-901
    p "Nooooooo!"
    scene inertiaday1-902
    r "That's probably the comfiest seat in the house right now!"
    r "See, you can use them for squats, too!"
    scene inertiaday1-903
    p "{i}Oh my god! Sitting on this ball is pushing it deeper in my ass...{/i}"
    p "Haha, yeah..."
    scene inertiaday1-904
    p "{i}Shit, it's so deep...{/i}"
    p "I should really be heading to bed though."
    scene inertiaday1-905
    pause
    scene inertiaday1-907
    p "Kinda have a big day tomorrow."
    scene inertiaday1-908
    p "No worries kiddo. That wasn't so hard, was it!"
    scene inertiaday1-909
    pause
    scene inertiaday1-910
    r "Are you... sure you're alright?"
    scene inertiaday1-911
    p "Yeah! I'm fine, just really exhausted!"
    scene inertiaday1-912
    p "I better head to sleep."
    p "{i}Damnit, I still need to talk to him about Mom...{/i}"
    scene inertiaday1-913
    r "Well, that's everything, have a good night [p]."
    scene inertiaday1-914
    p "Actually, there is one more thing..."
    scene inertiaday1-915
    p "Remember how you spoke to me about Mom...?"
    scene inertiaday1-921
    r "Yeah, of course I remember, why are you bringing this up?"
    scene inertiaday1-916
    p "Well, Nika is starting to ask questions..."
    scene inertiaday1-917
    p "I think she should be hearing it from you, not me."
    scene inertiaday1-922
    r "I guess I should've known she'd be curious by now."
    scene inertiaday1-923
    r "Hopefully it doesn't hurt her the same way it hurt you."
    scene inertiaday1-918
    p "I was around the same age when you first told me."
    scene inertiaday1-919
    p "It did hurt, a lot, but... I'm glad you told me the truth."
    scene inertiaday1-920
    p "Anyway, it's probably not the best thing to talk about before bed, but I thought I'd let you know."
    scene inertiaday1-924
    r "I appreciate you coming to me first, I'll be sure to talk to her soon."
    scene inertiaday1-925
    r "Just remember, I love you both."
    scene inertiaday1-926
    p "I love you too, goodnight, Dad."
    scene inertiaday1-927
    r "Go get some rest. I'm going to finish up here, goodnight."
    scene inertiaday1-929
    r "{i}Time goes so fast, I didn't expect this to come around so soon...{/i}"
    scene inertiaday1-930
    p "{i}I hope he's going to be alright and that Nika doesn't react as badly as I did...{/i}"
    scene inertiaday1-931
    p "{i}Oh god... I can... Um... still feel the buttplug in my ass! I can't... Um... I can't believe that just happened in front of Dad.{/i}"
    p "{i}It was kinda exciting though, in a way!...{/i}"
    scene inertiaday1-932
    p "{i}What the hell What am I thinking... He's my Dad!"
    p "{i}I better go check on the girls quickly, before I go work out this frustration."
    p "{i}Nika doesn't usually leave her door open.{/i}"
    scene inertiaday1-934
    pause
    scene inertiaday1-935
    pause
    scene inertiaday1-936
    p "{i}Aww."
    scene inertiaday1-937
    p "{i}They look so cute together..."
    scene inertiaday1-938
    pause
    scene inertiaday1-939
    pause
    scene inertiaday1-940
    p "{i}They must be freezing!"
scene inertiaday1-940
menu:
    "Take a closer look":
        jump closerlook01
    "Cover them up":
        jump sheeton01
label sheeton01:
    scene inertiaday1-933
    p "{i}I'd better put a blanket on them."
    scene inertiaday1-943
    pause
    scene inertiaday1-942
    pause
    scene inertiaday1-944
    p "Good night, girls."
    scene inertiaday1-945
    pause
    scene inertiaday1-946
    pause
    scene inertiaday1-947
    pause
    scene inertiaday1-948
    pause
    scene inertiaday1-949
    pause
    jump enterroom02
label closerlook01:
    scene inertiaday1-951
    pause
    scene inertiaday1-950
    pause
    scene inertiaday1-953
    pause
    scene inertiaday1-952
    p "{i}Wow, they really must be cold."
    scene inertiaday1-954
    pause
    scene inertiaday1-955
    pause
    p "{i}Oh my... Amy really has grown."
    scene inertiaday1-956
    pause
    p "{i}I should probably head to bed before these thoughts become to much."
    scene inertiaday1-957
    p "{i}Or in case they wake up."
    scene inertiaday1-958
    pause
    scene inertiaday1-959
    pause
    scene inertiaday1-960
    pause
    scene inertiaday1-961
    pause
label enterroom02:
    scene inertiaday1-962
    p "{i}This has been one crazy day..."
    scene inertiaday1-963
    pause
    scene inertiaday1-964
    p "Really! {i}Another{/i} present?"
    scene inertiaday1-965
    p "{i}Who keeps doing this?"
    scene inertiaday1-966
    p "{i}Judging by the size of this box I'm hoping it's not another buttplug."
    scene inertiaday1-967
    pause
    scene inertiaday1-968
    p "{i}Oh, wow!"
    scene inertiaday1-969
    pause
    scene inertiaday1-970
    p "{i}Well, this is definitely a bit more appealing."
    scene inertiaday1-971
    p "{i}This looks so expensive!"
    scene inertiaday1-972
    p "{i}I love it already!"
    scene inertiaday1-973
    p "{i}There's not much point in them just sitting there!"
    scene inertiaday1-974
    pause
    scene inertiaday1-975
    pause
    scene inertiaday1-976
    pause
    scene inertiaday1-977
    pause
    scene inertiaday1-978
    pause
    scene inertiaday1-979
    p "Oh my god!"
    scene inertiaday1-981
    pause
    scene iu25-1
    p "Well... what do you think?"
    menu:
        "Love it...":
            jump loveit
        "Looks shit":
            jump looksshit
label looksshit:
    scene iu25-2
    p "..."
    scene iu25-3
    p "I'll kick yo ass!"
    jump sleeptime
label loveit:
    scene iu25-4
    p "Aww, why thank you"
    jump sleeptime
label sleeptime:
    scene iu25-5
    p "{i}Anyway, I better get some sleep."
    play sound "phonevib.ogg"
    scene iu25-5
    pause
    scene iu25-6
    pause
    p "{i}I wonder who that could be?"
    scene iu25-25
    pause
    p "{i}Oh It's Marty, I wonder what he wants at this hour."
    scene iu25-7
    ma "Hi [p] I showed the boss your photos and he loves everything about you..."
    ma "Can you come to 53 Vogue Place tomorrow at mid-day please."
    scene iu25-8
    p "Heck yes!"
    scene iu25-9
    p "{i}What a confidence boost!"
    scene iu25-10
    p "{i}This is so cool, like a dream come true!"
    scene iu25-10
    play sound "phonemess.ogg"
    scene iu25-11
    ma "Only thing is... The boss is requesting a selfie from you, can you please send one through now."
    scene iu25-12
    p "{i}Uhhh... I'm sure that would be fine."
    scene iu25-13
    p "{i}Luckily I've got something amazing on right now."
    scene iu25-14
    pause
    scene iu25-15
    pause
    play sound "phonecam.ogg"
    scene iu25-16
    pause
    scene iu25-18
    play sound "phonesend.ogg"
    pause
    scene iu25-19
    p "{i}There's no way the boss won't like that."
    scene iu25-19
    pause
    scene iu25-20
    play sound "phonemess.ogg"
    ma "Wow, I love it... the Only thing is the boss is really picky... he needs to see you in better lighting."
    ma "Can you take another one around the house please, remember this needs to impress."
    scene iu25-21
    p "{i}Are you serious..."
    scene iu25-22
    p "{i}The only other good lighting in this house is in the kitchen... I hope no one is awake."
    scene iu25-23
    p "{i}On the other hand who doesn't like a bit of adventure..."
    scene iu25-24
    p "{i}Please don't get caught..."
    scene iu25-37
    p "{i}But, what if I do..."
    scene iu25-38
    pause
    scene iu25-39
    p "{i}Phew... no one is here."
    scene iu25-40
    p "{i}I gotta be quick."
    scene iu25-41
    p "{i}Wow, This lighting is so much better!"
    scene iu25-42
    play sound "phonecam.ogg"
    p "{i}CHEEESE!"
    scene iu25-26
    play sound "phonesend.ogg"
    scene iu25-27
    p "{i}This better be good enough..."
    play sound "phonemess.ogg"
    scene iu25-28
    ma "Wow... the boss is really impressed with the lighting... but he needs to see more angles of you..."
    ma "Please set your camera up and take some full body shots."
    scene iu25-29
    p "Uhh..."
    scene iu25-31
    p "{i}This is nerve racking what if someone comes in..."
    scene iu25-32
    p "{i}I'd better do it, I need this job. But after that, no more."
    scene iu25-43
    pause
    scene iu25-33
    pause
    scene iu25-34
    p "{i}That should be okay, I'll put it on the timer."
    scene iu25-35
    pause
    scene iu25-36
    pause
    scene iu25-44
    p "{i}I'll just try some random poses, I guess..."
    scene iu25-45
    play sound "phonecam.ogg"
    pause
    scene iu25-46
    play sound "phonecam.ogg"
    pause
    scene iu25-47
    play sound "phonecam.ogg"
    pause
    scene iu25-48
    play sound "phonecam.ogg"
    pause
    scene iu25-49
    play sound "phonesend.ogg"
    p "{i}That should be enough..."
    scene iu25-50
    play sound "phonemess.ogg"
    ma "Wow [p], the boss loves you a lot and he's made a special request..."
    ma "He would like to see you without a bra, but you can cover your nipples. The more open you are the better."
    scene iu25-51
    p "{i}Without my bra...?"
    scene iu25-52
    p "{i}It feels like he just wants to see me naked but what if its legit..."
    scene iu25-53
    p "{i}NAH, YOU KNOW WHAT!"
    scene iu25-54
    play sound "phonesend.ogg"
    p "Sure give me a second..."
    play sound "phonecall.ogg"
    scene iu25-118
    pause
    scene iu25-130
    play sound "ringtone.ogg"
    m "..."
    scene iu25-131
    m "{i}Ayy misses me already!"
    scene iu25-132
    stop sound
    m "Howdy doodly neighborino."
    scene iu25-119
    p "Marcus I need a favour... sort of now!"
    scene iu25-133
    m "Wow, so impatient! What do you need!?"
    scene iu25-120
    p "I need you to send me a nudey but please don't ask questions."
    scene iu25-134
    m "Oh I see... when it's the girl asking for nudes its all Hunky Dory, but when a guy asks he's a sexual predator."
    scene iu25-121
    p "Haha shutup. Please just do this one thing for me, I'll explain later."
    scene iu25-135
    play sound "phonecam.ogg"
    m "Already on it!"
    scene iu25-122
    p "Thanks."
    scene iu25-137
    scene iu25-122
    pause
    scene iu25-123a
    play sound "phonemess.ogg"
    pause
    p "Oh my fucking god! That's perfect!"
    scene iu25-124
    p "Thank you so much, I owe you big time."
    scene iu25-138
    m "Yeah ya do."
    scene iu25-139
    m "I'm going to go back to helicoptering my doodle in the wind, bye bye!"
    scene iu25-125
    p "You're an absolute tossa. See ya!"
    scene iu25-126
    play sound "phonesend.ogg"
    p "Muhaha... and send."
    scene iu25-126
    pause
    scene iu25-126
    play sound "phonemess.ogg"
    ma "WHAT THE FUCK???"
    scene iu25-127
    p "{i}Hahaha, see ya tomorrow, Marty!"
    scene iu25-128
    p "{i}I hope that doesn't come back to bite me in the ass..."
    scene iu25-129
    p "{i}But it was so worth it..."
    scene iu25-57
    p "{i}Weirdly enough, that was so much fun... I wanna take more photos..."
    scene iu25-58
    p "{i}The thought of this really excites me, but what if someone walks in...?"
    scene iu25-59
    p "{i}I'll be quick! This is terrifying..."
    scene iu25-60
    pause
    scene iu25-61
    p "{i}Eeeek!"
    scene iu25-62
    p "{i}Hmm..."
    scene iu25-63
    play sound "phonecam.ogg"
    p "{i}CHEEESE!"
    scene iu25-64
    play sound "phonecam.ogg"
    p "{i}I look so prettyyyyyy..."
    scene iu25-67
    pause
    scene iu25-68
    p "{i}Wow!"
    play sound "stepdylan.ogg"
    scene iu25-69
    p "{i}OH SHI-"
    scene iu25-70
    p "{i}I NEED TO HIDE!"
    scene iu25-71
    pause
    scene iu25-72
    play sound "dooropen.ogg"
    pause
    scene iu25-73
    p "{i}Please don't catch me... Oh god! I hope it's not Dad..."
    scene iu25-74
    d "{i}Gotta be some sort of alcohol around here somewhere."
    scene iu25-75
    p "{i}..Shit!"
    scene iu25-76
    p "{i}...Shit!"
    scene iu25-77
    p "{i}Please leaveeeeee!"
    scene iu25-78
    d "{i}That bitch won't be needing this."
    scene iu25-79
    pause
    scene iu25-80
    p "{i}Dylan..."
    scene iu25-81
    p "..."
    scene iu25-82
    p "{i}THAT'S MY WINE!"
    scene iu25-83
    p "{i}THAT LITTLE PRICK!"
    p "Tomorrow, I'm talkin' to Tenika, and we are going to get him back..."
    p "...for EVERYTHING!"
    scene iu25-84
    p "{i}That was close...! Kind of exciting though, to be honest..."
    scene iu25-85
    p "{i}Oh! I've still got my little toy in, I didn't even realise... It actually feels really nice..."
    scene iu25-92
    p "{i}This is so risky, and I shouldn't be doing this, but..."
    scene iu25-87
    p "{i}Mmmm..."
    scene iu25-88
    p "{i}I'm shaking..."
    $ renpy.movie_cutscene("iu25-002ani.webm", loops=-1)
    scene iu25-90
    p "{i}This feels sooo... good..."
    p "{i}Imagine if someone walks in right now and I'm pleasuring myself...? "

    p "{i}Mmmm..."
    p "{i}I need more..."
    $ renpy.movie_cutscene("iu25-001ani.webm", loops=-1)
    scene iu25-91
    p "{i}I'm so close...."
    scene iu25-93
    $ renpy.movie_cutscene("iu25-001ani.webm", loops=-1)
    p "{i}Mmmmmmm..."
    scene iu25-94
    p "{i}Oh..."
    scene iu25-95a
    p "FU-hhCKKK!"
    scene iu25-96
    p "{i}Oh my god!"
    p "{i}I can't believe it... I think I just squirted..."
    scene iu25-97a
    p "{i}I've never done that before...!"
    play sound "stepryan.ogg"
    scene iu25-98a
    pause
    scene iu25-99
    p "{i}OH NO!"
    scene iu25-100
    stop sound
    r "ARGH!"
    scene iu25-101
    r "[p]...?"
    scene iu25-102
    pause
    scene iu25-103
    p "DAD, IT'S MEEEEE!"
    scene iu25-104
    r "What on Earth are you doing, I heard yelling?"
    scene iu25-105
    p "I was uh..."
    scene iu25-106
    p "... stretching."
    scene iu25-107
    r "You were... stretching...?"
    scene iu25-108
    r "In lingerie... at this hour...?"
    scene iu25-109
    p "Yeah I couldn't sleep, see, ee, oo!"
    scene iu25-110
    p "Ah!!!"
    scene iu25-111
    p "And I felt like looking pretty."
    scene iu25-112
    r "Mmhmm..."
    scene iu25-113
    p "Goodnight, Dad."
    scene iu25-114
    play sound "kiss.ogg"
    pause
    scene iu25-115
    p "{i}Oh my god..."
    scene iu25-116
    pause
    scene iu25-117
    r "{i}Bloody teenagers..."
    scene iu25-140
    p "{i}I don't want to talk about it."
    scene iu25-141
    p "{i}Bed is definitely... needed."
    scene iu25-142
    pause
    scene iu25-143
    pause
    scene iu25-144
    p "{i} Goodnight."
    scene iu25-145
    pause
    scene iu25-145a
    pause
    scene iu25-145b
    pause
    scene iu25-145c
    pause
    play sound "alarmsound.ogg"
    scene iu25-145c
    pause
    scene iu25-146a
    pause
    scene iu25-146b
    pause
    scene iu25-146
    pause
    scene iu25-147
    stop sound
    je "Morning, sleepyhead!"
    scene iu25-148
    p "You've been staring at me while I sleep, haven't you?"
    scene iu25-149
    je "Not for long, just like the past two hours or so..."
    scene iu25-150
    je "Haha! I'm joking, move ya butt, it's beach time baby!"
    scene iu25-151
    je "I'll meet you at the south section!"
    scene iu25-152
    je "It's pretty early, we should have it all to ourselves, c'mon!"
    scene iu25-153
    p "Hehe, okay. Just let me get changed and I'll meet you there."
    scene iu25-154
    p "See you in a minute."
    scene iu25-155
    je "I'll be waiting..."
    scene iu25-156
    p "Hehe."
    scene iu25-157
    pause
    p "{i}Oh my god! My buttplug... I slept with it in!"
    scene iu25-158
    p "{i}I didn't even realise..."
    scene iu25-159
    pause
    scene iu25-160
    p "Eeee."
    scene iu25-161
    p "Oooo."
    scene iu25-162
    p "Ah..."
    scene iu25-163
    p "{i}That actually felt good. Maybe I should've just left it in..."
    scene iu25-164
    p "{i}Hello, friend."
    p "{i}I better put you somewhere safe."
    scene iu25-165
    pause
    scene iu25-166
    pause
    scene iu25-167
    p "Ready, what do ya think!?"
    menu:
        "You look pretty":
            jump pretty
        "You look like dogshit":
            jump dogshit
label dogshit:
    scene iu25-169
    p "I WILL bite you."
    scene iu25-170
    p "{i}Let's go find Jen, I'm going to ask her about the gifts!"
    jump beachtime
label pretty:
    scene iu25-168
    p "Aww... Thanks!"
    scene iu25-170
    p "Let's go find Jen, I'm going to ask her about the gifts!"
    jump beachtime
label beachtime:
    scene iu25-171
    p "{i}I've never been to this part of the beach before, it looks quite secluded."
    scene iu25-172
    p "Jen!"
    scene iu25-173
    je "..."
    scene iu25-174
    je "Hey, you..."
    scene iu25-175
    p "Heya!"
    scene iu25-176
    p "Okay... so... the gifts?"
    scene iu25-177
    je "The gifts?"
    scene iu25-178
    je "I have no idea what you're talking about..."
    scene iu25-179
    p "Oh c'mon! You know exactly what I'm talking about!"
    scene iu25-180
    je "Nope, I really have no idea what you're talking about."
    scene iu25-181
    je "Come, lie down and tell me more, I'm rather intrigued..."
    scene iu25-182
    p "Oh my gosh!"
    scene iu25-183
    p "You're such a fibber."
    scene iu25-184
    p "{i}What if she really doesn't know..."
    scene iu25-185
    je "Suns out guns out, get yo little butt over here!"
    scene iu25-186
    p "Yes m'am!"
    scene iu25-187
    pause
    scene iu25-188
    pause
    scene iu25-189
    je "So, tell us about these mysterious {i}gifts...{/i}"
    scene iu25-190
    p "Right... the gifts..."
    scene iu25-191
    p "Well, I've received two of them..."
    scene iu25-192
    p "One of the gifts, was an amazing set of uh..."
    scene iu25-193
    p "...lingerie."
    scene iu25-194
    p "And the other gift was a... uh..."
    scene iu25-195
    p "... a uh... buttplug!"
    scene iu25-196
    je "A buttplug and lingerie huh... how perculiar..."
    scene iu25-197
    je "Someone must really like you..."
    scene iu25-198
    p "{i}I feel like she's being sarcastic."
    p "It's so strange, like."
    scene iu25-199
    p "I've been trying to think about who it could be for a while now."
    scene iu25-200
    p "And I honestly thought it was y-"
    scene iu25-201
    p "Wait! What are you doing?"
    scene iu25-205
    je "What?"
    scene iu25-206
    je "You didn't realise this is the nudie section of the beach?"
    scene iu25-207
    p "Uh, no I didn't, actually..."
    scene iu25-208
    je "Well, we're both females here and no one is around, just you and me... so..."
    scene iu25-209
    je "You can't leave me hangin'."
    scene iu25-210
    p "Haha, I guess not..."
    scene iu25-211
    p "But no staring!"
    scene iu25-212
    je "Me? I'd never do such a thing."
    scene iu25-213
    p "There..."
    scene iu25-214
    je "See..."
    scene iu25-215
    je "How hard was that?"
    scene iu25-216
    p "Shutup, I've never been here before okay, I didn't know."
    scene iu25-217
    pause
    scene iu25-218
    pause
    je "So..."
    scene iu25-219
    je "I've gotta talk to you about something..."
    scene iu25-220
    je "You know how me and your dad are dating, yeah?"
    scene iu25-222
    p "Duh, of course I do."
    scene iu25-223
    je "To be honest, there's a little bit more to it than that..."
    scene iu25-221
    p "What do you mean, like what?"
    scene iu25-223
    je "Your Dad and I are in an open relationship."
    scene iu25-224
    je "Due to everything that's happened to him in his past, we thought it was best... But you'll need to talk to him more about that."
    scene iu25-225
    je "That doesn't mean I'm going to hurt or cheat on him, but it does mean I'm open to expressing my feelings to... certain people..."
    scene iu25-226
    je "And I've never been happier."
    scene iu25-227
    p "I..."
    scene iu25-228
    p "I... think I understand, but don't you get jealous if he does the same?"
    scene iu25-229
    je "As long as your Dad comes back to me at the end of the day, there's no issue. We have a mutual agreement..."
    scene iu25-230
    p "That's really cool! I've never thought about it like that before, and honestly, I would never have thought Dad would be the type..."
    scene iu25-231
    je "There's definately more to Ryan than you realise, sweety."
    scene iu25-232
    pause
    scene iu25-233
    pause
    scene iu25-234
    p "{i}Mmm..."
    scene iu25-236
    je "Are you okay with this?"
    menu:
        "Yes...":
            jump yesjen01
        "Better talk to Dad first...":
            jump talkdad01
label talkdad01:
    scene iu25-235
    p "I'd better talk to Dad first, if that's okay, Jen...?"
    scene iu25-240
    je "Hmm..."
    scene iu25-251
    je "Of course that's okay."
    play sound "jenphone.ogg"
    scene iu25-251
    pause
    scene iu25-245
    je "God damnit!"
    scene iu25-276
    p "Huh?"
    scene iu25-277
    je "I'm sorry [p] I have to go, I need to pick up Tenika for her appointment. I promised Ryan I would... But, we can continue this conversation later...maybe?"
    scene iu25-282
    p "Okay... sure. Say hi to Nika for me and we can catch up another time!"
    scene iu25-288
    p "{i}Damn I wish I'd gotten to spend more time with Jen. I still reckon it's her sending me gifts..."
    p "{i}But, if it's not her, then who else could it be...?"
    scene iu25-289
    p "{i}I need to get going to see Amy anyway..."
    jump afterbeach01
label yesjen01:
    scene iu25-235
    p "Yeah, it's okay..."
    scene iu25-237
    pause
    scene iu25-238
    pause
    scene iu25-239
    p "{i}Is this really happening...?"
    p "{i}I'm letting Jen touch me... Her fingers feel so soft on my skin..."
    scene iu25-240
    je "Hmm... you like that?"
    p "Mmmm... yeah..."
    scene iu25-241
    pause
    p "Jen... Um... I think there's someone watching us."
    scene iu25-242
    pause
    scene iu25-243
    w "{i}Wow! This isn't something an old guy like me see's everday..."
    scene iu25-244
    menu:
        "Tell him off":
            jump tellhimoff01
        "Let him watch":
            jump lethimwatch01
label tellhimoff01:
    scene iu25-245
    je "Grr..."
    scene iu25-246
    je "Get lost, old man!"
    scene iu25-247
    w "Oh."
    scene iu25-248
    w "I'm sorry ladies..."
    scene iu25-249
    pause
    scene iu25-250
    pause
    scene iu25-251
    je "Problem solved!"
    scene iu25-257
    p "Are you sure he's gone?"
    scene iu25-256
    je "Trust me, yeah?"
    scene iu25-258
    je "I trust you..."
    scene iu25-254
    pause
    scene iu25-255
    pause
    scene iu25-255
    p "{i}I feel so exposed... and to be completely honest, I just don't care... I'm so comfortable with Jen."
    p "{i}If anything... it's kinda making me even more horny!"
    scene iu25-261
    p "Everything's out and on show, for anyone to see..."
    scene iu25-262
    je "I know... It's so hot... Just relax...!"
    scene iu25-263
    p "Mmmmmm..."
    scene iu25-264
    p "That feels {i}really good..."
    scene iu25-265
    je "Ready?"
    $ renpy.movie_cutscene("iu25-003ani.webm", loops=-1)
    scene iu25-266
    p "Oh my god, Jen..."
    scene iu25-267
    p "{i}I'm so fucking turned on..."
    p "{i}Her soft warm lips are amazing to kiss..."
    scene iu25-270
    p "{i}I can't believe this is happening, Jen's warm fingers are thrusting so deep inside of me..."
    scene iu25-271
    je "{i}Fuck... I hadn't realised how attracted I am to Ryan's daughter..."
    scene iu25-269
    p "Mmmmmm..."
    scene iu25-269
    play sound "jenphone.ogg"
    pause
    scene iu25-245
    je "God damnit!"
    scene iu25-275b
    je "I forgot about Tenika!"
    scene iu25-276
    p "Huh?"
    scene iu25-277
    je "I'm sorry [p], I have to go. I need to pick up Tenika for her appointment, I promised Ryan I would. But... we can continue this later..."
    scene iu25-281
    p "Are you serious?"
    scene iu25-282
    p "{i}I can't believe she left me hanging like this! I'm so horny..."
    scene iu25-283
    p "{i}God damnit..."
    scene iu25-288
    p "{i}On the brightside... she did say continue this later..."
    scene iu25-289
    p "{i}I won't think too far ahead, but I need to get going and see Amy..."
    scene iu25-290
    jump afterbeach02
label lethimwatch01:
    scene iu25-250
    pause
    scene iu25-251
    je "He's harmless... just focus on me..."
    scene iu25-257
    p "Are you sure?"
    scene iu25-256
    je "Trust me, yeah?"
    scene iu25-258
    je "I trust you..."
    scene iu25-254
    pause
    scene iu25-255
    pause
    scene iu25-255
    p "{i}That old man can see everything. But somehow, being with Jen makes me so excited that I don't even care...!"
    scene iu25-259
    je "You good?"
    scene iu25-261
    p "He can see everything..."
    scene iu25-262
    je "I know... It's so hot! Just relax..."
    scene iu25-263
    p "Mmmmmm..."
    scene iu25-264
    p "That feels {i}really good..."
    scene iu25-265
    je "Ready?"
    $ renpy.movie_cutscene("iu25-003ani.webm", loops=-1)
    scene iu25-266
    p "Oh my god, Jen..."
    scene iu25-267
    p "{i}I'm so fucking turned on..."
    p "{i}Her soft warm lips are amazing to kiss..."
    scene iu25-268
    pause
    scene iu25-272
    w "{i}This is so great..."
    w "{i}I never imagined that I'd ever see two hot chicks going at it like this! Glad I decided to come to the beach this morning, ey?"
    scene iu25-270
    p "{i}I can't believe this is happening! I'm fully exposed to a stranger with Jen's warm fingers so deep inside me..."
    scene iu25-271
    je "{i}Fuck... I hadn't realised how attracted I am to Ryan's daughter..."
    scene iu25-272
    w "{i}Bloody hell! Keep on going girls..."
    scene iu25-273
    p "Mmmmmm..."
    play sound "jenphone.ogg"
    scene iu25-274
    je "Oh shit!!!"
    scene iu25-275
    je "I forgot about Tenika!"
    scene iu25-276
    p "Huh?"
    scene iu25-277
    je "I'm sorry [p], I have to go. I need to pick up Tenika for her appointment, I promised Ryan I would. But... we can continue this later..."
    scene iu25-278
    pause
    scene iu25-279
    je "Bye, old man."
    scene iu25-280
    w "Bye..."
    scene iu25-281
    p "Are you serious?"
    scene iu25-282
    p "{i}I can't beleive she left me hanging like this! I'm so horny..."
    scene iu25-283
    p "..."
    scene iu25-284
    p "What are YOU lookin' at?"
    scene iu25-285
    w "Oh uh..."
    scene iu25-286
    w "Sorry luv, I'd best be on my way..."
    scene iu25-287
    pause
    w "FUCK, what a show! It gave me a right stiffy!"
    w "Been years since that's happened..!"
    scene iu25-288
    p "{i}Did that really just happen?"
    scene iu25-289
    p "{i}That really did just happen, didn't it...?"
    p "{i}I need to get going..."
    scene iu25-290
    jump afterbeach02
label afterbeach01:
    scene iu25-290
    p "{i}It's such a lovely day out today..."
    scene iu25-290a
    p "{i}I love getting out as much as I can, it's really good for the mind, body and soul."
    scene iu25-291
    p "{i}Although, I will admit, I have been quite slack lately. But, I'm planning to work out in Dad's gym more often."
    scene iu25-292
    p "{i}Here's Amy's clothes store."
    jump amy01
label afterbeach02:
    scene iu25-290
    p "{i}I can barely focus after what happened at the beach..."
    scene iu25-290a
    p "{i}... and I'm feeling quite tingly down there... I guess it was from all the excitement."
    scene iu25-291
    p "{i}Either way, I need to focus. Hopefully, Amy has an awesome costume for me."
    p "{i}I can go to my shoot, then go home and have some alone time."
    scene iu25-292
    p "{i}Here's Amy's clothes store."
    jump amy01
label amy01:
    scene iu25-293
    p "Hey, Amy!"
    scene iu25-294
    pause
    scene iu25-295
    a "[p]! It's so good to see youuuu."
    scene iu25-296
    a "How's your day been? It's looking so hot out at the moment."
    scene iu25-297
    p "Yeah... Warm to say the least! I was just at the beach with Jen, it was lovely."
    scene iu25-298
    p "How about you, how's work?"
    scene iu25-299
    a "It's been pretty good, actually. I've got some awesome costumes lined up for you, but I also wanted to talk to you about something important."
    scene iu25-300
    p "That you're dating my sister and I've never seen her look happier?"
    scene iu25-301
    a "Haha! Aww you know? That's sweet that she told you."
    a "We aren't actually dating yet, but I do really like her though."
    scene iu25-302
    p "She tells me everything! You should definitely ask her... when you're ready of course."
    scene iu25-303
    a "You know, maybe I will!"
    scene iu25-304
    a "And I really appreciate you accepting me and Nika. I don't get that very often."
    scene iu25-305
    p "I've always had good feelings about you, Amy. Don't worry, I trust you."
    scene iu25-306
    a "That's absolutely splendid! Now, let's get you something gorgeous to wear for the party!"
    p "Go check the changing room, I have some surprises for you!"
    scene iu25-307
    p "Oooh! How exciting! Thanks, Amy."
    scene iu25-308
    p "..."
    scene iu25-309
    p "..."
    scene iu25-310
    p "{i}This one's cool!"
    scene iu25-312
    p "Amy!?"
    scene iu25-320
    a "Yeah!"
    scene iu25-312
    pause
    scene iu25-313
    pause
    scene iu25-314
    p "What do ya think?"
    scene iu25-315
    p "I'm not too sure..."
    scene iu25-321
    a "Reow, I actually like it!"
    scene iu25-322
    a "Try the next one!"
    scene iu25-316
    pause
    scene iu25-312
    pause
    scene iu25-317
    p "What about this?"
    scene iu25-318
    p "I think it might be a little {i}too{/i} short..."
    scene iu25-319
    p "What do ya think?"
    scene iu25-323
    a "Ah..."
    scene iu25-324
    a "Yeah, you could say that. Hehe..."
    scene iu25-312
    p "I'll try the next one."
    scene iu25-325
    p "{i}Hey, I like this!"
    scene iu25-312
    p "..."
    scene iu25-326
    p "Uhh..."
    scene iu25-329
    a "Everything okay, [p]?"
    scene iu25-326
    p "Umm..."
    scene iu25-327
    p "{i}Shit, this is embarassing."
    scene iu25-328
    p "Amy? Could you come in here, please..."
    scene iu25-330
    p "..."
    scene iu25-330
    p "{i}I hate my genetics sometimes...{i}"
    scene iu25-330
    a "Can I come in?"
    scene iu25-331
    p "Uh-huh!"
    scene iu25-332
    p "Yeah..."
    scene iu25-333
    a "Oh deary me, it does looks like we are having a bit of a trouble here, doesn't it?"
    scene iu25-334
    p "Yeah, you could say that..."
    scene iu25-335
    a "Here, let me fix you up. Turn around, please."
    scene iu25-336
    a "..."
    scene iu25-337
    a "Arms up, cowgirl"
    scene iu25-338
    a "I need to tighten the front for you."
    scene iu25-339
    pause
    scene iu25-340
    p "Oh..."
    scene iu25-341
    pause
    scene iu25-342
    a "All good?"
    scene iu25-343
    p "Yes, fix me up!"
    scene iu25-344
    p "..."
    scene iu25-345
    p "{i} Her hands are so gentle...{i}"
    scene iu25-346
    a "I've just gotta go under your top a bit, is that okay?"
    scene iu25-347
    p "Yes, go for it."
    scene iu25-348
    p "..."
    scene iu25-349
    p "{i}This is starting to feel nice...{i}"
    menu:
        "Let your imagination drift":
            jump imagination
        "Don't, stay focused":
            jump alldone
label imagination:
    scene iu25-350
    p "... Mmmm..."
    scene iu25-351
    pause
    scene iu25-353
    a "Would you like me to touch you like... this?"
    scene iu25-354
    a "And, what if I slid my hands down your pants...?"
    scene iu25-356
    a "..."
    scene iu25-357
    a "..."
    scene iu25-355
    a "And if I kissed you on your neck while my fingers are pleasuring you... [p]?"
    scene iu25-358
    p "Mmm..."
    scene iu25-359
    a "[p]!?"
    scene iu25-360
    p "Mmm..."
    scene iu25-361
    p "Hmm?"
label alldone:
    scene iu25-362
    a "All done!"
    scene iu25-363
    p "Oh..."
    scene iu25-364
    p "Great job, haha!"
    scene iu25-365
    a "Anytime, hehe."
    scene iu25-366
    p "I think we've found the costume for the party."
    scene iu25-370
    p "Thanks, Amy."
    scene iu25-371
    a "Anytime, [p]! I'll see you in a second. Call me if you need any more help with your outfits, haha..."
    scene iu25-367
    a "Also, feel free to try out that outfit on the floor. It's too big for me."
    scene iu25-368
    p "{i}Another one?"
    scene iu25-369
    p "{i}Oh my god, this one looks so cool! Amy's spoiling me!"
    scene iu25-312
    p "Hey, Amy?"
    scene iu25-374
    a "Yeah!?"
    scene iu25-375
    a "Holy moly!"
    scene iu25-373
    p "..."
    scene iu25-372
    p "It's a little bit different I know. Do you like it?"
    scene iu25-376
    a "Yes! You look so nice with your hair down."
    scene iu25-377
    p "I never wear my hair like this. I felt like a change, I guess."
    scene iu25-378
    a "It's definitely a nice change, that's for sure."
    scene iu25-379
    p "It might take me a while to get used to, I think..."
    p "Are you excited for the party tonight?"
    scene iu25-380
    a "Yes. It's going to be so much fun, I cant wait to hang out with you and Nika."
    scene iu25-381
    p "Nika is super lucky to have someone like you. I can't imagine what you two are going to get up to, we may need a leash."
    scene iu25-382
    a "Oh noooo! Don't tie us up, I promise we'll be good!"
    scene iu25-384
    p "You'd better watch yourselves, haha."
    scene iu25-383
    a "We'll be watching you too, hehe."
    scene iu25-385
    a "Anyway I'd better let you go!"
    scene iu25-387
    p "Yeah I've got a lot do, I'm already late for my meeting."
    scene iu25-388
    p "It was so good seeing you, and thank you again."
    scene iu25-389
    a "You to, [p]."
    scene iu25-390
    play sound "kiss.ogg"
    p "..."
    scene iu25-391
    p "uh..."
    scene iu25-392
    p "{i}Wait! What am I doing...{i}"
    scene iu25-393
    a "Hehe, Bye bye, [p]."
    scene iu25-394
    a "I'll see you and Nika at the party tonight!"
    scene iu25-395
    p "Bye..."
    scene iu25-396
    p "{i}Oh no, what did I just do...?"
    scene iu25-397
    p "{i}Shit... I didn't mean to do that! It's just all this built up tension and strange thoughts...{i}"
    scene iu25-398
    p "{i}Why did Amy initiate the kiss? Still, it's no excuse, but I'll have to think about that later...{i}"
    scene iu25-399
    p "{i}I'm going to have to talk to Nika, I feel really awful."
    scene iu25-400
    p "{i}I'd better head to my photoshoot, I'm already late..."
    scene iu25-401
    p "{i}This place is interesting."
    scene iu25-402
    p "{i}I've never been to this side of town before."
    scene iu25-403
    p "{i}Well, here's the address."
    scene iu25-404
    p "{i}I'd better hurry up."
    scene iu25-405
    p "..."
    scene iu25-406
    p "Wow, compared to the outside, I didn't think it'd be so exquisite."
    scene iu25-407
    pause
    scene iu25-408
    l "{i}Young, blonde, fit, blue eyes, athletic...{i}"
    scene iu25-409
    l "Oh!"
    scene iu25-410
    l "Hello beautiful. You must be [p], we've been waiting for you."
    scene iu25-411
    p "Yes that's me, sorry I'm late. I assume that means I'm at the right place?"
    scene iu25-412
    p "I'm here to see uhh, Marty."
    scene iu25-413
    l "Yes yes, we've been expecting you! I'm Lorenzo, it's a pleasure."
    scene iu25-414
    l "Hmm..."
    scene iu25-415
    l "Alright, let's see here..."
    scene iu25-416
    l "Room 101, The Gentlemen's lounge."
    scene iu25-417
    p "The Gentlemen's lounge?"
    scene iu25-418
    l "Yes, one of the finest rooms of the house, follow me please!"
    scene iu25-419
    pause
    scene iu25-420
    l "I've been working here for almost 10 years now and I haven't seen a young girl like you in quite some time."
    scene iu25-421
    p "10 years? That's a long time... You're saying that like it's a bad thing?"
    scene iu25-422
    l "No, not all maddam."
    scene iu25-423
    l "It's kind of relieving actually, I can sense you have a great aura about you."
    scene iu25-424
    l "And to be fair I'm sick of seeing some of the, {i}more unusual{/i}, individuals that come through, but don't let the boss know that, haha."
    scene iu25-425
    p "{i} I wonder what he means by that...?"
    scene iu25-426
    p "{i}I guess there must be a lot of people who try-out for these modelling gigs."
    scene iu25-427
    l "Room 101! Here we are maddam."
    scene iu25-428
    l "Marty will be waiting for you inside."
    scene iu25-429
    pause
    scene iu25-430
    pause
    scene iu25-431
    "..."
    scene iu25-432
    p "..."
    scene iu25-433
    l "Everything alright, dear?"
    scene iu25-434
    p "{i}I know him from somewhere...{i}"
    scene iu25-435
    p "Oh nothing, haha."
    scene iu25-436
    l "Have fun."
    scene iu25-439
    pause
    scene iu25-438
    p "Hey, Marty."
    scene iu25-437
    ma "[p], you're late..."
    scene iu25-440
    p "I know, I'm sorry I was caught up... and a bit lost."
    scene iu25-442
    ma "It doesn't look very good for a first audition, does it?"
    scene iu25-441
    p "It won't happen again, promise."
    scene iu25-443
    ma "Great, take a seat."
    scene iu25-444
    p "Sure."
    scene iu25-445
    pause
    scene iu25-446
    p "I have to thank you again for this amazing opportunity, Marty."
    scene iu25-447
    p "It's not everyday a girl like me gets so fortunate."
    scene iu25-448
    p "{i} I just hope I don't let anyone down.{i}"
    scene iu25-450
    ma "That's okay. The first day I saw you, I knew you there were great things in store for you."
    scene iu25-451
    ma "And the boss loved your pictures... but is also not so happy..."
    scene iu25-449
    p "{i}Haha! I bet they loved Marcus' cheeks..."
    p "I'm sorry, it was just a joke, but I'm glad he liked the photos."
    scene iu25-452
    ma "Yeah well, sometimes jokes aren't as funny as you think! Either way, we have given you the benefit of the doubt."
    scene iu25-453
    ma "The boss needs to see how you can perform under a bit of pressure... He would love to see a video of you."
    scene iu25-454
    p "Uh-huh. Im listening..."
    scene iu25-455
    ma "It'll be very similar to our shoot before, but we'll be recording it, instead."
    scene iu25-457
    p "{i}Thinking about being on video makes me quite anxious, but I have to act confident..."
    scene iu25-456
    p "Great, sounds fun!"
    scene iu25-458
    ma "{i}This is going to be good...{i}"
    scene iu25-459
    ma "{i}She has no idea what I've got planned for her...{i}"
    scene iu25-460
    ma "Camera's rolling, ready when you are!"
    scene iu25-461
    p "Sorry to ask, but what is it you want me to do?"
    scene iu25-462
    ma "Stand in the centre of the room, please."
    scene iu25-463
    p "..."
    scene iu25-464
    p "Like, here?"
    scene iu25-465
    p "Look, I've never been on video before, I'm a bit lost."
    scene iu25-466
    ma "Don't worry, you're doing fine... I want you to dance for me!"
    scene iu25-467
    p "Dance? Umm... I can try, I guess..."
    scene iu25-468
    p "{i}I feel so awkward."
    scene iu25-469
    p "..."
    scene iu25-470
    p "{i}What the heck am I doing...?"
    scene iu25-471
    p "..."
    scene iu25-472
    p "{i}I can only dance when I'm drunk..."
    scene iu25-473
    p "..."
    scene iu25-474
    ma "..."
    ma "What an ass...!"
    scene iu25-475
    ma "{i}So developed for a teenager...{i}"
    scene iu25-476
    ma "Perfect, [p]. Now take your pants off and continue to dance. Or... I'll send all of your photos to your family... including Dylan and Tenika."
    scene iu25-477
    pause
    scene iu25-478
    p "..."
    scene iu25-479
    p "{i}What the f...?"
    scene iu25-480
    p "WHO THE HELL DO YOU THINK YOU ARE!?"
    scene iu25-481
    ma "Oh trust me, I know a lot more than you think."
    scene iu25-482
    ma "So, be a good girl, obey my requests, and we won't have to esculate things any further."
    scene iu25-483
    p "You're a filthy pig, how dare you blackmail me and bring my family into this!"
    scene iu25-484
    ma "Sometimes life isn't fair, is it?"
    scene iu25-485
    ma "Now, be a good girl and remove those pants."
    scene iu25-486
    p "You know you won't get away with this..."
    scene iu25-487
    ma "Ooh I'm so scared! It'll all be over soon, as long as you do as you're told."
    scene iu25-488
    p "{i}I need to think of something... but I better do what he says, for now...{i}"
    scene iu25-489
    p "Grr."
    scene iu25-490
    pause
    scene iu25-491
    ma "{i}Wow! That firm ass... her panties are barely covering it."
    ma "{i}And those long, sexy legs... What I wouldn't do to have them wrapped around me..."
    scene iu25-492
    p "{i}This is so embarassing.{i}"
    scene iu25-494
    p "{i}I'm going to make sure he regrets this!"
    scene iu25-495
    p "There you happy!?"
    scene iu25-496
    ma "Very happy, now pose for me."
    scene iu25-497
    p "{i}Grrr... I have to play along."
    scene iu25-498
    p "Okay, what do you need me to do?"
    scene iu25-499
    ma "Put your hand on your hip and flex your petite body for me..."
    scene iu25-500
    p "{i}Absolute asshole!"
    scene iu25-501
    p "Like, there...?"
    ma "So cute. Now, turn and show me your backside."
    scene iu25-519
    p "{i}He won't get away with this..."
    ma "Sexy. Now, look over your shoulder, back at me."
    scene iu25-502
    pause
    ma "Wow..."
    scene iu25-503
    ma "{i}Mmmm... her teenage ass is to die for"
    scene iu25-504
    ma "{i}I need to see it closer."
    scene iu25-505
    ma "Hey, [p]?"
    scene iu25-506
    ma "Come stand in front of me will you?"
    scene iu25-507
    p "{i}Just you wait... you freak!"
    scene iu25-508
    p "Sure."
    scene iu25-509
    pause
    scene iu25-510
    pause
    scene iu25-511
    ma "{i}Oh yeah..."
    scene iu25-512
    pause
    scene iu25-513
    ma "{i}Her little panties are barely holding anything in..."
    scene iu25-514
    p "{i}This is so messed up, but I have to think of my family."
    scene iu25-515
    p "{i}But... what on earth can I do...?"
    scene iu25-517
    ma "Hey [p], put one hand on your bum, and give it a little squeeze for me."
    scene iu25-518
    p "{i}GRRRRRRRR! I'M GOING TO KILL HIM!!"
    scene iu25-520
    p "Okay."
    scene iu25-521
    pause
    scene iu25-522
    pause
    scene iu25-523
    pause
    scene iu25-524
    ma "{i}Oh yeah, look at that cute little ass..."
    scene iu25-525
    p "{i}I hate him."
    scene iu25-526
    p "{i}What do I do now?"
    menu:
        "Teach him a lesson":
            jump teachlesson01
        "Endure it":
            jump endure01
label teachlesson01:
    scene iu25-527
    p "Hey, Marty?"
    scene iu25-528
    ma "Yeah!?"
    scene iu25-529
    pause
    scene iu25-530
    play sound "kick01.ogg"
    p "HIYA!"
    scene iu25-531
    ma "ARGH!"
    scene iu25-563
    ma "OH MY GOD. YOU FUCKING BITCH!"
    jump ilaugh01
label endure01:
    scene iu25-528
    ma "I want to see that sweet ass. Bend over and show it to me... hands on the table, NOW!"
    scene iu25-532
    p "{i}I need to endure it..."
    scene iu25-533
    pause
    scene iu25-534
    pause
    scene iu25-535
    p "{i}This is so fucking demoralizing..."
    scene iu25-536
    ma "Oh yeah..."
    scene iu25-537
    ma "That cute little ass..."
    scene iu25-538
    ma "{i}I can just see both her holes, she looks like a virgin... but what's with that gaping ass...!?"
    scene iu25-539
    p "{i}What do I do now... he's so close and staring at me...?"
    p "{i} This sick bastard is able to see my most private parts..."
    scene iu25-540
    p "{i}I can feel my butt is still loose from the toy... please let this end."
    scene iu25-541
    ma "Oh yeah! You've got such an amazing ass, [p]."
    ma "{i}I bet she's a little anal whore..."
    scene iu25-542
    ma "{i}I can't contain myself..."
    scene iu25-543
    pause
    scene iu25-544
    pause
    scene iu25-543
    pause
    scene iu25-544
    pause
    scene iu25-543
    ma "{i}I want to fill both of these little holes till they are overflowing with my cum..."
    ma "{i}She'll be begging for me to give her more, by the time I'm done with her..."
    scene iu25-544
    pause
    scene iu25-543
    pause
    scene iu25-544
    pause
    scene iu25-543
    pause
    scene iu25-545
    ma "Your ass is to die for, [p]. Keep looking forward..."
    scene iu25-546
    p "I am!!!"
    p "{i}Asshole!"
    scene iu25-547
    ma "{i}I need to touch it."
    scene iu25-548
    pause
    scene iu25-549
    pause
    scene iu25-550
    p "HEY!"
    scene iu25-551
    ma "Do as your told and keep looking forward, or I'll send your photos to everyone!"
    scene iu25-552
    p "Argh!"
    scene iu25-553
    ma "Good girl."
    scene iu25-554
    ma "{i}I need a better look at these holes..."
    scene iu25-555
    pause
    scene iu25-550
    p "WHAT THE...!"
    scene iu25-556
    ma "Be quiet!"
    ma "{i}Holy shit..."
    scene iu25-557
    ma "If I'm not mistaken, it looks like you enjoy it in the ass, [p]...?"
    scene iu25-558
    p "Stop... please!"
    scene iu25-559
    ma "I bet your little sister, Tenika, has a tight pussy and gaping ass, just like you, eh?"
    scene iu25-560
    p "YOU MOTHER FU-"
    scene iu25-561
    play sound "kick01.ogg"
    p "YARGH!"
    scene iu25-562
    p "YOU FUCKING SICK FREAK!"
    scene iu25-563
    ma "MY JAW! YOU DAMN BITCH!"
label ilaugh01:
    scene iu25-564
    p "Muhaha!"
    scene iu25-565
    p "How does my heel taste, pervert!"
    scene iu25-566
    play sound "revolver.ogg"
    pause
    scene iu25-567
    p "Shit...!"
    play sound "doorslam.ogg"
    scene iu25-567
    pause
    scene iu25-568
    mav "Is there a problem here?"
    scene iu25-569
    ma "This goddamn bitch is disobeying orders, and she abused me!"
    scene iu25-570
    mav "Disobeying orders? Now, now, we can't have that, can we?"
    scene iu25-571
    ma "No boss, we definitely can't."
    scene iu25-575
    p "{i}HE{/i} FUCKING ABUSED {i}ME!{/i} CHECK THE CAMERA!"
    scene iu25-573
    mav "{i}He{/i} abused {i}you?{/i}"
    scene iu25-574
    mav "A trusted employee and friend, who has been working with me for years?"
    scene iu25-575
    p "I'M TELLING THE TRUTH!"
    scene iu25-577
    mav "You really think I'd beleive you, over a hard working individual like Marty?"
    scene iu25-578
    mav "Pass me the gun, please."
    scene iu25-579
    ma "Yes sir, my apologies."
    scene iu25-580
    mav "Thank you."
    scene iu25-581
    mav "Now, what are we going to do with you...?"
    scene iu25-582
    mav "What do you think Marty? I know you don't like liars."
    scene iu25-583
    ma "You know me boss, I think we should teach this bitch a lesson."
    scene iu25-584
    mav "Teach the bitch a lesson, huh?"
    scene iu25-585
    ma "Yeah yeah, let's fuc-"
    scene iu25-586
    ma "EEEGH!"
    scene iu25-587
    pause
    scene iu25-588
    pause
    play sound "punch01.ogg"
    scene iu25-591
    pause
    scene iu25-592
    pause
    scene iu25-589
    p "Oh... SHIT!"
    scene iu25-593
    ma "What the fuck, boss!?"
    scene iu25-594
    mav "I heard everything from outside Marty, you're an absolute scumbag! And, you did also say 'teach the BITCH a lesson.'"
    scene iu25-595
    p "Haha, you really did."
    scene iu25-596
    ma "I'll remember this, this isn't over...!"
    scene iu25-597
    mav "Your fired, Marty, don't return here ever again!"
    scene iu25-598
    mav "{i}Idiot...! He's going to ruin everything... this is a serious business. Now I have to fix this!"
    scene iu25-599
    p "Uh... I'm gonna go..."
    scene iu25-600
    mav "Look, I'm so sorry, [p]. I knew you were coming, but I didn't expect anything like that!"
    scene iu25-601
    mav "I did hear rumours about Marty, but I really didn't believe they were true..."
    scene iu25-602
    mav "I've organised the bouncers to take care of him on the way out, so you don't have to worry about him ever again."
    scene iu25-603
    p "This is absolutely messed up! I came here to shoot, was harassed and all of this bullshit happened, instead."
    scene iu25-604
    p "You're lucky I don't tell the police about this although, I'm still kinda questioning if I should, or not..."
    scene iu25-605
    mav "Please don't, [p]. Here take this, it's compensation for what you went through."
    scene iu25-606
    p "{i}Holy moly! I've never seen so much money before...!"
    scene iu25-607
    p "This is a lot! Are you sure?"
    scene iu25-608
    mav "Yes I'm sure! It was horrible what happened, and I feel really guilty about it..."
    scene iu25-609
    mav "Please, feel free to wash up in the bathroom next door while I clean up here."
    mav "Can you come see me in the green room across the hall after you are done, please?"
    scene iu25-610
    p "Sure, I can do that, but any funny business and I'm out!"
    scene iu25-611
    pause
    scene iu25-612
    pause
    scene iu25-613
    mav "[p]..."
    scene iu25-637
    p "Yeah!?"
    scene iu25-614
    mav "Your pants..."
    scene iu25-615
    p "..."
    scene iu25-638
    p "Haha...! Oh, right!"
    scene iu25-616
    p "{i}What the hell was Marty thinking? What an asshole...!"
    scene iu25-617
    p "{i}If that guy hadn't come though...?"
    scene iu25-618
    p "{i}Oh my god! I didn't even ask his name..."
    scene iu25-619
    p "{i}I better go talk to him and make sure he's not like Marty..."
    scene iu25-620
    p "{i}Let me tidy myself up a bit first."
    scene iu25-621
    p "{i}Ready when you are!"
    scene iu25-622
    p "Found ya!"
    scene iu25-623
    mav "I'm happy you found the room, it's a maze in here..."
    scene iu25-624
    mav "Look... I wanted to apologise again about what happened! I feel so horrible."
    scene iu25-625
    p "Oh, umm..."
    scene iu25-626
    p "It's okay, I'm just happy you came when you did."
    scene iu25-627
    mav "So am I... Anyway I'm Maverick, I never introduced myself properly."
    p "{i}That answers that question, then!"
    scene iu25-628
    mav "I manage this place, and for bullshit to happen like that makes me feel..."
    scene iu25-629
    mav "Well... pretty damn annoyed! We don't work that way here."
    scene iu25-630
    p "I understand..."
    scene iu25-631
    p "When you say 'here', what exactly do you mean?"
    scene iu25-632
    mav "{i} As much as I want to tell her the truth, it may scare her away..."
    scene iu25-633
    mav "This is my modelling studio, clients from all across the globe, come here to shoot. There's a range of rooms for different styles of modelling."
    mav "...But I can tell you more about it later."
    scene iu25-634
    p "Hmm it sounds interesting. I'd really love to hear more about it."
    scene iu25-635
    mav "In the meantime I've got a surprise for you. Think of it as another way of me apologizing for what happened here today."
    scene iu25-636
    p "Ooo, I like surprises!"
    scene iu25-639
    p "Is it more money!?"
    scene iu25-640
    mav "Unfortunately not, haha! But you can earn more money, if you like. Do you know Bunny Hurdette lingerie? I've got a set of it behind the curtain for you to try on, if you'd like?"
    scene iu25-641
    p "Oh my god are you serious? YES! "
    scene iu25-642
    mav "Watch your step. Let me know if you like it?"
    scene iu25-643
    mav "{i}Hmm..."
    scene iu25-644
    mav "{i}There's something strange about this girl. She reminds me of my sisters somewhat. But I can't put my finger on what, exactly...?"
    scene iu25-645
    mav "{i}I need to explain to her in more detail about what's going on. But I don't think now's the right time..."
    scene iu25-646
    mav "{i}..."
    scene iu25-647
    mav "Hey, that looks great!"
    scene iu25-648
    p "Do you think so?"
    scene iu25-649
    p "I'm not too sure..."
    scene iu25-650
    mav "Not too sure? Behave! It fits amazingly!"
    scene iu25-651
    mav "My friend, Cherry, owns the Bunny Hurdette in town. I'm sure she'd love to see you wearing her lingerie. Do you want to take a few quick photos for her?"
    scene iu25-652
    p "Oh my god yes!"
    scene iu25-653
    mav "Great! Take a seat and we can begin."
    scene iu25-654
    p "This better be just business, or I'm gone, okay!"
    mav "Of course!"
    scene iu25-655
    pause
    scene iu25-657
    mav "Ready?"
    scene iu25-658
    mav "Smile!"
    scene iu25-656a
    play sound "shutter.ogg"
    pause
    scene iu25-658
    mav "Great job [p], now, lay on your side for me and I'll capture a few different angles."
    scene iu25-659
    play sound "shutter.ogg"
    pause
    scene iu25-660
    play sound "shutter.ogg"
    pause
    scene iu25-661
    play sound "shutter.ogg"
    pause
    p "Hehe."
    scene iu25-662
    mav "Very good! If Cherry loves these, there could be more work for you!"
    mav "{i}Im sure she will, [p] is beautiful, but It's not up to me."
    mav "Now, on your tummy please!"
    scene iu25-663
    p "Ooo, how exciting."
    scene iu25-663
    play sound "shutter.ogg"
    pause
    scene iu25-664
    play sound "shutter.ogg"
    pause
    scene iu25-665
    play sound "shutter.ogg"
    pause
    scene iu25-666
    mav "Rockin it! On your back now and clasp your arms around your legs, please."
    scene iu25-667
    p "Thank you!"
    scene iu25-667
    play sound "shutter.ogg"
    pause
    scene iu25-668
    play sound "shutter.ogg"
    pause
    scene iu25-669
    play sound "shutter.ogg"
    pause
    scene iu25-670
    mav "And we're done. Great work!"
    scene iu25-671
    p "Oh! Wait... that's it?"
    p "{i}I was having so much fun..."
    scene iu25-672
    mav "It sure is. Were you expecting more?"
    scene iu25-673
    p "When I did my first shoot with Marty, it went on for ages..."
    scene iu25-674
    mav "That's because Marty's an ass and wanted to shoot you for his own twisted agenda."
    scene iu25-675
    p "Hmm..."
    scene iu25-676
    p "You're so right, actually."
    scene iu25-677
    p "He was a bit of an ass, wasn't he? Screw that guy!"
    scene iu25-678
    mav "It's embarassing, to say the least. I've been running this place for 5 years and I even let him look after my sisters..."
    scene iu25-680
    mav "I trusted him, and I hope there isn't anything more that I could find out..."
    scene iu25-679
    p "I'm sure it'll be okay Maverick, I have a sister too, so I know what it feels like to be protective."
    scene iu25-681
    p "What about your parents?"
    scene iu25-682
    mav "Uh... my parents passed away 5 years ago and left this place to me, I don't really want to get into it..."
    scene iu25-683
    p "I'm sorry for asking. Believe it or not, I can understand to some extent. Anyway, I'm here for you, if you need to talk..."
    scene iu25-684
    mav "It's fine [p], you didn't know. But, maybe we can talk about it another time, if that's okay?"
    scene iu25-679
    p "Of course it is!"
    scene iu25-689
    mav "Anyway..."
    scene iu25-688a
    mav "These are my sisters."
    scene iu25-698
    mav "Twins..."
    scene iu25-685
    mav "Charly on the left, Chelsea on the right."
    mav "Identical in every way, except their eye colour."
    mav "Although, Chelsea can be a bit of a deviant sometimes..."
    mav "They've had a really difficult upbringing, but I do everything I can to be there for them. I even help them with school... where I can, that is!"
    scene iu25-686
    p "Aww... that must be so difficult."
    scene iu25-687
    p "They're adorable, and so lucky to have you!"
    scene iu25-691
    mav "Thanks! I do what I can to make sure they're safe and secure at all times."
    scene iu25-689
    mav "But yeah..."
    scene iu25-690
    mav "Thank you for being so understanding today. And, you know what...?"
    scene iu25-691
    mav "Keep the lingerie."
    scene iu25-692
    p "You definitely know how to make a girl happy!"
    scene iu25-694
    mav "I try my best... I'd better let you go. I've got loads of things to checkup on!"
    scene iu25-693
    p "Aw okay. Thank you Maverick, this was so much better with you."
    scene iu25-696
    mav "Anytime. I'll message you soon regarding Cherry."
    scene iu25-697
    p "{i}I didn't anticipate Maverick to be so nice... and he literally saved me from that scumbag, Marty."
    scene iu25-699
    p "{i}Maybe I should ask if he wants to hang out? I'd love to get to know him more, even as friends."
    scene iu25-700
    p "Hey, Maverick?"
    scene iu25-701
    mav "Yeah!?"
    scene iu25-702
    p "Just out of curiousity... I know it's a bit random to ask, but..."
    scene iu25-703
    p "My family is throwing a costume party tonight, and I wanted to know if there's any chance you wanted to come around for a bit?"
    scene iu25-704
    mav "It's so kind of you to ask, [p]. Any other day I would jump at the chance... but there's a few things I have to sort out tonight, I'm afraid. But, I'll message you soon, okay?"
    scene iu25-705
    p "Okay, that's totally fine, I'll see ya when i see ya!"
    scene iu25-706
    p "{i}Hehe, that was fun. I better go get changed..."
    scene iu25-708
    pause
    scene iu25-709
    p "{i}I don't usually like to check myself out, but..."
    scene iu25-710
    p "{i}Damn! I look fine..."
    scene iu25-872
    p "{i}Oh...."
    scene iu25-711
    p "{i}Mmm..."
    scene iu25-712
    p "{i}Jesus, not here, [p]..."
    scene iu25-713
    pause
    scene iu25-714
    pause
    scene iu25-715
    pause
    scene iu25-716
    p "Lets' gooooo!"
    scene iu25-717
    p "{i}That was such a fun shoot, apart from the beginning..."
    scene iu25-718
    p "{i}And the fact Maverick treated me so nicely, and could even offer me a deal with Bunny Hurdette, what a dream!"
    scene iu25-719
    p "{i}He made me feel so good about myself... I feel... really good actually."
    scene iu25-720
    p "{i}I don't think I can wait till I get home so I can release these urges..."
    scene iu25-721
    p "{i}The toilets near Jade's cafe are around here, what should I do?"
    menu:
        "Go home":
            jump Gohome01
        "Release urges":
            jump urges01
    scene inertiaday1-781
label urges01:
    scene iu25-722
    pause
    scene iu25-723
    p "{i}Fuck... I'm so horny..."
    scene iu25-724
    play sound "doorslam.ogg"
    pause
    scene iu25-725
    pause
    scene iu25-726
    pause
    scene iu25-727
    p "{i}Mmmm..."
    scene iu25-728
    p "{i}I've been needing this all day..."
    scene iu25-729
    p "{i}I'm so sensitive..."
    scene iu25-731
    p "Oh yeah..."
    scene iu25-732
    p "{i}I need more..."
    scene iu25-729
    pause
    scene iu25-730
    pause
    scene iu25-733
    p "{i}OH....yeahhh."
    scene iu25-733
    play sound "2step.ogg"
    scene iu25-734
    pause
    menu:
        "Ignore the noise":
            jump ignore02
        "Notice the noise":
            jump hearnoise01
label ignore02:
    scene iu25-733
    p "{i}This feels so good..."
    $ renpy.movie_cutscene("iu25-004ani.webm", loops=-1)
    scene iu25-735
    p "{i}Holy shit...!"
    scene iu25-736
    p "Yes....!"
    scene iu25-737
    p "I'M CUMMING!"
    scene iu25-730
    pause
    scene iu25-738
    p "Ahhh...."
    scene iu25-739
    pause
    scene iu25-740
    pause
    scene iu25-741
    pause
    scene iu25-742
    p "{i}Holy shit..."
    scene iu25-743
    p "{i}I don't think I've ever cum that hard before... I'm a total mess."
    scene iu25-744
    p "{i}Ha... I... Umm... I'd better head home."
    jump backhome02
label hearnoise01:
    scene iu25-745
    pause
    scene iu25-746
    pause
    scene iu25-747
    p "{i}What the heck...?"
    menu:
        "Get MAD!":
            jump mad01
        "Give in to temptation...":
            jump pleasure01
label mad01:
    scene iu25-748
    p "GET LOST YOU ABSOLUTE HORSE COCKED FREAK!!!"
    scene iu25-749
    pause
    scene iu25-750
    pause
    scene iu25-751
    pause
    scene iu25-752
    p "{i}Much better... now where was I...?"
    scene iu25-732
    p "{i}Oh....yeah."
    jump ignore02
label pleasure01:
    scene iu25-753
    p "{i}I feel so naughty... you know what...?"
    scene iu25-754
    p "{i}Oh my god...!"
    scene iu25-755
    p "{i}I've never seen a cock this big before..."
    p "{i}I need to touch it..."
    scene iu25-756
    p "{i}How would this even fit inside anybody...?"
    scene iu25-757
    p "{i}I can barely hold onto it... what am I doing...?"
    scene iu25-758
    p "{i}This is so wrong, but I can't control myself..."
    scene iu25-759
    pause
    scene iu25-760
    pause
    s "Oh yeahhhhhhhhh!"
    scene iu25-761
    p "{i}I have a stranger's cock in my mouth..."
    scene iu25-762
    p "{i}And I'm pleasuring myself to it..."
    scene iu25-763
    p "{i}I have no control..."
    scene iu25-763
    p "{i}I want to suck it..."
    scene iu25-768
    p "Mmm..."
    scene iu25-765
    p "I wish someone was in me right now..."
    $ renpy.movie_cutscene("iu25-005ani.webm", loops=-1)
    $ renpy.movie_cutscene("iu25-006ani.webm", loops=-1)
    scene iu25-770
    p "{i}Holy shit, I'm gonna fuckin' cum..."
    scene iu25-769
    p "MMMMMmmmm...."
    scene iu25-765
    pause
    scene iu25-766
    pause
    scene iu25-767
    p "{i}FUCKKK........."
    scene iu25-769
    p "Oh my god..."
    scene iu25-770
    s "Ahhhhhhhhhh..."
    p "{i}Ah?"
    scene iu25-771
    p "AH!"
    scene iu25-772
    play sound "gulp.ogg"
    p "{i}*gulp*"
    scene iu25-773
    pause
    scene iu25-774
    pause
    p "{i}What did I just do...?"
    scene iu25-775
    p "{i}I... just blew a stranger... and let him cum in my mouth...!"
    p "...and then I swallowed it...!!!"
    scene iu25-776
    p "{i}I'm still so turned on... I came everywhere... I couldn't control myself... Oh my god, I'm such a bad girl!"
    scene iu25-777
    p "{i}Hmmm..... But, it felt sooo good!"
    scene iu25-778
    p "{i}I need to go, this doesn't feel real."
    jump backhome02
label Gohome01:
    scene iu25-779
    p "{i}Safer to head home I think, I'm just a little bit scared to talk to Tenika about Amy..."
    scene iu25-780
    p "{i}I'm sure it will be okay..."
    scene iu25-781
    p "{i}I need to tell her, she will understand...I hope."
    jump backhome02
label backhome02:
    scene iu25-782
    p "{i}I'm so exhausted... It's good to be home."
    scene iu25-783
    pause
    scene iu25-784
    pause
    scene iu25-785
    p "{i}Oh hello you..."
    scene iu25-786
    p "{i}Hmm...."
    scene iu25-787
    p "{i}You know what...?"
    scene iu25-788
    pause
    scene iu25-789
    pause
    scene iu25-790
    pause
    scene iu25-791
    pause
    scene iu25-794
    p "{i}Mmm..."
    scene iu25-792
    pause
    scene iu25-793
    pause
    i "Ooo."
    scene iu25-795
    p "{i}It goes in so easily now..."
    scene iu25-796
    p "{i}Hehe."

    scene iu25-797
    p "{i}Mmm... I better go speak to Nika, I wonder what she's up to?{i}"
    scene iu25-798
    t "Eeeeeeee!"
    scene iu25-799
    t "{i}Frig, this hurts.{i}"
    scene iu25-800
    t "{i}Why am I like this?{i}"
    scene iu25-802
    t "{i}A little bit more...{i}"
    scene iu25-803
    t "Huh...?"
    scene iu25-804
    p "What on earth are you doing?"
    scene iu25-805
    t "Tryna be as flexible as my big sis, what do ya think?"
    scene iu25-806
    t "Ooh!"
    scene iu25-807
    t "Ah!"
    scene iu25-808
    t "Haha!"
    scene iu25-809
    p "You're an absolute idiot! You know that, right?"
    scene iu25-810
    p "Here, let me help you."
    scene iu25-811
    t "Why thank you, upside down lady."
    scene iu25-812
    t "Eee."
    scene iu25-813
    t "Hehe thanks, [p]."
    scene iu25-814
    p "It's really good to see you practising flexibility, but be careful, okay...?"
    scene iu25-815
    p "...I have to talk to you about something."
    scene iu25-816
    p "Ummm..."
    scene iu25-817
    t "What...?"
    scene iu25-818
    t "Tell me."
    scene iu25-819
    p "Well, today was very strange..."
    scene iu25-820
    p "I mean, it was a good day and all, I had a lot of fun..."
    scene iu25-821
    t "JUST TELL ME!"
    scene iu25-822
    p "Alright, sorry... I went to the beach with Jen and..."
    p "..."
    p "... That's a story for another day, I think..."
    scene iu25-823
    p "Anyway, shortly after, I went to see Amy for the costume..."
    scene iu25-824
    p "Then uh... I don't really know how to explain it, there was a moment and we... Uh..."
    scene iu25-825
    t "You what...?"
    scene iu25-826
    p "We umm..."
    scene iu25-827
    p "Well she..."
    p "... and you see... I...."
    p "..."
    p "{i}*sigh*"
    scene iu25-828
    p "We kissed..."
    scene iu25-829
    t "..."
    scene iu25-830
    p "I'm so sorry Nika, please don't look at me like that I-"
    scene iu25-831
    t "iM sOrRy NiKa ThErE wAs A MoMeNt, AnD wE kIsSeD!"
    scene iu25-832
    t "She's European, she kisses everybody you dumbass!"
    scene iu25-833
    p "Wait... WHAT?"
    scene iu25-834
    t "Why? Did it turn you on, and you thought you betrayed your little sister?"
    scene iu25-835
    p "Nooo, I don't know what you mean!! I kept thinking about it all day, and I felt SO bad!"
    scene iu25-836
    t "Uh-huh."
    scene iu25-837
    t "I bet that, if given the chance, you'd even kiss your little sister too, huh?"
    scene iu25-838
    t "Wouldn't ya?"
    scene iu25-839
    p "Umm, Tenika...?"
    p "{i}Is she really going to...?"
    scene iu25-840
    pause
    scene iu25-841
    p "{i}Oh god!..."
    scene iu25-842
    t "..."
    scene iu25-843
    p "...Uh."
    scene iu25-844
    pause
    scene iu25-845
    pause
    scene iu25-846
    t "Oh my god! You so would!"
    scene iu25-847
    p "... Noooo!"
    p "{i}Yesss...!"
    p "{i}Maaaybee...?"
    scene iu25-848
    play sound "dooropen.ogg"
    pause
    scene iu25-849
    r "Hey, girls!"
    scene iu25-850
    r "Sorry Nika, your door was open. How were days today, girls?"
    scene iu25-851
    t "[p] was telling me how her and Amy ki-"
    scene iu25-852
    t "erm mermy merh merp."
    scene iu25-853
    p "Haha..."
    scene iu25-854
    p "What I was telling Tenika, is how Amy, {i}KIND-HEARTEDLY{/i}, gave me a costume to wear for the party tonight."
    scene iu25-855
    t "Meergghhmereregghh mergh mergh mer."
    scene iu25-856
    r "That's kind of her to do that, but I don't see why you have to hold your sister's mouth?"
    scene iu25-857
    r "Unless there was something {i}else{/i} I needed to know...?"
    scene iu25-855
    pause
    t "Moh mir."
    scene iu25-858
    r "Either way, I'm sure you can tell me more about it in the car. We need to go for a family drive."
    scene iu25-859
    r "There's something that I need to discuss with you both..."
    scene iu25-860
    r "Especially you, Nika!"
    scene iu25-861
    t "Meh mir."
    scene iu25-862
    r "{i}I've been dreading this for a while now, but I knew this day was going to come sooner or later! I'll do this the same as I did with [p]."
    scene iu25-864
    p "{i}Phew!"
    scene iu25-863
    pause
    scene iu25-864
    pause
    scene iu25-865
    p "Oh!"
    scene iu25-866
    p "Sorry, Haha!"
    scene iu25-867
    t "You're naughty!"
    scene iu25-868
    p "I did us a favour!"
    scene iu25-869
    p "Now c'mon, let's get ready, Dad's waiting. Wear your matching PJ's!"
    scene iu25-870
    t "Yes, my naughty sister!"
    scene iu25-871
    p "{i}I can only imagine what Dad wants to talk to us about. I assume it's time..."
    scene iu25-873
    pause
    scene iu25-874
    r "{i}It'll be fine! I just have to tell her the same way I told [p]."
    scene iu25-875
    r "{i}She'll be okay, just like her big sister was... eventually!"
    scene iu25-876
    pause
    scene iu25-877
    pause
    scene iu25-878
    r "Are you ready girls?"
    scene iu25-879
    p "Ready when you are, Dad."
    scene iu25-880
    pause
    scene iu25-881
    pause
    scene iu25-882
    pause
    scene iu25-883
    t "Hahahaha!"
    scene iu25-884
    r "You good, girls?"
    scene iu25-885
    p "Yes, Dad."
    scene iu25-886
    r "Great! Because I need to talk to you about something that's quite serious..."
    r "But first..."
    scene iu25-887
    t " What!?"
    "Save your game here!"
    "Thank you for playing Inertia v0.25"
    "Big thanks to the support on Patreon and Discord & also to the Dev Team."
    "If you would like to help me to get the updates out faster, please consider joining my Patreon!"
    "See you soon, -Dob"
    pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
