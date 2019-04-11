# RootMe

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This program will allow you to see information about a person precisely like the information like the number of point, the number of chatbox I'm going a little you show my program below.

Lang Information
----
The [-l/--lang] option will allow you to see the user's language.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --lang
    [..SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo

    [+] Lang of the user : fr

As you can see the language of the user has been found successfully.

Chatbox Information
----
This options will show the number of posts posted on the chatbox.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --chatbox
    [..SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo

    [+] ChatBox of the user : 0

Me in my case I put 0 post in the chatbox.

Point Information
----
This option allows you to see the point numbers on the user in question.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --point
    [..SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo

    [+] Point of Seyptoo : 600

So in my case I only have 600 points because I am not active.

Status of User
----
This is to see the status of the user if he is visitor, moderator, administrator etc.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --status
    [...SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo

    [+] Status of the user : Visiteur

So me in my case I am a user.

Challenge RootMe
----
This part allows to see the challenges hacked or not. So I'm going to show you a little explanation.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --Challenge=Programming
    [..SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo

    [-] Go-back-to-college-147 : Not Owned
    [-] Encoded-string : Not Owned
    [-] The-Roman-s-wheel-151 : Not Owned
    [-] Uncompress-me : Not Owned
    [-] CAPTCHA-me-if-you-can : Not Owned
    [-] Arithmetic-progression-18 : Not Owned
    [-] ELF-x64-Shellcoding-Sheep-warmup : Not Owned
    [-] ELF-x64-Shellcoding-Polymorphism : Not Owned
    [-] Quick-Response-Code : Not Owned
    [-] ELF64-Shellcoding : Not Owned
    [-] ELF-x86-Shellcoding-Alphanumeric : Not Owned

So as you can see I own none of his challenges.

CTF RootMe
----
So this part will show the machines hacked or not, the whole machine.

    seyptoo@Computer:~/root-me$ python root-me.py -u Seyptoo --machines
    [..SNIP...]
    [+] User : Seyptoo
    [+] URL : https://www.root-me.org/Seyptoo
    
    Analougepond Not Owned
    ARM FTP box Not Owned
    Awky Not Owned
    [...SNIP...]
    Metasploitable 2 Owned
    Minotaur Not Owned
    
