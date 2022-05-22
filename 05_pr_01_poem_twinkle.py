with open('poems.txt','w') as f:
    a = f.write('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# The above code is used fr the file fromation and the below code is used for the searchimg of the word in the file.

f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print ('Twinkle is present')
else :
    print ('Twinkle is not present')

f.close()
